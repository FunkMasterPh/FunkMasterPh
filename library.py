import time
from character_class import Character
from monster_class import Monster
import commands as cmd
from world_creator import *


def printInterface(currentRoom):
    print(currentRoom.getRoomDesc())
    for object in currentRoom.getObjects():
        print(f"A "+object.getType() +".")
    printVisibleExits(currentRoom)    


def parsePlayerCommand(playerCommand, currentRoom):

    command = playerCommand.strip().split()
    if command == []:
        return currentRoom
    elif command[0] not in cmd._PLAYER_COMMANDS:
        print("Command doesn't exist.")
    elif command[0] == cmd._HELP:
        cmd.displayHelpMenu()
    elif command[0] == cmd._ATTACK:
        if not cmd.attack(command[1], currentRoom):
            print("No such target.")
    elif command[0] == cmd._GO:
        newCurrentRoom = cmd.movePlayer(command[1], currentRoom)
        if newCurrentRoom != None:
            return newCurrentRoom
        else:
            return currentRoom
    elif command[0] == cmd._EXAMINE:
        print("Looking...")
        time.sleep(1)
        cmd.lookAt(command[1], currentRoom)
    elif command[0] == cmd._STATUS:
        hp = player.getHP()
        dex = player.getDex()
        stren = player.getStr()
        print(f"You have {hp} health and {dex} dexterity and {stren} strength")
    elif command[0] == cmd._WIELD_ITEM:
        if cmd.wieldWeapon(command[1]):
            print(f"You wielded {command[1]}.")
    elif command[0] == cmd._UNWIELD_ITEM:
        if cmd.unwieldWeapon(command[1]):
            print(f"You unwielded {command[1]}.")
        else:
            print("You're not wielding that item.")
    elif command[0] == cmd._TAKE_ITEM:
        if cmd.takeItem(command[1], currentRoom):
            print(f"You take {command[1]}.")
        else:
            print("You can't take that.")  
    elif command[0] == cmd._DROP_ITEM:
        if cmd.dropItem(command[1], currentRoom):
            print(f"You dropped {command[1]}.")       
        else:
            print("You don't have that item.")
    elif command[0] == cmd._INVENTORY:
        cmd.checkInventory()
    elif command[0] == cmd._LOOT:
        if cmd.loot(currentRoom):
            print("You loot the body.")
        else:
            print("Nothing to loot.")
    elif command[0] == cmd._LIGHT:
        if cmd.light(command[1]):
            print("You light the torch")
    elif command[0] == cmd._EXTINGUISH:
        if cmd.extinguish():
            print("You put out the torch.")
        


    return currentRoom


def printVisibleExits(currentRoom):
    roomExits = []
    print("Visible exits: ", end='')
    if currentRoom.getExitWest():
        roomExits.append("West")   
    if currentRoom.getExitEast():
        roomExits.append("East")     
    if currentRoom.getExitNorth():
        roomExits.append("North")
    if currentRoom.getExitSouth():
        roomExits.append("South")
    print(str(roomExits).replace('[', '').replace(']', ''))

