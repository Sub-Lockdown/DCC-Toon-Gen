#!/usr/bin/env python3

##### DCC RPG mechanic commands

# Importing Python modules
import random
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

def ability_Modifer(STAT, type='INT'):
    """Takes the ability score, and returns the modifier."""
    if type == 'INT':
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
    elif type == 'STR':
        if STAT == 3:
            return '-3'
        elif STAT in range(4,6):
            return '-2'
        elif STAT in range(6, 9):
            return '-1'
        elif STAT in range(9,13):
            return '0'
        elif STAT in range(13,16):
            return '+1'
        elif STAT in range(16, 18):
            return '+2'
        else:
            return '+3'

# Message if run directly
if __name__ == "__main__":
    print("This file contains the basic DCC mechanic functions")
    sys.exit()