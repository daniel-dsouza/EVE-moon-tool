import os
import sys
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "C:\\Users\\danie\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\danie\\Anaconda3\\tcl\\tk8.6"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name='moon-app',
    version='0.1',
    description='convert Moon analysis to a spreadsheet',

    options={
        'build_exe': {
            'packages': ['csv'],
            "include_files": ["tcl86t.dll", "tk86t.dll"],
        },
    },

    executables=[Executable('moon_app.py', base=base)],
)