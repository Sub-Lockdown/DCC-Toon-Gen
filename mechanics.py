#!/usr/bin/env python3

##### DCC RPG mechanic commands

# Importing Python modules
import random
import pandas
import sys

# Reference variables
dice = [3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 20, 24, 30]
ability_scores = ["Strength", "Agility", "Stamina", "Personality", "Intelligence", "Luck"]
money = ["gp", "sp", "cp"]
saving_throws = {"Fortitude" : "Stamina", "Reflex" : "Agility", "Willpower" : "Personality"}
xp_threshold = {0 : 0, 1 : 10, 2 : 50, 3 : 110, 4 : 190, 5 : 290, 6 : 410, 7 : 550, 8 : 710, 9 : 890, 10 : 1090}

def dice_Roller(ROLL, IMP=0):
    """Dice roller takes a dice pool; +, -, x modifiers; and improvements/reductions of the dice face"""
    # Return variable
    value = 0
    multiply = False
    # Checks if there is a modifier, and seperates it from the dice pool
    if any(i in ROLL for i in '+-x'):
        if any(i in ROLL for i in '+'):
            dice_pool, modifier = ROLL.split('+')
            value += int(modifier)
        elif any(i in ROLL for i in '-'):
            dice_pool, modifier = ROLL.split('-')
            value -= int(modifier)
        else:
            dice_pool, modifier = ROLL.split('x')
            multiply = True
    else:
        dice_pool = ROLL

    # Takes the current die from the pool, and improves / reduces the die by the modifier
    count, sides = dice_pool.split('d')
    if sides in dice:
        index = dice.index(int(sides)) + IMP
        if index <= 0:
            mod_die = dice[0]
        elif index >= len(dice):
            mod_die = dice[-1]
        else:
            mod_die = dice[index]
    else:
         mod_die = int(sides)

    # Rolls the dice pool and adds it to the modifier
    for i in range(int(count)):
        value += random.randint(1, mod_die)

    # Checks if the modifier was mulitplication, and multiplies the value if so
    if multiply:
        value = value * int(modifier)
    return value

def ability_Roller():
    """Rolls the abilities scores, in order, using a 3d6 pool."""
    rolled_stats = {}
    for ability in range(len(ability_scores)):
        rolled_stats.update({ability_scores[ability]: dice_Roller("3d6")})
    return rolled_stats

def ability_Modifer(STAT):
    """Takes the ability score, and returns the modifier."""
    if STAT == 3:
        return -3
    elif STAT in range(4,6):
        return -2
    elif STAT in range(6, 9):
        return -1
    elif STAT in range(9,13):
        return 0
    elif STAT in range(13,16):
        return 1
    elif STAT in range(16, 18):
        return 2
    else:
        return 3

def ability_Wizard_KNOWN(STAT):
    """Takes the INT ability score and returns how many Wizard spells known."""
    if STAT == 3:
        return "NOSPELL"
    elif STAT in range(4,6):
        return -2
    elif STAT in range(6, 8):
        return -1
    elif STAT in range(8,14):
        return 0
    elif STAT in range(14,17):
        return 1
    else:
        return 2

def ability_Max_SPELL(STAT):
    """Takes the ability score (INT or PER) and returns the max spell level."""
    if STAT == 3:
        return "NOSPELL"
    elif STAT in range(4,8):
        return 1
    elif STAT in range(8, 10):
        return 2
    elif STAT in range(10,12):
        return 3
    elif STAT in range(12,15):
        return 4
    else:
        return 5

def ability_Luck_SCORE():
    """Randomly assigns a Birth Augur, and returns the associated Lucky Roll."""
    sheet = pandas.read_excel('data//luck_score.xlsx', header=0, index_col=0)
    roll = dice_Roller("1d30")
    luck_score = [
        (sheet.loc[roll, "Birth Augur"]),
        (sheet.loc[roll, "Lucky Roll"])
    ]
    return luck_score

def currency(COIN):
    """Currently takes money and converts all of it to it's GP value."""
    count = int(COIN[:-3])
    piece = COIN[len(COIN) - 2:]
# create a new string of last N characters
    if piece == "cp":
        return (count/100)
    elif piece == "sp":
        return (count/10)
    else:
        return count

def zero_Equipment_ROLL():
    """Rolls on the equipment table for starter equipment piece."""
    sheet = pandas.read_excel((pandas.ExcelFile('data//items.xlsx')), 'equipments', header=0, index_col=0)
    item = sheet.loc[dice_Roller("1d24"), "Item"]
    return item

def occupation_Roll():
    """Rolls on the occupation table, and returns the name, trained weapon, and starting trade good."""
    sheet = pandas.read_excel('data//occupation.xlsx', header=0, index_col=0)
    roll = dice_Roller("1d100")
    occupation = [
        (sheet.loc[roll, "Occupation"]),
        (sheet.loc[roll, "Trained Weapon"]),
        (sheet.loc[roll, "Trade Goods"])
    ]
    return occupation

def saving_Throw_ROLL(throw, DC, class_mods, abilities, misc_mod=0):
    """Basic saving throw roll."""
    total = 0
    total += class_mods[throw]
    total += abilities[saving_throws[throw]]
    total += misc_mod
    total += dice_Roller("1d20")
    if total >= DC:
        return True
    else:
        return False
    
def level_Zero(NAME):
    """Creates a level 0 character."""
    abilities = ability_Roller()
    birth_augur, lucky_roll = ability_Luck_SCORE()
    hp = dice_Roller("1d4") + ability_Modifer(abilities["Stamina"])
    copper = dice_Roller("5d12")
    wealth = currency(f"{copper} cp")
    items = [zero_Equipment_ROLL()]
    occupation, weapon_training, trade_goods = occupation_Roll()
    print(f"""
        Name: {NAME}
        Ability Scores: {abilities})
        Birth Augur: {birth_augur} ({lucky_roll})
        HP: {hp}
        Wealth: {wealth}
        Items: {items}
        Occupation: {occupation}
        Weapon Training: {weapon_training}
        Trade Goods: {trade_goods}
        """)

def xp_Threshold_CHECK(LV, XP):
    """Checks if current XP total is above the threshold for the next level."""
    if XP >  xp_threshold[LV]:
        return True
    else:
        return False

# Message if run directly
if __name__ == "__main__":
    print("This file contains basic DCC functions")
    sys.exit()