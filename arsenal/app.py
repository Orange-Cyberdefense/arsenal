import argparse
import json
import os
import fcntl
import termios
import re
import time
from curses import wrapper

# arsenal
from . import __version__
from .modules import config
from .modules import cheat
from .modules import check
from .modules import gui as arsenal_gui


class PanePathAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not re.fullmatch("^[^:]+:[^:]+:[0-9]*", values):
            raise ValueError("Not a PANE_PATH")
        setattr(namespace, self.dest, values)

class App:
    
    tmux_server = None
    tmux_session = None

    def __init__(self):
        pass

    def get_args(self):
        examples = '''examples:
        arsenal
        arsenal --copy
        arsenal --print

        You can manage global variables with:
        >set GLOBALVAR1=<value>
        >show
        >clear

        (cmd starting with '>' are internals cmd)
        '''

        parser = argparse.ArgumentParser(
            prog="arsenal",
            description='arsenal v{} - Pentest command launcher'.format(__version__),
            epilog=examples,
            formatter_class=argparse.RawTextHelpFormatter
        )

        group_out = parser.add_argument_group('output [default = prefill]')
        group_out.add_argument('-p', '--print', action='store_true', help='Print the result')
        group_out.add_argument('-o', '--outfile', action='store', help='Output to file')
        group_out.add_argument('-x', '--copy', action='store_true', help='Output to clipboard')
        group_out.add_argument('-e', '--exec', action='store_true', help='Execute cmd')
        group_out.add_argument('-t', '--tmux', action='store_true', help='Send command to tmux panel')
        group_out.add_argument("-z", "--tmux-new", action=PanePathAction, metavar="PANE_PATH", 
            help="Send command to tmux pane", dest="tmux_new")
        group_out.add_argument('-c', '--check', action='store_true', help='Check the existing commands')
        group_out.add_argument('-f', '--prefix', action='store_true', help='command prefix')
        parser.add_argument('-V', '--version', action='version', version='%(prog)s (version {})'.format(__version__))

        return parser.parse_args()

    def run(self):
        args = self.get_args()
        if args.tmux_new:
            self.check_tmux(args)

        # load cheatsheets
        cheatsheets = cheat.Cheats().read_files(config.CHEATS_PATHS, config.FORMATS,
                                                config.EXCLUDE_LIST)

        if args.check:
            check.check(cheatsheets)
        else:
            self.start(args, cheatsheets)

    def start(self, args, cheatsheets):
        # create gui object
        gui = arsenal_gui.Gui()
        while True:
            # launch gui
            cmd = gui.run(cheatsheets, args.prefix)

            if cmd == None:
                exit(0)

            # Internal CMD
            elif cmd.cmdline[0] == '>':
                if cmd.cmdline == ">exit":
                    break
                elif cmd.cmdline == ">show":
                    if (os.path.exists(config.savevarfile)):
                        with open(config.savevarfile, 'r') as f:
                            arsenalGlobalVars = json.load(f)
                            for k, v in arsenalGlobalVars.items():
                                print(k + "=" + v)
                    break
                elif cmd.cmdline == ">clear":
                    with open(config.savevarfile, "w") as f:
                        f.write(json.dumps({}))
                    self.run()
                elif re.match(r"^\>set( [^= ]+=[^= ]+)+$", cmd.cmdline):
                    # Load previous global var
                    if (os.path.exists(config.savevarfile)):
                        with open(config.savevarfile, 'r') as f:
                            arsenalGlobalVars = json.load(f)
                    else:
                        arsenalGlobalVars = {}
                    # Add new glovar var
                    varlist = re.findall("([^= ]+)=([^= ]+)", cmd.cmdline)
                    for v in varlist:
                        arsenalGlobalVars[v[0]] = v[1]
                    with open(config.savevarfile, "w") as f:
                        f.write(json.dumps(arsenalGlobalVars))
                else:
                    print("Arsenal: invalid internal command..")
                    break

            # OPT: Copy CMD to clipboard
            elif args.copy:
                try:
                    import pyperclip
                    pyperclip.copy(cmd.cmdline)
                except ImportError:
                    pass
                break

            # OPT: Only print CMD
            elif args.print:
                print(cmd.cmdline)
                break

            # OPT: Write in file
            elif args.outfile:
                with open(args.outfile, 'w') as f:
                    f.write(cmd.cmdline)
                break

            # OPT: Exec
            elif args.exec and not args.tmux:
                os.system(cmd.cmdline)
                break

            elif args.tmux:
                try:
                    import libtmux
                    try:
                        server = libtmux.Server()
                        session = server.list_sessions()[-1]
                        window = session.attached_window
                        panes = window.panes
                        if len(panes) == 1:
                            # split window to get more pane
                            pane = window.split_window(attach=False)
                            time.sleep(0.3)
                        else:
                            pane = panes[-1]
                        # send command to other pane and switch pane
                        if args.exec:
                            pane.send_keys(cmd.cmdline)
                        else:
                            pane.send_keys(cmd.cmdline, enter=False)
                            pane.select_pane()
                    except libtmux.exc.LibTmuxException:
                        self.prefil_shell_cmd(cmd)
                        break
                except ImportError:
                    self.prefil_shell_cmd(cmd)
                    break
            elif args.tmux_new:
                pane_path = args.tmux_new.split(":")
                new_window = False
                import libtmux
                try:
                    window = self.tmux_session.select_window(pane_path[1])
                except libtmux.exc.LibTmuxException:
                    window = self.tmux_session.new_window(attach=False, window_name=pane_path[1])
                    new_window = True
                if new_window:
                    pane = window.panes[0] 
                elif pane_path[2] == "": # all panes
                    pane = None
                elif int(pane_path[2]) > len(window.panes):
                    pane = window.split_window(attach=False)
                    time.sleep(0.3)
                else:
                    pane = window.panes[int(pane_path[2])]
                if pane:
                    if args.exec:
                        pane.send_keys(cmd.cmdline)
                    else:
                        pane.send_keys(cmd.cmdline, enter=False)
                        pane.select_pane()
                else:
                    for pane in window.panes:
                        if args.exec:
                            pane.send_keys(cmd.cmdline)
                        else:
                            pane.send_keys(cmd.cmdline, enter=False)
                            pane.select_pane()
                break
            # DEFAULT: Prefill Shell CMD
            else:
                self.prefil_shell_cmd(cmd)
                break

    def prefil_shell_cmd(self, cmd):
        stdin = 0
        # save TTY attribute for stdin
        oldattr = termios.tcgetattr(stdin)
        # create new attributes to fake input
        newattr = termios.tcgetattr(stdin)
        # disable echo in stdin -> only inject cmd in stdin queue (with TIOCSTI)
        newattr[3] &= ~termios.ECHO
        # enable non canonical mode -> ignore special editing characters
        newattr[3] &= ~termios.ICANON
        # use the new attributes
        termios.tcsetattr(stdin, termios.TCSANOW, newattr)
        # write the selected command in stdin queue
        try:
            for c in cmd.cmdline:
                fcntl.ioctl(stdin, termios.TIOCSTI, c)
        except OSError:
            message = "========== OSError ============\n"
            message += "Arsenal needs TIOCSTI enable for running\n"
            message += "Please run the following commands as root to fix this issue on the current session :\n"
            message += "sysctl -w dev.tty.legacy_tiocsti=1\n"
            message += "If you want this workaround to survive a reboot,\n" 
            message += "add the following configuration to sysctl.conf file and reboot :\n"
            message += "echo \"dev.tty.legacy_tiocsti=1\" >> /etc/sysctl.conf\n"
            message += "More details about this bug here: https://github.com/Orange-Cyberdefense/arsenal/issues/77"
            print(message)
        # restore TTY attribute for stdin
        termios.tcsetattr(stdin, termios.TCSADRAIN, oldattr)

    def check_tmux(self, args):
        try:
            import libtmux
        except ImportError:
            raise RuntimeError("Could not load libtmux") from None
        pane_path = args.tmux_new.split(":")
        try:
            self.tmux_server = libtmux.Server()
            self.tmux_session = self.tmux_server.sessions.get(session_name=pane_path[0])
        except libtmux._internal.query_list.ObjectDoesNotExist:
            raise RuntimeError(f"Could not find session {pane_path[0]}") from None


def main():
    try:
        App().run()
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    wrapper(main()) 
