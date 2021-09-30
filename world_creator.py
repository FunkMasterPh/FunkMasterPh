from monster_class import Monster
from character_class import Character
from room_class import *
from goblin_class import *
from items_class import *
from potion import *
import time
import library
import random
import fight
import commands


"""**********Creating All Items**********"""



axe1 = weapons.Axe()
sword1 = weapons.Sword()
sword2 = weapons.Sword()
sword3 = weapons.Sword()
sword4 = weapons.Sword()
sword5 = weapons.Sword()
torch1 = misc.Torch()
axe2 = weapons.Axe()
helmet1 = Armor('helmet', 'head', 2)
chestplate1 = Armor('chestplate', 'chest', 3)

"""**********Creating Entities**********"""
goblin1 = Goblin([sword5])
goblin2 = Goblin([sword2])
goblin3 = Goblin([])
goblin4 = Goblin([sword4])
troll1 = Troll([])

player = Character("Aragorn", [axe1, torch1, chestplate1, helmet1])

"""**********World Creation**********"""

cave_1 = Room("It's the first cave.", [goblin1, troll1])
cave_2 = Room("It's the second cave.", [goblin2, sword3])
cave_3 = Room("It's the third cave.", [goblin3, axe2])
cave_4 = Room("It's the fourth cave.", [goblin4])

cave_1.setExitWest(cave_2)
cave_1.setExitNorth(cave_3)
cave_1.setExitEast(cave_4)

cave_2.setExitEast(cave_1)

cave_3.setExitSouth(cave_1)
cave_3.setDark(True)

cave_4.setExitWest(cave_1)








