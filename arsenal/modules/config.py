import os
from os.path import dirname, abspath, expanduser, join

# Base paths
BASEPATH = dirname(dirname(dirname(abspath(__file__))))
HOMEPATH = expanduser("~")
FORMATS = ["md", "rst"]
EXCLUDE_LIST = ["README.md", "README.rst", "index.rst"]

CHEATS_PATHS = [
    join(BASEPATH, "cheats"),  # DEFAULT
    # Additional paths below, add comma to line above
    join(BASEPATH, "my_cheats"),
    join(HOMEPATH, ".cheats")
]

messages_error_missing_arguments = 'Error missing arguments'

# set lower delay to use ESC key (in ms)
os.environ.setdefault('ESCDELAY', '25')

savevarfile = join(expanduser("~"), ".arsenal.json")
