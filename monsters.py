#!/usr/bin/env python3

# Python module import
import pandas
import sys

# DCC-text module import
import mechanics

class Monster:
    def __init__(self, name) -> None:
        """Creates a monster using the monsters excel file."""
        sheet = pandas.read_excel('data//monsters.xlsx', header=0, index_col=0)
        self.Name = name
        self.Init = sheet.loc[name, "Init"]
        self.Atk = sheet.loc[name, "Atk"]
        self.AC = sheet.loc[name, "AC"]
        self.HD = sheet.loc[name, "HD"]
        self.HP = mechanics.dice_Roller(self.HD)
        self.MV = sheet.loc[name, "MV"]
        self.AD = sheet.loc[name, "AD"]
        self.SP = sheet.loc[name, "SP"]
        self.SV = sheet.loc[name, "SV"]
        self.AL = sheet.loc[name, "AL"]
    
    def statBlock(self):
        """Prints out a stack block of (the Monster."""
        print(f"""
        Name: {self.Name}
        Initiative: {self.Init}
        Attacks: {self.Atk}
        Armor Class: {self.AC}
        HP: {self.HP} ({self.HD})
        Movement: {self.MV}
        Action Dice: {self.AD}
        Special Powers: {self.SP}
        Saving Values: {self.SV}
        Alignment: {self.AL}
        """)    

# Message if run directly
if __name__ == "__main__":
    print("This file contains Monster functions.")
    sys.exit()