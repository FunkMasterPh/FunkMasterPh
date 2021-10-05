from merchant_class import Merchant
from world_class import World
from monster_class import Monster
from character_class import Character
from room_class import *
from goblin_class import *
from items_class import *
from potion import *
import misc
import account_handler as acc
import time
import library
import random
import fight
import commands
import pickle


"""**********Creating All Items**********"""
potion1 = Flask(PotionType.HP, PotionSize.SMALL)
potion2 = Flask(PotionType.DEX, PotionSize.SMALL)
axe1 = weapons.Axe()
sword1 = weapons.Sword()
sword2 = weapons.Sword()
sword3 = weapons.Sword()

sword4 = weapons.Sword()
sword5 = weapons.Sword()
torch1 = misc.Torch()
torch2 = misc.Torch()
axe2 = weapons.Axe()
helmet1 = Armor('helmet', 'head', 2)
chestplate1 = Armor('chestplate', 'chest', 3)

"""**********Creating Objects**********"""
goblin1 = Goblin([])
goblin2 = Goblin([])
goblin3 = Goblin([])
goblin4 = Goblin([])
troll1 = Troll([])
troll2 = Troll([])

merchant = Merchant([sword5])

lock1 = misc.Lock(1)
chest1 = misc.Chest([sword1, axe1], lock1)
key1 = misc.Key(1, "A small key.")

"""**********World Creation**********"""

try:
    with open(f'{acc.player._name.lower()}/{acc.player._name.lower()}_caves.P', 'rb') as f:
        caves = pickle.load(f)
        cave_1, cave_2, cave_3, cave_4, cave_5 = caves

except:
    cave_1 = Room("It's the first cave.", [goblin1, troll1, potion1, potion2, torch1, key1])
    cave_2 = Room("It's the second cave.", [chest1])
    cave_3 = Room("It's the third cave.", [goblin3])
    cave_4 = Room("It's the fourth cave.", [goblin4, troll2])
    cave_5 = Room("Its the merchant and his shop!", [merchant])
    caves = [cave_1, cave_2, cave_3, cave_4, cave_5]


cave_1.setExitWest(cave_2)
cave_1.setExitNorth(cave_3)
cave_1.setExitEast(cave_4)
cave_1.setExitSouth(cave_5)

cave_2.setExitEast(cave_1)

cave_3.setExitSouth(cave_1)
cave_3.setDark(True)

cave_4.setExitWest(cave_1)

cave_5.setExitNorth(cave_1)
