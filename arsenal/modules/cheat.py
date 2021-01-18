#!/usr/bin/python3
from pathlib import Path

from docutils.parsers import rst
from docutils.utils import new_document
from docutils.frontend import OptionParser
from docutils import nodes


class Cheat:
    name = ""
    str_title = ""
    titles = []
    filename = ""
    tags = ""
    command = ""
    printable_command = ""
    description = ""
    variables = dict()
    command_capture = False

    def is_done(self):
        return self.name != "" and self.command != "" and not self.command_capture

    def inline_cheat(self):
        return "{}{}{}".format({self.tags}, {self.name}, {self.command})


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

    def end_cheat(self):
        self.current_cheat.tags = self.current_tags
        self.current_cheat.str_title = ", ".join(self.titles[:-1])
        if self.current_cheat.str_title == '':
            self.current_cheat.str_title = self.firsttitle
        self.cheatlist.append(self.current_cheat)

    # -----------------------------------------------------------------------------#
    # RestructuredText                                                            #
    # -----------------------------------------------------------------------------#

    def parse_restructuredtext(self, filename):
        self.firsttitle = ""
        self.current_tags = ""
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
    # Markdown                                                                    #
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
        nb = 0

        with open(filename) as f:
            for entry in f.readlines():
                line = entry.strip('\n')
                nb += 1

                # Previous cheat completed ? -> Create a new one
                if self.current_cheat.is_done():
                    self.end_cheat()
                    self.new_cheat()

                # TAGS
                if line.startswith('%'):
                    # replace current tags (metadata)
                    self.current_tags = line[1:].strip()
                    continue

                # Name & Titles
                if line.startswith('#'):

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

                    # Save first title (incase only niv1 title are used)
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
            "rst": self.parse_restructuredtext
        }
        paths = [paths] if isinstance(paths, str) else paths
        for path in paths:
            for file_format in file_formats:
                for entry in Path(path).rglob('*.{0}'.format(file_format)):
                    if entry.name not in exclude_list and file_format in parsers.keys():
                        parsers[file_format](str(entry.absolute()))
        return self.cheatsheets
