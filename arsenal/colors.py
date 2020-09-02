import curses


def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, 255):
        curses.init_pair(i + 1, i, -1)
    # for i in range(0, 255):
    #     curses.init_pair(i + 1 + 255, i, curses.COLOR_WHITE)
    try:
        for i in range(0, 2000):
            stdscr.addstr('[' + str(i) + ']', curses.color_pair(i))
        # for i in range(0, 255):
        #     stdscr.addstr('[' + str(i + 255) + '] ', curses.color_pair(i + 255))
    except curses.ERR:
        # End of screen reached
        pass
    stdscr.getch()

curses.wrapper(main)
