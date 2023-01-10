#!/usr/bin/env python3

#### Collection of utility commands for python program

import os
import sys

def change_Title(title):
    """Changes the title of the terminal window."""
    os.system("title " + title)

def clear():
    """Clears the terminal window, cross-platform compatable"""
    print("\033c", end="")

def restart():
    """Restarts the python file."""
    os.execv(sys.executable, ['python'] + sys.argv)