from monster_class import Monster
from character_class import Character
from room_class import *
from goblin_class import *
from items_class import *
import time
import library
import random
import fight
import commands
from world_creator import *

currentRoom = cave_1

while True:
    currentRoom = library.parsePlayerCommand(input("What do you want to do? > "), currentRoom)
  