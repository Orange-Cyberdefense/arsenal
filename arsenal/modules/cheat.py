#!/usr/bin/python3
from pathlib import Path

from docutils.parsers import rst
from docutils.utils import new_document
from docutils.frontend import OptionParser
from docutils import nodes

from yaml import load as yml_load, FullLoader
import re


class Cheat:
    name = ""
    str_title = ""
    titles = []
    filename = ""
    tags = ""
    command_tags = {}
    command = ""
    printable_command = ""
    description = ""
    variables = dict()
    command_capture = False
    rate = 0

    def is_done(self):
        return self.name != "" and self.command != "" and not self.command_capture

    def inline_cheat(self):
        return "{}{}{}".format({self.tags}, {self.name}, {self.command})

    def get_rating(self):
        # Rating
        rate = ""
        for i in range(0, 5):
            if self.rate <= i:
                rate += "★"
            else:
                rate += "⭐"
        return rate

    def get_tags(self):
        tags_dict = {'target/local': 'Loc',
                     'target/remote': 'Rem',
                     'target/serve': 'Ser',
                     'platform/linux': '[L] ',
                     'platform/windows': '[W] ',
                     'platform/mac': '[M] ',
                     'platform/multiple': '[*] '}

        tag_string = ''
        if self.command_tags is not None:
            for tag_key in self.command_tags.keys():
                tag = tag_key + '/' + self.command_tags[tag_key]
                if tag in tags_dict.keys():
                    tag_string += '' + tags_dict[tag]
                elif 'cat/' in tag:
                    tag_string += ' ' + tag.split('cat/')[1].upper().strip()
                # else:
                #     tag_string += '|' + tag.lower().strip()
        return tag_string


class ArsenalRstVisitor(nodes.GenericNodeVisitor):
    def __init__(self, document, cheats):
        self.cheats = cheats
        super().__init__(document)

    def default_visit(self, node):
        # Previous cheat completed ? -> Create a new one
        if self.cheats.current_cheat.is_done():
            self.cheats.end_cheat()
            self.cheats.new_cheat()

    def visit_section(self, node):
        """Cheats and titles"""
        # if no cmd but description use description as the command
        if self.cheats.current_cheat.command == "" and \
                self.cheats.current_cheat.description != "":
            self.cheats.current_cheat.command = self.cheats.current_cheat.description.replace('\n', ';\\\n')
            self.cheats.current_cheat.description = ""
            self.cheats.end_cheat()
            self.cheats.new_cheat()
        # Parsing is based on sections (delimited by titles)
        current = " ".join(node.get('ids'))
        niv = 0
        if isinstance(node.parent, nodes.document):
            self.cheats.firsttitle = current
            self.cheats.titles = [current]
        else:
            parent = " ".join(node.parent.get('ids'))
            niv = self.cheats.titles.index(parent) + 1
            self.cheats.titles = self.cheats.titles[:niv] + [current]
        self.cheats.new_cheat()
        # Set default tag to all titles tree
        self.cheats.current_tags = ", ".join(self.cheats.titles)

    def visit_comment(self, node):
        """Tags"""
        self.cheats.current_tags = node.astext()

    def visit_literal_block(self, node):
        """Commands"""
        self.cheats.current_cheat.command = node.astext().replace("\n", " \\\n")

    def visit_paragraph(self, node):
        """Descriptions, constants and variables"""
        para = node.astext()
        descr = []  # Using mutable objects for string concat
        for line in para.split("\n"):
            # Constants and variables
            if line.startswith("=") or line.startswith("$") and ":" in line:
                varname, varval = [x.strip() for x in line[1:].split(":")]
                if line.startswith("$"):
                    varval = "$({0})".format(varval)
                self.cheats.filevars[varname] = varval
            elif line.endswith(":"):  # Name
                self.cheats.current_cheat.name = line[:-1]
            else:  # Description
                descr += [line]
        # If description list is not empty, convert it to string as description
        # Here we only do this if command has been filled to avoid junk text
        if len(descr) and len(self.cheats.current_cheat.command):
            self.cheats.current_cheat.description = "\n".join(descr)
            # For me descriptions are in paragraphs not title so I use the descr as a name
            self.cheats.current_cheat.name = " ".join(descr)


class Cheats:
    current_cheat = Cheat()
    cheatsheets = dict()

    def new_cheat(self):
        self.current_cheat = Cheat()
        self.current_cheat.command = ''
        self.current_cheat.description = ''
        if self.titles == []:
            self.current_cheat.titles = ""
            self.current_cheat.name = ""
        elif len(self.titles) == 1:
            self.current_cheat.titles = ""
            self.current_cheat.name = self.titles[-1]
        else:
            self.current_cheat.titles = "".join(self.titles[:-1])
            self.current_cheat.name = self.titles[-1]
        # self.current_cheat.command_tags = {}

    def end_cheat(self):
        self.current_cheat.tags = self.current_tags
        self.current_cheat.str_title = ", ".join(self.titles[:-1])
        if self.current_cheat.str_title == '':
            self.current_cheat.str_title = self.firsttitle
        # merge ref cmd_tags (title) with current_cheat cmd tags
        if len(self.command_tags_ref) > 0:
            cmd_tags = self.command_tags_ref.copy()
            cmd_tags.update(self.current_cheat.command_tags)
            self.current_cheat.command_tags = cmd_tags
        self.cheatlist.append(self.current_cheat)

    # -----------------------------------------------------------------------------#
    # RestructuredText                                                             #
    # -----------------------------------------------------------------------------#

    def parse_restructuredtext(self, filename):
        self.firsttitle = ""
        self.current_tags = ""
        self.command_tags_ref = {}
        self.filevars = {}
        self.titles = []
        self.cheatlist = []
        self.new_cheat()

        parser = rst.Parser()
        with open(filename, "r") as fd:
            text = fd.read()
            settings = OptionParser(components=(rst.Parser,)).get_default_values()
            document = new_document(filename + ".tmp", settings)
            parser.parse(text, document)
            visitor = ArsenalRstVisitor(document, self)
            document.walk(visitor)

            # add the last command if done
            if self.current_cheat.is_done():
                self.end_cheat()
            elif self.current_cheat.command == "" and self.current_cheat.description != "":
                self.current_cheat.command = self.current_cheat.description.replace('\n', ';\\\n')
                self.current_cheat.description = ""
                self.end_cheat()

        # File parsing done
        # set constants variables
        for varname, varval in self.filevars.items():
            for cheat in self.cheatlist:
                cheat.variables[varname] = varval

        # add all file's cheats 
        for cheat in self.cheatlist:
            cheat.filename = filename
            cheat.printable_command = cheat.command.replace('\\\n', '')
            self.cheatsheets[cheat.str_title + cheat.name] = cheat

    # -----------------------------------------------------------------------------#
    # Yaml                                                                         #
    # -----------------------------------------------------------------------------#

    def parse_yaml(self, filename):
        self.cheatlist = []
        self.titles = []
        self.filevars = {}

        required_fields = ["name", "cmds"]

        with open(filename, "r") as fd:
            yml_text = yml_load(fd, Loader=FullLoader)

            for tool_id in yml_text.keys():
                self.command_tags_ref = {}
                self.firsttitle = ""
                self.current_tags = ""

                tool = yml_text[tool_id]

                if all(item in tool.keys() for item in required_fields):
                    self.firsttitle = tool["name"]

                    if "tags" in tool.keys():
                        self.current_tags = ", ".join(tool["tags"])

                    if "const_variables" in tool.keys():
                        for variable in tool["const_variables"]:
                            varname, varval = list(variable.items())[0]
                            self.filevars[varname] = varval

                    if "exec_variables" in tool.keys():
                        for variable in tool["exec_variables"]:
                            varname, varval = list(variable.items())[0]
                            self.filevars[varname] = "$(" + varval + ")"

                    if "command_tags" in tool.keys():
                        for cmd_tag in tool["command_tags"]:
                            if "/" in cmd_tag:
                                cat, value = cmd_tag.split("/", 1)
                                self.command_tags_ref[cat] = value

                    for cmd_id in tool["cmds"].keys():
                        cmd = tool["cmds"][cmd_id]

                        self.new_cheat()
                        self.current_cheat.name = cmd["name"]
                        self.current_cheat.command = cmd["cmd"]
                        self.current_cheat.description = cmd["description"]

                        self.current_cheat.command_tags = {}
                        if "command_tags" in cmd.keys():
                            for cmd_tag in cmd["command_tags"]:
                                if "/" in cmd_tag:
                                    cat, value = cmd_tag.split("/", 1)
                                    self.current_cheat.command_tags[cat] = value
                        
                        self.end_cheat()

        for varname, varval in self.filevars.items():
            for cheat in self.cheatlist:
                cheat.variables[varname] = varval

        for cheat in self.cheatlist:
            cheat.filename = filename
            cheat.printable_command = cheat.command.replace('\\\n', '')
            self.cheatsheets[cheat.str_title + cheat.name] = cheat

    # -----------------------------------------------------------------------------#
    # Markdown                                                                     #
    # -----------------------------------------------------------------------------#

    def parse_markdown(self, filename):

        # Nested markdown stuff
        def parse_title(title):
            c = title[0]
            niv = 0
            while c == '#':
                niv += 1
                title = title[1:]
                c = title[0]
                title = title.lstrip()
            return niv, title

        self.firsttitle = ''
        self.cheatlist = []
        self.current_tags = ''
        self.filevars = {}
        self.titles = []
        self.new_cheat()
        self.command_tags_ref = {}
        nb = 0

        with open(filename) as f:
            for entry in f.readlines():
                line = entry.strip('\n')
                nb += 1

                # Previous cheat completed ? -> Create a new one
                if self.current_cheat.is_done():
                    self.end_cheat()
                    self.new_cheat()

                # cheat TAGS
                if line.startswith('%'):
                    # replace current tags (metadata)
                    self.current_tags = line[1:].strip()
                    continue

                # Name & Titles
                if line.startswith('# ') or line.startswith('##'):
                    if self.current_cheat.command_capture:
                        raise Exception('Error parsing (Title) markdown file ' + filename + ' line: ' + str(nb))
                    # if no cmd but description use description as the command
                    if self.current_cheat.command == "" and self.current_cheat.description != "":
                        self.current_cheat.command = self.current_cheat.description.replace('\n', ';\\\n')
                        self.current_cheat.description = ""
                        self.end_cheat()
                        self.new_cheat()

                    # New title found !
                    niv, title = parse_title(line)

                    # Save first title (in case only niv1 title are used)
                    if self.firsttitle == "":
                        self.firsttitle = title

                    # Title hierarchy verification
                    if (niv == (len(self.titles) + 1)):
                        # new sub title
                        self.titles.append(title)

                    elif (niv == (len(self.titles))):
                        # New same title
                        self.titles[-1] = title

                    elif (niv < len(self.titles)):
                        # New parent title
                        self.titles = self.titles[:niv - 1]
                        self.titles.append(title)

                    else:
                        raise Exception('Error parsing (Title Skip) markdown file ' + filename + ' line: ' + str(nb))
                    self.new_cheat()
                    continue

                # CMD TAGS (with #tag format on same line)
                if re.match(r'^#[^\s#]', line):
                    # replace current tags (metadata)
                    cmd_tags = re.split(r'#([^\s#]+)', line)
                    cmd_tags = ' '.join(cmd_tags).split()
                    #if niv > 1:
                    # reset current_cheat tag with backup of lvl1 title
                    self.current_cheat.command_tags = self.command_tags_ref
                    for cmd_tag in cmd_tags:
                        tag_split = cmd_tag.split('/')
                        if len(tag_split) >= 2:
                            cmd_tag_key = tag_split[0]
                            cmd_tag_value = "/".join(tag_split[1:])
                            self.current_cheat.command_tags[cmd_tag_key] = cmd_tag_value
                    if niv <= 1:
                        self.command_tags_ref = self.current_cheat.command_tags.copy()
                    continue

                # CMD Start/End
                if line.startswith('```'):
                    if self.current_cheat.name != "":
                        self.current_cheat.command_capture = not self.current_cheat.command_capture
                    else:
                        raise Exception('Error parsing (CMD Start/End) markdown file ' + filename)
                    continue

                # CMD
                if line.strip() != '' and self.current_cheat.command_capture:
                    if self.current_cheat.name != "":
                        if self.current_cheat.command == "":
                            # first line
                            self.current_cheat.command = line.rstrip()
                        else:
                            # multi lines cmd
                            if self.current_cheat.command[-1] == ';':
                                self.current_cheat.command += "\\\n" + line.rstrip()
                            else:
                                self.current_cheat.command += ";\\\n" + line.rstrip()
                        continue
                    else:
                        raise Exception('Error parsing (CMD) markdown file ' + filename)

                # Executable Variables
                if line.startswith('$') and not self.current_cheat.command_capture:
                    varname = line[2:].split(':')[0].strip()
                    varval = line[2:].split(':')[1].strip()
                    self.filevars[varname] = "$(" + varval + ")"
                    continue

                # Constant Variables
                if line.startswith('=') and not self.current_cheat.command_capture:
                    varname = line[2:].split(':')[0].strip()
                    varval = line[2:].split(':')[1].strip()
                    self.filevars[varname] = varval
                    continue

                # Else -> description
                if line.strip() != '':
                    if self.current_cheat.description == '':
                        self.current_cheat.description += line.rstrip()
                    else:
                        self.current_cheat.description += '\n' + line.rstrip()

            # add the last command if done
            if self.current_cheat.is_done():
                self.end_cheat()
            elif self.current_cheat.command == "" and self.current_cheat.description != "":
                self.current_cheat.command = self.current_cheat.description.replace('\n', ';\\\n')
                self.current_cheat.description = ""
                self.end_cheat()

        # File parsing done
        # set constants variables
        for varname, varval in self.filevars.items():
            for cheat in self.cheatlist:
                cheat.variables[varname] = varval

                # add all file's cheats
        for cheat in self.cheatlist:
            cheat.filename = filename
            cheat.printable_command = cheat.command.replace('\\\n', '')
            self.cheatsheets[cheat.str_title + cheat.name] = cheat

    def read_files(self, paths, file_formats, exclude_list):
        parsers = {
            "md": self.parse_markdown,
            "rst": self.parse_restructuredtext,
            "yml": self.parse_yaml
        }
        paths = [paths] if isinstance(paths, str) else paths
        for path in paths:
            for file_format in file_formats:
                for entry in Path(path).rglob('*.{0}'.format(file_format)):
                    if entry.name not in exclude_list and file_format in parsers.keys():
                        parsers[file_format](str(entry.absolute()))
        return self.cheatsheets
