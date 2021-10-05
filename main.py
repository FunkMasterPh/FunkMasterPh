from monster_class import Monster
from character_class import Character
from room_class import *
from goblin_class import *
from items_class import *
import threading
import library
import account_handler
from world_creator import *

currentRoom = cave_1
saver = threading.Thread(target=account_handler.autoSave, args=[caves])
saver.start()

def main_menu(currentRoom):
    while True:
        currentRoom = library.parsePlayerCommand(input("What do you want to do? > "), currentRoom)
 
if __name__ == '__main__':

    main_menu(currentRoom)

