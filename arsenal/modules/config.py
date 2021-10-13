import os
from os.path import dirname, abspath, expanduser, join

# Base paths
DATAPATH = join(dirname(dirname(abspath(__file__))),'data')
BASEPATH = dirname(dirname(dirname(abspath(__file__))))
HOMEPATH = expanduser("~")
FORMATS = ["md", "rst"]
EXCLUDE_LIST = ["README.md", "README.rst", "index.rst"]

CHEATS_PATHS = [
    join(DATAPATH, "cheats"),  # DEFAULT
    # Additional paths below, add comma to line above
    join(BASEPATH, "my_cheats"),
    join(HOMEPATH, ".cheats")
]

messages_error_missing_arguments = 'Error missing arguments'

# set lower delay to use ESC key (in ms)
os.environ.setdefault('ESCDELAY', '25')
os.environ['TERM'] = 'xterm-256color'

savevarfile = join(HOMEPATH, ".arsenal.json")
