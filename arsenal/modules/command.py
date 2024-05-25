import re
import curses
import textwrap


class Command:
    cmdline = ""
    description = ""
    args = []  # [(name, value)]
    nb_place_holder = 0
    nb_lines_cmd = 1
    nb_lines_desc = 0

    def __init__(self, cheat, gvars):
        self.cmdline = cheat.command
        self.nb_place_holder = 0

        self.cmd_tags = cheat.command_tags
        self.description = ''
        for tag in self.cmd_tags:
            self.description += '[' + self.cmd_tags[tag] + '] '
        if self.description != '' and cheat.description != '':
            self.description += '\n-----\n'
        self.description += cheat.description

        self.compute_args(cheat, gvars)
        # careful this is not the lines number in GUI
        self.nb_lines_cmd = len(cheat.command.split('\n'))
        # careful this is not the lines number in GUI
        self.nb_lines_desc = 0 if cheat.description == '' else len(cheat.description.split('\n'))

    def get_description_cut_by_size(self, size):
        """
        The description cut by lines inside the gui size
        """
        desc_lines = self.description.split('\n')
        result = []
        for line in desc_lines:
            result.extend(textwrap.wrap(line, size))
        return result

    def compute_args(self, cheat, gvars):
        """
        Process cmdline from the cheatsheet to get args names
        """
        self.args = {}
        for position, arg_name in enumerate(re.findall(r"<([^ <>]+)>", cheat.command)):
            if "|" in arg_name:  # Format <name|default_value>
                name, var = arg_name.split("|")[:2]
                self._add_arg(name, var, position)
                # Variable has been added to cheat variables before, remove it
                cheat.command = cheat.command.replace(arg_name, name)
                self.cmdline = cheat.command
            elif arg_name in gvars:
                self._add_arg(arg_name, gvars[arg_name], position)
            elif arg_name in cheat.variables:
                self._add_arg(arg_name, cheat.variables[arg_name], position)
            else:
                self._add_arg(arg_name, "", position)

    def _add_arg(self, name=None, value="", position=0):
        if name in self.args:
            self.args[name]["value"] = value
            self.args[name]["positions"].append(position)
        else:
            v = {}
            v["value"] = value
            v["positions"] = [position]
            self.args[name] = v
        self.nb_place_holder += 1

    def get_arg(self, position):
        for k, v in self.args.items():
            if position in v["positions"]:
                return k, v["value"]
        return f"{position}", f"|{self.nb_place_holder}|"

    def set_arg_value(self, position, value):
        for k, v in self.args.items():
            if position in v["positions"]:
                self.args[k]["value"] = value

    def get_command_parts(self):
        if self.nb_place_holder != 0:
            regex = "|".join("<" + arg + ">" for arg in self.args)
            cmdparts = re.split(regex, self.cmdline)
        else:
            cmdparts = [self.cmdline]
        return cmdparts

    def build(self):
        """
        Called after argument completion
        -> if some args values are still empty do nothing
        -> else build the final command string by adding args values
        """
        if self.nb_place_holder == 0 :
            return True
        argsval = [a[1] for a in self.args]
        if "" not in argsval:
            # split cmdline at each arg position
            regex = "|".join("<" + arg + ">" for arg in self.args)
            cmdparts = re.split(regex, self.cmdline)
            # concat command parts and arguments values to build the command
            self.cmdline = ""
            for i in range(len(cmdparts) + self.nb_place_holder):
                if i % 2 == 0:
                    self.cmdline += cmdparts[i // 2]
                else:
                    _, value = self.get_arg((i - 1) // 2)
                    self.cmdline += value
            curses.endwin()

        # build ok ?
        return "" not in argsval
