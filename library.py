import time, sys
from character_class import Character
from monster_class import Monster
import commands as cmd
from world_creator import *
from account_handler import *


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
        elif command[0] not in cmd._PLAYER_COMMANDS:
            print("Command doesn't exist.")
        elif command[0] == cmd._HELP:
            cmd.displayHelpMenu()
        elif command[0] == cmd._ATTACK:
            if not cmd.attack(command[1], currentRoom):
                print("Invalid target.")
        elif command[0] == cmd._GO:                                    
            newCurrentRoom = cmd.movePlayer(command[1], currentRoom)
            if newCurrentRoom != None:
                printInterface(newCurrentRoom)
                return newCurrentRoom
            else:
                return currentRoom

        elif command[0] == cmd._EXAMINE:
            if canPlayerSee(currentRoom):
                print("Looking...")
                time.sleep(1)
                cmd.examine(command[1], currentRoom)
            else:
                print("It´s too dark to see.")

        elif command[0] == cmd._STATUS:
            cmd.playerStatus()
            
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
            if cmd.loot(currentRoom, command[1]):
                print("You loot the body.")
            else:
                print("Nothing to loot.")

        elif command[0] == cmd._LIGHT:
            if cmd.light(command[1]):
                print("You light the torch.")

        elif command[0] == cmd._EXTINGUISH:
            if cmd.extinguish(command[1]):
                print("You put out the torch.")
            else:
                print("There is nothing to extinguish.")    
        elif command[0] == cmd._EQUIP_ITEM:
            if cmd.equip(command[1]):
                print(f"You equipped {command[1]}.")

        elif command[0] == cmd._UNEQUIP_ITEM:
            if cmd.unEquip(command[1]):
                print(f"You unequipped {command[1]}")
        
        elif command[0] == cmd._BUY:
            cmd.trade(command[0], command[1])
            
        elif command[0] == cmd._SELL:
            cmd.trade(command[0], command[1])

        elif command[0] == cmd._SAVE:
            if(savePlayer(player)):
                print("Saved game.")

        elif command[0] == cmd._QUIT:
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