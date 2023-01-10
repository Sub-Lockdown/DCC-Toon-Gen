#!/usr/bin/env python3

# Python module imports
import mechanics
import monsters


mechanics.level_Zero("Nobody")

creatures = []
creatures.append(monsters.Monster("Goblin"))
for i in creatures:
    i.statBlock()