#!/usr/bin/env python3

# Python module import
import os
import time

# DCC-text module import
import util

def entry_text():
    """Entrance crawl"""
    print("""
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
    """)
    time.sleep(10)
    util.clear()

def main_Menu():
    """"Currently only used as a start off point."""
    util.change_Title("DCC-text")
    print("(L)ist Characters")
    print("(E)xit")
    choice = input().upper()
    util.clear()
    if choice not in ["L", "E"]:
        print("Please make a valid selection")
    elif choice == "L":
        list_Characters()
    elif choice == "E":
        quit()

def list_Characters():
    """Lists the characters in toons directory."""
    path = os.getcwd() + "\\toons"
    if os.path.exists(path) is False:
        os.mkdir(path)
    list = []
    
    # dirs=directories
    for (file) in os.walk(path):
        for f in file:
            if '.json' in f:
                print(f)
    print("Listing")
    input()

if __name__ == "__main__":
    entry_text()
    while True:
        main_Menu()