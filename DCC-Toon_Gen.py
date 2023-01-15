#!/usr/bin/env python3

# Python Module Imports


# DCC Module Imports
import adventurers

# Entry Text
"""
You’re no hero.

You’re an adventurer:
a reaver,
a cutpurse,
a heathen-slayer,
a tight-lipped warlock guarding long-dead secrets.

You seek gold and glory,
winning it with sword and spell,
caked in the blood and filth of the weak, the dark, the demons, and the vanquished.

There are treasures to be won deep underneath,
and you shall have them...
"""

# Functions
def clear():
    """Clears the terminal window, cross-platform compatable"""
    print("\033c", end="")


def main_Menu():
    player = adventurers.Adventurer()
    player.level_Zero()
    player.statBlock()

if __name__ == "__main__":
    main_Menu()