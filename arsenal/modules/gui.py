import time
import curses
import math
import json
from curses import wrapper
from os.path import commonprefix, exists, isdir
from os import sep
import glob

#  local
from . import config
from . import command


class CheatslistMenu:
    globalcheats = []  # all cheats
    cheats = []  # cheats after search
    max_visible_cheats = 0
    input_buffer = ''
    position = 0
    page_position = 0

    xcursor = None
    x_init = None
    y_init = None

    @staticmethod
    def draw_prompt():
        """
        Create a prompt box
        at x : 0 / y : 5
        size 5 chars
        :return: the windows created
        """
        y, x = 5, 0
        ncols, nlines = 5, 1
        promptwin = curses.newwin(nlines, ncols, y, x)
        try:
            promptwin.addstr("\u2620  >", curses.color_pair(Gui.BASIC_COLOR))
        except:
            promptwin.addstr(">>>>", curses.color_pair(Gui.BASIC_COLOR))
        promptwin.refresh()
        return promptwin

    def draw_infobox(self):
        """
        Draw the top infobox (4 lines / width from param)
        :return: the window created
        """
        y, x = 0, 0
        ncols, nlines = self.width, 4
        infowin = curses.newwin(nlines, ncols, y, x)
        selected_cheat = self.selected_cheat()
        if selected_cheat is not None:
            infowin.addstr(y + 1, x + 2, Gui.draw_string(selected_cheat.name, self.width - 3),
                           curses.color_pair(Gui.INFO_NAME_COLOR))
            # infowin.addstr(y + 2, x + 2, Gui.draw_string(selected_cheat.description.split('\n')[0], self.width - 3),
            #                curses.color_pair(Gui.INFO_DESC_COLOR))
            infowin.addstr(y + 2, x + 2, Gui.draw_string(selected_cheat.printable_command, self.width - 3),
                           curses.color_pair(Gui.INFO_CMD_COLOR))
        infowin.border()
        infowin.refresh()
        return infowin

    def draw_editbox(self):
        """
        Draw the edition box (in the right of the prompt box
        """
        y, x = 5, 6
        ncols, nlines = self.width - 5, 1
        editwin = curses.newwin(nlines, ncols, y, x)
        editwin.addstr(self.input_buffer, curses.color_pair(Gui.BASIC_COLOR))
        editwin.refresh()
        return editwin

    @staticmethod
    def draw_cheat(win, cheat, selected):
        """
        Draw a cheat line in the cheats list menu
        :param win:
        :param cheat:
        :param selected:
        """
        win_height, win_width = win.getmaxyx()
        prompt = '> '
        max_width = win_width - len(prompt) - len("\n")


        col4_size = math.floor(max_width * 14 / 100)
        col3_size = math.floor(max_width * 8 / 100)
        col1_size = math.floor(max_width * 23 / 100)
        col2_size = math.floor(max_width * 55 / 100)
        #col0_size = math.floor(max_width * 20 / 100)

        title = cheat.tags if cheat.tags != '' else cheat.str_title

        tags = cheat.get_tags()

        if selected:
            win.addstr(prompt, curses.color_pair(Gui.CURSOR_COLOR_SELECT))
            win.addstr("{:{}s}".format(Gui.draw_string(tags, col4_size), col4_size),
                       curses.color_pair(Gui.COL4_COLOR_SELECT))
            win.addstr("{:{}s}".format(Gui.draw_string(cheat.str_title, col3_size), col3_size),
                       curses.color_pair(Gui.COL3_COLOR_SELECT))
            win.addstr("{:{}s}".format(Gui.draw_string(cheat.name, col1_size), col1_size),
                       curses.color_pair(Gui.COL2_COLOR_SELECT))
            win.addstr("{:{}s}".format(Gui.draw_string(cheat.printable_command, col2_size), col2_size),
                       curses.color_pair(Gui.COL3_COLOR_SELECT))
            # win.addstr("{:{}s}".format(Gui.draw_string(title, col0_size), col0_size),
            #            curses.color_pair(Gui.COL1_COLOR_SELECT))
            win.addstr("\n")
        else:
            win.addstr(' ' * len(prompt), curses.color_pair(Gui.BASIC_COLOR))
            if tags.startswith('[W]'):
                win.addstr("{:{}s}".format(Gui.draw_string(tags, col4_size), col4_size),
                           curses.color_pair(Gui.COL5_COLOR))
            else:
                win.addstr("{:{}s}".format(Gui.draw_string(tags, col4_size), col4_size),
                           curses.color_pair(Gui.COL4_COLOR))
            win.addstr("{:{}s}".format(Gui.draw_string(cheat.str_title, col3_size), col3_size),
                       curses.color_pair(Gui.COL1_COLOR))
            win.addstr("{:{}s}".format(Gui.draw_string(cheat.name, col1_size), col1_size),
                       curses.color_pair(Gui.COL2_COLOR))
            win.addstr("{:{}s}".format(Gui.draw_string(cheat.printable_command, col2_size), col2_size),
                       curses.color_pair(Gui.COL3_COLOR))
            # win.addstr("{:{}s}".format(Gui.draw_string(title, col0_size), col0_size),
            #            curses.color_pair(Gui.COL1_COLOR))
            win.addstr("\n")



    def draw_cheatslistbox(self):
        """
        Draw the box to show the cheats list
        """
        y, x = 6, 0
        ncols, nlines = self.width, self.height - 6
        listwin = curses.newwin(nlines, ncols, y, x)

        visible_cheats = self.cheats[self.page_position:self.max_visible_cheats + self.page_position]
        counter = self.page_position

        for cheat in visible_cheats:
            self.draw_cheat(listwin, cheat, counter == self.position)
            counter += 1

        listwin.refresh()

    def draw_footbox(self, info):
        """
        Draw the footer (number infos)
        :param info: str info to draw
        """
        y, x = self.height - 1, 0
        ncols, nlines = self.width, 1

        # print nb cmd info (bottom left)
        nbinfowin = curses.newwin(nlines, ncols, y, x)
        nbinfowin.addstr(info, curses.color_pair(Gui.BASIC_COLOR))
        nbinfowin.refresh()

        # print cheatsheet filename (bottom right)
        if self.selected_cheat() is not None:
            cheat_file = self.selected_cheat().filename

            # protection in case screen to small or name too long        
            if len(cheat_file) > self.width - 16:
                cheat_file = cheat_file[0:self.width - 17] + ".."

            fileinfowin = curses.newwin(nlines, ncols, y, self.width - (len(cheat_file) + 3))
            fileinfowin.addstr(cheat_file, curses.color_pair(Gui.BASIC_COLOR))
            fileinfowin.refresh()

    def match(self, cheat):
        """
        Function called by the iterator to verify if the cheatsheet match the entered values
        :param cheat: cheat to check
        :return: boolean
        """
        match = True

        # if search begin with '>' print only internal CMD
        if self.input_buffer != '' and self.input_buffer[0] == '>':
            match = cheat.command[0] == '>'

        for value in self.input_buffer.lower().split(' '):
            if value in cheat.str_title.lower() \
                    or value in cheat.name.lower() \
                    or value in cheat.tags.lower() \
                    or value in "".join(cheat.command_tags.values()).lower() \
                    or value in cheat.command.lower():
                match = True and match
            else:
                match = False
        return match

    def search(self):
        """
        Return the list of cheatsheet who match the searched term
        :return: list of cheatsheet to show
        """
        if self.input_buffer != '':
            list_cheat = list(filter(self.match, self.globalcheats))
        else:
            list_cheat = self.globalcheats
        return list_cheat

    def selected_cheat(self):
        """
        Return the selected cheat in the list
        :return: selected cheat
        """
        if len(self.cheats) == 0:
            return None
        return self.cheats[self.position % len(self.cheats)]

    def draw(self, stdscr):
        """
        Draw the main menu to select a cheatsheet
        :param stdscr: screen
        """
        self.height, self.width = stdscr.getmaxyx()
        self.max_visible_cheats = self.height - 7
        # create prompt windows
        self.draw_prompt()
        # create info windows
        self.draw_infobox()
        # create cheatslist box
        self.draw_cheatslistbox()
        # draw footer
        info = "> %d / %d " % (self.position + 1, len(self.cheats))
        self.draw_footbox(info)
        # create edit windows
        self.draw_editbox()
        # init cursor position (if first draw)
        if self.x_init is None or self.y_init is None or self.xcursor is None:
            self.y_init, self.x_init = curses.getsyx()
            self.xcursor = self.x_init
        # set cursor position
        curses.setsyx(self.y_init, self.xcursor)
        curses.doupdate()

    def move_position(self, step):
        """
        :param step:
        """
        # SCROLL ?
        #
        # 0                                ---------      
        # 1                                |       |
        # 2                       ->   -----------------    <-- self.page_position
        # 3                      |     |   |       |   |       
        # 4 max_visible_cheats = |     |   |       |   |
        # 5                      |     |  >|xxxxxxx|   |    <-- self.position      
        # 6                      |     |   |       |   |       
        # 7                       ->   -----------------    <-- self.page_position+max_visible_cheats
        # 8                                |       |
        # 9                                ---------        <-- len(self.cheats)
        self.position += step

        # clean position
        if self.position < 0: self.position = 0
        if self.position >= len(self.cheats) - 1: self.position = len(self.cheats) - 1

        # move page view UP
        if self.page_position > self.position:
            self.page_position -= (self.page_position - self.position)

            # move page view DOWN
        if self.position >= (self.page_position + self.max_visible_cheats):
            self.page_position += 1 + (self.position - (self.page_position + self.max_visible_cheats))

    def move_page(self, step):
        """
        :param step:
        """
        # only move if it is possible
        if len(self.cheats) > self.max_visible_cheats:
            new_pos = self.page_position + step * self.max_visible_cheats
            # clean position
            if new_pos >= (len(self.cheats) + 1 - self.max_visible_cheats):
                self.position = len(self.cheats) - 1
                self.page_position = len(self.cheats) - self.max_visible_cheats
            elif new_pos < 0:
                self.position = self.page_position = 0
            else:
                self.position = self.page_position = new_pos

    def check_move_cursor(self, n):
        return self.x_init <= (self.xcursor + n) < self.x_init + len(self.input_buffer) + 1

    def run(self, stdscr):
        """
        Cheats selection menu processing..
        :param stdscr: screen
        """
        # init
        Gui.init_colors()
        stdscr.clear()
        self.height, self.width = stdscr.getmaxyx()
        self.max_visible_cheats = self.height - 7
        self.cursorpos = 0

        while True:
            stdscr.refresh()
            self.cheats = self.search()
            self.draw(stdscr)
            c = stdscr.getch()
            if c == curses.KEY_ENTER or c == 10 or c == 13:
                # Process selected command (if not empty)
                if self.selected_cheat() is not None:
                    Gui.cmd = command.Command(self.selected_cheat(), Gui.arsenalGlobalVars)
                    # check if arguments are needed
                    # if len(Gui.cmd.args) != 0:
                    # args needed -> ask
                    args_menu = ArgslistMenu(self)
                    curses.endwin()
                    curses.echo()
                    wrapper(args_menu.run)
                    break
            elif c == curses.KEY_F10 or c == 27:
                Gui.cmd = None
                break  # Exit the while loop
            elif c == 339 or c == curses.KEY_PPAGE:
                # Page UP
                self.move_page(-1)
            elif c == 338 or c == curses.KEY_NPAGE:
                # Page DOWN
                self.move_page(1)
            elif c == curses.KEY_UP:
                # Move UP
                self.move_position(-1)
            elif c == curses.KEY_DOWN:
                # Move DOWN
                self.move_position(1)
            elif c == curses.KEY_BACKSPACE or c == 127:
                if self.check_move_cursor(-1):
                    i = self.xcursor - self.x_init - 1
                    self.input_buffer = self.input_buffer[:i] + self.input_buffer[i + 1:]
                    self.xcursor -= 1
                    # new search -> reset position
                    self.position = 0
                    self.page_position = 0
            elif c == curses.KEY_DC or c == 127:
                if self.check_move_cursor(1):
                    i = self.xcursor - self.x_init - 1
                    self.input_buffer = self.input_buffer[:i + 1] + self.input_buffer[i + 2:]
                    # new search -> reset position
                    self.position = 0
                    self.page_position = 0
            elif c == curses.KEY_LEFT:
                # Move cursor LEFT
                if self.check_move_cursor(-1): self.xcursor -= 1
            elif c == curses.KEY_RIGHT:
                # Move cursor RIGHT
                if self.check_move_cursor(1): self.xcursor += 1
            elif c == curses.KEY_BEG or c == curses.KEY_HOME:
                # Move cursor to the BEGIN
                self.xcursor = self.x_init
            elif c == curses.KEY_END:
                # Move cursor to the END
                self.xcursor = self.x_init + len(self.input_buffer)
            elif c == 9:
                # TAB cmd auto complete
                if self.input_buffer != "":
                    predictions = []
                    for cheat in self.cheats:
                        if cheat.command.startswith(self.input_buffer):
                            predictions.append(cheat.command)
                    if len(predictions) != 0:
                        self.input_buffer = commonprefix(predictions)
                        self.xcursor = self.x_init + len(self.input_buffer)
                        self.position = 0
                        self.page_position = 0
            elif 20 <= c < 127:
                i = self.xcursor - self.x_init
                self.input_buffer = self.input_buffer[:i] + chr(c) + self.input_buffer[i:]
                self.xcursor += 1
                # new search -> reset position
                self.position = 0
                self.page_position = 0
        curses.endwin()


class ArgslistMenu:
    current_arg = 0
    max_preview_size = 0
    prev_lastline_len = 0

    # init arg box margins
    AB_TOP = 0
    AB_SIDE = 0

    xcursor = None
    x_init = None
    y_init = None

    def __init__(self, prev):
        self.previous_menu = prev

    def get_nb_preview_new_lines(self):
        """
        Returns the number of preview lines
        :return:
        """
        next_arg = 0
        nblines = 0
        multiline = '\n' in Gui.cmd.cmdline
        firstline = True
        # in case of multiline cmd process each line separately
        # for each line we have to count each char and deduce the
        # number of lines needed to print it
        for line in Gui.cmd.cmdline.split('\n'):
            parts = Gui.cmd.get_command_parts()
            nb_args_todo = len(parts) - 1
            nbchar = 0

            # for all lines except the first one we have ' >' in addition
            if multiline and (not firstline):
                nbchar = 2
            else:
                firstline = False

            # extract len of args in the current line
            i = 0
            for arg_name, arg_val in Gui.cmd.args:
                if i == next_arg and nb_args_todo > 0:
                    if arg_val != "":
                        # use value len if not empty
                        nbchar += len(arg_val)
                    else:
                        # else use name len + 2 for '<' and '>'
                        nbchar += (len(arg_name) + 2)
                    next_arg += 1
                    nb_args_todo -= 1
                i += 1

            # len of the cmd body
            for p in parts:
                nbchar += len(p)

            nblines += 1 + ((nbchar - 1) // self.max_preview_size)

        return nblines - 1

    def next_arg(self):
        """
        Select the next argument in the list
        """
        # reset cursor position
        self.xcursor = None
        self.x_init = None
        self.y_init = None
        # change selected arg
        if self.current_arg < Gui.cmd.nb_args - 1:
            self.current_arg += 1
        else:
            self.current_arg = 0

    def previous_arg(self):
        """
        Select the previous argument in the list
        """
        # reset cursor position
        self.xcursor = None
        self.x_init = None
        self.y_init = None
        # change selected arg
        if self.current_arg > 0:
            self.current_arg -= 1
        else:
            self.current_arg = Gui.cmd.nb_args - 1

    def draw_preview_part(self, win, text, color):
        """
        Print a part of the preview cmd line
        And start a new line if the last line of the preview is too long
        :param win: window
        :param text: part of the preview to draw
        :param color: color used to draw the text
        """
        for c in text:
            if c == "\n":
                # multi line cmd -> new line
                self.prev_lastline_len = 2
                win.addstr("\n    > ", color)
            elif self.prev_lastline_len < self.max_preview_size:
                # size ok -> print the char
                self.prev_lastline_len += 1
                win.addstr(c, color)
            else:
                # last line too long -> new line
                self.prev_lastline_len = 1
                win.addstr("\n    " + c, color)


    def draw_selected_arg(self, y_pos):
        """
        Draw the selected argument line in the argument menu
        """
        y, x = self.AB_TOP + y_pos + self.current_arg, self.AB_SIDE + 1
        ncols, nlines = self.width - 2 * (self.AB_SIDE + 1), 1
        arg = Gui.cmd.args[self.current_arg]
        max_size = self.max_preview_size - 4 - len(arg[0])
        selectedargline = curses.newwin(nlines, ncols, y, x)
        selectedargline.addstr("   > ", curses.color_pair(Gui.BASIC_COLOR))
        selectedargline.addstr(arg[0], curses.color_pair(Gui.ARG_NAME_COLOR))
        selectedargline.addstr(" = " + Gui.draw_string(arg[1], max_size), curses.color_pair(Gui.BASIC_COLOR))
        selectedargline.refresh()

    def draw_args_list(self, y_pos):
        """
        Draw the asked arguments list in the argument menu
        """
        y, x = self.AB_TOP + y_pos, self.AB_SIDE + 1
        ncols, nlines = self.width - 2 * (self.AB_SIDE + 1), Gui.cmd.nb_args + 1
        argwin = curses.newwin(nlines, ncols, y, x)
        for arg in Gui.cmd.args:
            max_size = self.max_preview_size + 4
            argline = Gui.draw_string("     {} = {}".format(*arg), max_size) + "\n"
            argwin.addstr(argline, curses.color_pair(Gui.BASIC_COLOR))
        argwin.refresh()

    def draw_desc_preview(self, argprev, p_x, p_y, description_lines):
        """
        Draw the descriptions_line preview in the preview windows (argprev)
        """
        # draw description
        if len(description_lines) > 0:
            argprev.addstr(p_y, p_x, "-----", curses.color_pair(Gui.BASIC_COLOR))
            p_y += 1
            for description_line in description_lines:
                argprev.addstr(p_y, p_x, description_line, curses.color_pair(Gui.BASIC_COLOR))
                p_y += 1
            p_y += 1
            argprev.refresh()
        return p_y

    def draw_cmd_preview(self, argprev, p_x, p_y=1):
        """
        Draw the cmd preview in the argument menu
        Also used to draw the borders of this menu
        """
        cmdparts = Gui.cmd.get_command_parts()

        # draw command
        argprev.addstr(p_y, p_x, "$ ", curses.color_pair(Gui.BASIC_COLOR))

        # draw preview cmdline
        for i in range(len(cmdparts) + Gui.cmd.nb_args):
            if i % 2 == 0:
                # draw cmd parts in white
                self.draw_preview_part(argprev, cmdparts[i // 2], curses.color_pair(Gui.BASIC_COLOR))
            else:
                # get argument value
                if Gui.cmd.args[(i - 1) // 2][1] == "":
                    # if arg empty use its name
                    arg = '<' + Gui.cmd.args[(i - 1) // 2][0] + '>'
                else:
                    # else its value
                    arg = Gui.cmd.args[(i - 1) // 2][1]

                # draw argument
                if (i - 1) // 2 == self.current_arg:
                    # if arg is selected print in blue
                    self.draw_preview_part(argprev, arg, curses.color_pair(Gui.ARG_NAME_COLOR))
                else:
                    # else in white
                    self.draw_preview_part(argprev, arg, curses.color_pair(Gui.BASIC_COLOR))
        argprev.border()
        argprev.refresh()

    def draw(self, stdscr):
        """
        Draw the arguments menu to ask them
        :param stdscr: screen
        """
        # init vars and set margins values
        self.height, self.width = stdscr.getmaxyx()
        self.AB_SIDE = 5
        padding_text_border = 3
        self.max_preview_size = self.width - (2 * self.AB_SIDE) - (2 * padding_text_border)

        # draw background cheatslist menu (clean resize)
        self.previous_menu.draw(stdscr)

        # draw argslist menu popup
        self.prev_lastline_len = 0
        nbpreviewnewlines = self.get_nb_preview_new_lines()
        # if Gui.cmd.nb_args != 0:
        #     nbpreviewnewlines = self.get_nb_preview_new_lines()
        # else:
        #     nbpreviewnewlines = 0

        # -------------- border
        # cmd
        # nbpreviewnewlines
        # .............. args margin top
        # args
        # ------
        # description
        # .............  description margin
        # ---------- border

        # width - preview
        ncols = self.width - 2 * self.AB_SIDE

        # prepare showed description
        description_lines = Gui.cmd.get_description_cut_by_size(ncols - (padding_text_border * 2))

        border_height = 1
        cmd_height = 1 + nbpreviewnewlines
        args_height = (2 + Gui.cmd.nb_args) if (Gui.cmd.nb_args > 0) else 0
        desc_height = (len(description_lines) + 1 + 1) if (len(description_lines) > 0) else 0

        cmd_pos = 1
        args_pos = border_height + cmd_height + 1
        desc_pos = args_pos + args_height - 1

        nlines = border_height * 2 + cmd_height + args_height + desc_height
        if nlines > self.height:
            nlines = self.height

        self.AB_TOP = (self.height - nlines) // 2
        y, x = self.AB_TOP, self.AB_SIDE

        try:
            argprev = curses.newwin(nlines, ncols, y, x)

            # draw command
            self.draw_cmd_preview(argprev, padding_text_border, cmd_pos)

            # draw description
            self.draw_desc_preview(argprev, padding_text_border, desc_pos, description_lines)

            if len(Gui.cmd.args) > 0:
                self.draw_args_list(args_pos)
                self.draw_selected_arg(args_pos)
                # init cursor position (if first draw)
                if self.x_init is None or self.y_init is None or self.xcursor is None:
                    self.y_init, self.x_init = curses.getsyx()
                    # prefill compatibility
                    self.x_init -= len(Gui.cmd.args[self.current_arg][1])
                    self.xcursor = self.x_init + len(Gui.cmd.args[self.current_arg][1])
                # set cursor position
                curses.setsyx(self.y_init, self.xcursor)
                curses.doupdate()
        except curses.error:
            # catch all curses error to not end with an exception in case of size error
            pass

    def check_move_cursor(self, n):
        if Gui.cmd.nb_args == 0:
            return False
        return self.x_init <= (self.xcursor + n) < self.x_init + len(Gui.cmd.args[self.current_arg][1]) + 1

    def autocomplete_arg(self):
        """
        Autocomplete the current argument
        """
        # current argument value
        argument = Gui.cmd.args[self.current_arg][1]
        # look for all files that match the argument in the working directory
        matches = glob.glob('{}*'.format(argument))

        if not matches:
            return False

        # init the autocompleted argument
        autocompleted_argument = ""
        # autocompleted argument is the longest start common string in all matches
        for i in range(len(min(matches))):
            if not all(min(matches)[:i + 1] == match[:i + 1] for match in matches):
                break
            autocompleted_argument = min(matches)[:i + 1]
        
        # add a "/" at the end of the autocompleted argument if it is a directory
        if isdir(autocompleted_argument) and autocompleted_argument[-1] != sep:
            autocompleted_argument = autocompleted_argument + sep

        # autocomplete the argument 
        Gui.cmd.args[self.current_arg][1] = autocompleted_argument
        # update cursor position
        self.xcursor = self.x_init + len(autocompleted_argument)

    def run(self, stdscr):
        """
        Arguments selection menu processing..
        :param stdscr: screen
        """
        # init
        Gui.init_colors()
        while True:
            self.draw(stdscr)
            c = stdscr.getch()
            if c == curses.KEY_ENTER or c == 10 or c == 13:
                # try to build the cmd
                # if cmd build is ok -> exit
                # else continue in args menu
                if Gui.cmd.build():
                    break
            elif c == curses.KEY_F10 or c == 27:
                # exit args_menu -> return to cheatslist_menu
                curses.endwin()
                wrapper(self.previous_menu.run)
                break
            elif c == curses.KEY_DOWN:
                self.next_arg()
            elif c == curses.KEY_UP:
                self.previous_arg()
            elif c == 9:
                if Gui.cmd.args:
                    # autocomplete the current argument
                    if Gui.cmd.args[self.current_arg][1]:
                        self.autocomplete_arg()
                    # go to the next argument
                    else:
                        self.next_arg()
            elif c == curses.KEY_BACKSPACE or c == 127:
                if self.check_move_cursor(-1):
                    i = self.xcursor - self.x_init - 1
                    Gui.cmd.args[self.current_arg][1] = Gui.cmd.args[self.current_arg][1][:i] + \
                                                        Gui.cmd.args[self.current_arg][1][i + 1:]
                    self.xcursor -= 1
            elif c == curses.KEY_DC or c == 127:
                # DELETE key
                if self.check_move_cursor(1):
                    i = self.xcursor - self.x_init - 1
                    Gui.cmd.args[self.current_arg][1] = Gui.cmd.args[self.current_arg][1][:i + 1] + \
                                                        Gui.cmd.args[self.current_arg][1][i + 2:]
            elif c == curses.KEY_LEFT:
                # Move cursor LEFT
                if self.check_move_cursor(-1): self.xcursor -= 1
            elif c == curses.KEY_RIGHT:
                # Move cursor RIGHT
                if self.check_move_cursor(1): self.xcursor += 1
            elif c == curses.KEY_BEG or c == curses.KEY_HOME:
                # Move cursor to the BEGIN
                self.xcursor = self.x_init
            elif c == curses.KEY_END:
                # Move cursor to the END
                self.xcursor = self.x_init + len(Gui.cmd.args[self.current_arg][1])
            elif 20 <= c < 127 and Gui.cmd.nb_args > 0:
                i = self.xcursor - self.x_init
                Gui.cmd.args[self.current_arg][1] = Gui.cmd.args[self.current_arg][1][:i] + chr(c) + \
                                                    Gui.cmd.args[self.current_arg][1][i:]
                self.xcursor += 1


class Gui:
    # result CMD
    cmd = None
    arsenalGlobalVars = {}
    savefile = config.savevarfile
    # colors
    BASIC_COLOR = 0  # output std
    COL1_COLOR = 7
    COL2_COLOR = 4 # gold
    COL3_COLOR = 14  # purple light 
    COL4_COLOR = 5  # 26  # violet clair: 14  # 4 yellow  # 6 purple # 7 cyan # 9 dark grey
    COL5_COLOR = 5 # blue
    COL1_COLOR_SELECT = 256  # output std invert
    COL2_COLOR_SELECT = 256
    COL3_COLOR_SELECT = 256
    COL4_COLOR_SELECT = 256
    CURSOR_COLOR_SELECT = 266  # background red
    PROMPT_COLOR = 0
    INFO_NAME_COLOR = 4 # 5
    INFO_DESC_COLOR = 0
    INFO_CMD_COLOR = 0
    ARG_NAME_COLOR = 5
    loaded_menu = False

    def __init__(self):
        self.cheats_menu = None

    @staticmethod
    def init_colors():
        """ Init curses colors """
        curses.start_color()
        curses.use_default_colors()
        for i in range(0, 255):
            curses.init_pair(i + 1, i, -1)

    @staticmethod
    def draw_string(str_value, max_size):
        """
        Return a string of the max size, ended with ... if >= max_size
        :param str_value:
        :param max_size:
        :return:
        """
        result_string = str_value
        if len(str_value) >= max_size:
            result_string = str_value[:max_size - 4] + '...'
        return result_string

    def run(self, cheatsheets):
        """
        Gui entry point
        :param cheatsheets: cheatsheets dictionary
        """
        if self.cheats_menu is None:
            # Load cheatList if not already done
            self.cheats_menu = CheatslistMenu()
            for value in cheatsheets.values():
                self.cheats_menu.globalcheats.append(value)

        # if global var save exists load it
        if exists(Gui.savefile):
            with open(Gui.savefile, 'r') as f:
                Gui.arsenalGlobalVars = json.load(f)

        wrapper(self.cheats_menu.run)
        return Gui.cmd
