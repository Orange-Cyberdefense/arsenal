import argparse
import sys
import json
import os
import arsenal.config as config
from arsenal.modules import cheat
from arsenal.modules import gui
import pyperclip
import fcntl
import termios
import re

class App:
    version = '1.0.0'

    def __init__(self):
        pass

    def get_args(self):
        examples = '''examples:
        arsenal
        arsenal --copy
        arsenal --print
        
        You can manage global variables with:
        ^set GLOBALVAR1=<value>
        ^show
        ^clear
        '''

        parser = argparse.ArgumentParser(
            prog="arsenal",
            description='arsenal v{} - Pentest command launcher'.format(self.version),
            epilog=examples,
            formatter_class=argparse.RawTextHelpFormatter
        )

        # group_auth = parser.add_argument_group('authentication')
        # group_auth.add_argument('-u', '--username', action='store', help='Username')
        # group_auth.add_argument('-p', '--password', action='store', help='Plaintext password')
        # group_auth.add_argument('-d', '--domain', default="", action='store', help='Domain name')
        # group_auth.add_argument('-H', '--hashes', action='store', help='[LM:]NT hash')
        # parser.add_argument('-v', action='count', default=0, help='Verbosity level (-v or -vv)')

        group_out = parser.add_argument_group('output [default = prefill]')
        group_out.add_argument('-p', '--print', action='store_true', help='Print the result')
        group_out.add_argument('-o', '--outfile', action='store', help='Output to file')
        group_out.add_argument('-c', '--copy', action='store_true', help='Output to clipboard')
        group_out.add_argument('--exec', action='store_true', help='Execute cmd')
        parser.add_argument('-V', '--version', action='version', version='%(prog)s (version {})'.format(self.version))

        # if len(sys.argv) == 1:
        #     parser.print_help()
        #     sys.exit(config.messages_error_missing_arguments)

        return parser.parse_args()

    def run(self):
        args = self.get_args()

        # load cheatsheets
        cheatsheets = cheat.Cheats().read_files(config.cheats_paths)
        
        while True:
            # launch gui
            cmd = gui.Gui().run(cheatsheets)

            if cmd == None:
                exit(0)

            # Internal CMD
            elif cmd.cmdline[0] == '>':
                if cmd.cmdline == ">exit":
                    break
                elif cmd.cmdline == ">show":
                    with open(config.savevarfile,'r') as f:
                        arsenalGlobalVars = json.load(f)
                        for k,v in arsenalGlobalVars.items():
                            print(k+"="+v)
                    break
                elif cmd.cmdline == ">clear":
                    with open(config.savevarfile,"w") as f:
                        f.write(json.dumps({}))
                    self.run()
                elif re.match("^\>set( [^= ]+=[^= ]+)+$", cmd.cmdline):
                    with open(config.savevarfile,'r') as f:
                        arsenalGlobalVars = json.load(f)
                    varlist = re.findall("([^= ]+)=([^= ]+)", cmd.cmdline)
                    for v in varlist:
                        arsenalGlobalVars[v[0]] = v[1]
                    with open(config.savevarfile,"w") as f:
                        f.write(json.dumps(arsenalGlobalVars))
                else :
                    print("Arsenal: invalid internal command..")
                    break

            # OPT: Copy CMD to clipboard
            elif args.copy:
                pyperclip.copy(cmd.cmdline)
                break

            # OPT: Only print CMD
            elif args.print:
                print(cmd.cmdline)
                break

            # OPT: Write in file
            elif args.outfile:
                with open(args.outfile,'w') as f:
                    f.write(cmd.cmdline)
                break

            # OPT: Exec
            elif args.exec:
                os.system(cmd.cmdline)
                break

            # DEFAULT: Prefill Shell CMD
            else:
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
                for c in cmd.cmdline:
                    fcntl.ioctl(stdin, termios.TIOCSTI, c)
                # restore TTY attribute for stdin
                termios.tcsetattr(stdin, termios.TCSADRAIN, oldattr)
                break

if __name__ == "__main__":
    try:
        App().run()
    except KeyboardInterrupt:
        exit(0)
