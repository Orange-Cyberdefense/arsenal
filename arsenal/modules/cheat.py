#!/usr/bin/python3
from pathlib import Path


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Cheat:
    name = ""
    str_title = ""
    titles = []
    filename = ""
    tags = ""
    command = ""
    printable_command = ""
    variables = dict()
    command_capture = False

    def is_done(self):
        return self.name != "" and self.command != "" and not self.command_capture

    def inline_cheat(self):
        return "{}{}{}".format({self.tags},{self.name},{self.command})

class Cheats:
    current_cheat = Cheat()
    cheatsheets = dict()


    def parse_title(self, title):
        c = title[0]
        niv = 0
        while c == '#':
            niv += 1
            title = title[1:]
            c = title[0]
        title = title.lstrip()
        return niv,title


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


    def parse_markdown(self, filename):
        
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
                        raise Exception('Error parsing (Title) markdown file '+filename+' line: '+str(nb))
                    # if no cmd but description use description as the command
                    if self.current_cheat.command == "" and self.current_cheat.description != "":
                        self.current_cheat.command = self.current_cheat.description.replace('\n',';\\\n')
                        self.current_cheat.description = ""
                        self.end_cheat()
                        self.new_cheat()

                    # New title found !
                    niv,title = self.parse_title(line)

                    # Save first title (incase only niv1 title are used)
                    if self.firsttitle == "":
                        self.firsttitle = title

                    # Title hierarchy verification
                    if (niv == (len(self.titles)+1)):
                        # new sub title
                        self.titles.append(title)

                    elif (niv == (len(self.titles))):
                        # New same title
                        self.titles[-1] = title

                    elif (niv < len(self.titles)):
                        # New parent title
                        self.titles = self.titles[:niv-1]
                        self.titles.append(title)

                    else: 
                        raise Exception('Error parsing (Title Skip) markdown file '+filename+' line: '+str(nb))
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
                                self.current_cheat.command += "\\\n"+line.rstrip()
                            else:
                                self.current_cheat.command += ";\\\n"+line.rstrip()
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
                self.current_cheat.command = self.current_cheat.description.replace('\n',';\\\n')
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
            cheat.printable_command = cheat.command.replace('\\\n','')
            self.cheatsheets[cheat.str_title+cheat.name] = cheat

    def read_files(self, paths):
        for path in paths:
            for entry in Path(path).rglob('*.md'):
                if entry.name != 'README.md':
                    self.parse_markdown(str(entry.absolute()))
        return self.cheatsheets
