#!/usr/bin/env python3

# Python module import
import pandas
import sys

# DCC-text module import
import mechanics

class Adventurer:
    def __init__(self) -> None:
        """Creates blank Adventurer."""
        self.abilities = {}
        for ability in mechanics.ability_scores:
            self.abilities[ability] = 0
        self.birth_augur = ""
        self.lucky_roll = ""
        self.init = 0
        self.HP = 0
        self.money = {}
        for coin in mechanics.money:
            self.money[coin] = 0
        self.items = {}
        self.occupation = ""
        self.weapon_training = []
        self.trade_goods = []
        self.SV = {}
        for save in mechanics.saving_throws:
            self.SV[save] = 0
        self.AC = 10
        self.speed = "30 ft"
        #self.SP = sheet.loc[name, "SP"]
        #self.SV = sheet.loc[name, "SV"]
        #self.AL = sheet.loc[name, "AL"]

    def level_Zero(self):
        """Creates a level 0 adventure randomly."""
        # Auto rolls ability scores in order, using a pool of 3d6
        for ability in range(len(mechanics.ability_scores)):
            self.abilities.update({mechanics.ability_scores[ability]: mechanics.dice_Roller("3d6")})
        
        # Auto rolls a Luck Score
        luck_db = pandas.read_excel('data//luck_score.xlsx', header=0, index_col=0)
        luck_roll = mechanics.dice_Roller("1d30")
        self.birth_augur = (luck_db.loc[luck_roll, "Birth Augur"])
        self.lucky_roll = (luck_db.loc[luck_roll, "Lucky Roll"])
        
        # Auto rolls starting HP and adds the Stamina modifier
        hp_roll = mechanics.dice_Roller("1d4")
        hp_stamina = mechanics.ability_Modifer(self.abilities["Stamina"])
        self.HP = hp_roll + hp_stamina
       
        # Auto rolls starting money
        copper_roll = mechanics.dice_Roller("5d12")
        self.money['cp'] = copper_roll
        
        # Auto rolls starting item
        item_db = pandas.read_excel((pandas.ExcelFile('data//items.xlsx')), 'equipments', header=0, index_col=0)
        item_roll = mechanics.dice_Roller("1d24")
        self.items = item_db.loc[item_roll, "Item"]

        # Auto rolls starting occupation
        occupation_db = pandas.read_excel('data//occupation.xlsx', header=0, index_col=0)
        occupation_roll = mechanics.dice_Roller("1d100")
        self.occupation = (occupation_db.loc[occupation_roll, "Occupation"])
        self.weapon_training = (occupation_db.loc[occupation_roll, "Trained Weapon"])
        self.trade_goods = (occupation_db.loc[occupation_roll, "Trade Goods"])

        # Uses ability scores to auto generate misc stats
        self.init += mechanics.ability_Modifer(self.abilities["Agility"])
        for save in self.SV:
            self.SV[save] = mechanics.ability_Modifer(self.abilities[mechanics.saving_throws[save]])
        self.AC += mechanics.ability_Modifer(self.abilities["Agility"])
        
    def statBlock(self):
        """Prints out a stack block of the Adventure."""
        print(f'Occupation: {self.occupation}')
        print('')
        for ability in self.abilities:
            ability_score = self.abilities[ability]
            ability_mod = mechanics.ability_Modifer(ability_score, type='STR')
            print(f'{ability}: {ability_score} ({ability_mod})')
        print('')
        print(f'HP: {self.HP}; AC: {self.AC}; Init: {self.init}')
        print(f'Weapon: {self.weapon_training}')
        print(f'Speed: {self.speed}; Fort: {self.SV["Fortitude"]}, Ref  {self.SV["Reflex"]}, Will {self.SV["Willpower"]}')
        print('')
        print(f'Birth Augur: {self.birth_augur}, {self.lucky_roll}')
        for coins in self.money:
            wealth = ''
            if self.money[coins] > 0:
                wealth = wealth + str(self.money[coins]) + coins + ' '
        print(f'Wealth: {wealth}')
        print(f'Items: {self.items}')
        print(f'Trade Goods: {self.trade_goods}')
        
    def xp_Threshold_CHECK(self):
        """Checks if current XP total is above the threshold for the next level."""
        if self.XP > mechanics.xp_threshold[self.LV]:
            # This is where to put the level up function directly, or at least call it
            return True
        else:
            return False

# Message if run directly
if __name__ == "__main__":
    print("This file contains Adventurers functions.")
    sys.exit()