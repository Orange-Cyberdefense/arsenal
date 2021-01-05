import subprocess
import shlex
import os


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def check(cheatsheets):
    done = []
    interactive_shell = '/bin/zsh'  # used for alias
    skip = ['powershell.md', 'windows.md', 'laps.md', 'reverse.md']
    for cheat in cheatsheets.values():
        if os.path.basename(cheat.filename) not in skip:
            binary = cheat.printable_command.split(' ')[0]
            if binary not in done:
                done.append(binary)
                if '<' in binary or binary.startswith('>'):
                    continue
                if (len(binary) > 4 and binary[-4:] == '.exe') or 'powershell' in cheat.name:
                    # Windows cmd : skip
                    print('{}{:<6s} : {} (full command is : {} ){}'.format(bcolors.BLUE, '✗ SKIP', binary,
                                                                           cheat.printable_command, bcolors.ENDC))
                    continue
                try:
                    cmd = interactive_shell + ' -i -c "type %s"' % shlex.quote(binary)
                    output = subprocess.check_output(cmd, shell=True, executable='/bin/zsh').decode()
                    print(
                        '{}{:<6s} : {} ({}){}'.format(bcolors.GREEN, '✔ OK', binary, output.split('\n')[0],
                                                      bcolors.ENDC))
                except subprocess.CalledProcessError as e:
                    print('{}{:<6s} : {} (full command is : {} ){}'.format(bcolors.WARNING, '✗ KO', binary,
                                                                           cheat.printable_command, bcolors.ENDC))
