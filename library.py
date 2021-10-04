import time, sys
from character_class import Character
from monster_class import Monster
import commands as cmd
from world_creator import *
from account_handler import *

ACTION = 0
TARGET = 1


"""function for printing information about the room the player is in"""
def printInterface(currentRoom):
    if not canPlayerSee(currentRoom):
        print("Its too dark to see.")
    else:
        print(currentRoom.getRoomDesc())
        for object in currentRoom.getObjects():
            print(f"A "+object.getType() +".")
        printVisibleExits(currentRoom)    

def canPlayerSee(currentRoom):
    """Checks if room is lit, returns desc if true. If room is not lit, checks if
       player has a lit torch in inventory. If so, displays the room's description.
       If all fails, room is too dark to see."""
    if currentRoom.getDark() and not player.getIlluminated():
        return False
    else:
        return True

def checkWeight(item):
    if (player.getTotalWeight() + item.getWeight()) <= (player.getStr() * 10):
        return True
    else:
        print("It's too heavy!")
        return False
        

#function for taking and handling user input
def parsePlayerCommand(playerCommand, currentRoom):
    try: 
        command = playerCommand.strip().split()
        if command == []:
            return currentRoom

        elif command[ACTION] not in cmd._PLAYER_COMMANDS:
            print("Command doesn't exist.")

        elif command[ACTION] == cmd._HELP:
            cmd.displayHelpMenu()

        elif command[ACTION] == cmd._ATTACK:
            if not cmd.attack(command[TARGET], currentRoom):
                print("Invalid target.")

        elif command[ACTION] == cmd._GO:                                    
            newCurrentRoom = cmd.movePlayer(command[TARGET], currentRoom)
            if newCurrentRoom != None:
                printInterface(newCurrentRoom)
                return newCurrentRoom
            else:
                return currentRoom

        elif command[ACTION] == cmd._EXAMINE:
            if canPlayerSee(currentRoom):
                print("Looking...")
                time.sleep(1)
                cmd.examine(command[TARGET], currentRoom)
            else:
                print("It´s too dark to see.")

        elif command[ACTION] == cmd._STATUS:
            cmd.playerStatus()
            
        elif command[ACTION] == cmd._WIELD_ITEM:
            if cmd.wieldWeapon(command[TARGET]):
                print(f"You wielded {command[TARGET]}.")

        elif command[ACTION] == cmd._UNWIELD_ITEM:
            if cmd.unwieldWeapon(command[TARGET]):
                print(f"You unwielded {command[TARGET]}.")
            else:
                print("You're not wielding that item.")

        elif command[ACTION] == cmd._TAKE_ITEM:
            if cmd.takeItem(command[TARGET], currentRoom):
                print(f"You take {command[TARGET]}.")
            else:
                print("You can't take that.")  

        elif command[ACTION] == cmd._DROP_ITEM:
            if cmd.dropItem(command[TARGET], currentRoom):
                print(f"You dropped {command[TARGET]}.")       
            else:
                print("You don't have that item.")

        elif command[ACTION] == cmd._INVENTORY:
            cmd.checkInventory()

        elif command[ACTION] == cmd._LOOT:
            if cmd.loot(currentRoom, command[TARGET]):
                print("You loot the body.")
            else:
                print("Nothing to loot.")

        elif command[ACTION] == cmd._LIGHT:
            if cmd.light(command[TARGET]):
                print("You light the torch.")

        elif command[ACTION] == cmd._EXTINGUISH:
            if cmd.extinguish(command[TARGET]):
                print("You put out the torch.")
            else:
                print("There is nothing to extinguish.")    

        elif command[ACTION] == cmd._EQUIP_ITEM:
            if cmd.equip(command[TARGET]):
                print(f"You equipped {command[TARGET]}.")

        elif command[ACTION] == cmd._UNEQUIP_ITEM:
            if cmd.unEquip(command[TARGET]):
                print(f"You unequipped {command[TARGET]}")

        elif command[ACTION] == cmd._CONSUME_ITEM:
            if cmd.consume(command[TARGET]):
                print("You feel refreshed.")
            else:
                print("Can't consume that!")
        
        elif command[ACTION] == cmd._BUY:
            cmd.trade(command[ACTION], command[TARGET])
            
        elif command[ACTION] == cmd._SELL:
            cmd.trade(command[ACTION], command[TARGET])

        elif command[ACTION] == cmd._SAVE:
            savePlayer(player)
            saveWorld(cave_1, cave_2, cave_3, cave_4, cave_5)
            print("Saved game.")

        elif command[ACTION] == cmd._QUIT:
            savePlayer(player)
            print("Leaving game.")
            sys.exit()
                
        return currentRoom
                
    except IndexError:
        print(f"{command[0].title()} what?")
        return currentRoom
        

#function for printing all visible exits in a room
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