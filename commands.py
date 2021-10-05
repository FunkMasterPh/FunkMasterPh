import fight
import library
from world_creator import *
from character_class import Character
from merchant_class import Merchant
from account_handler import *

""" Contains commands available through the input loop. """

_HELP = "help"
_TAKE_ITEM = "take"
_DROP_ITEM = "drop"
_EQUIP_ITEM = "equip"
_UNEQUIP_ITEM = "unequip"
_INVENTORY = "inventory"
_LOOT = "loot"
_STATUS = "status"
_CONSUME_ITEM = "consume"
_EXAMINE = "examine"
_LIGHT = "light"
_EXTINGUISH = "extinguish"
_GO = "go"
_BUY = "buy"
_SELL = "sell"
_ATTACK = "attack"
_QUIT = "quit"
_SAVE = "save"
_OPEN = "open"

EQUIP = "equip"
UNEQUIP = "unequip"
TORCH = "torch"
POTION = "potion"
MONSTER = "monster"
ITEM = "item"
WEAPON = "weapon"
ARMOR = "armor"
MERCHANT = "merchant"
BUY = "buy"
SELL = "sell"
LIGHT = "light"
EXTINGUISH = "extinguish"


_PLAYER_COMMANDS = [
    _HELP,
    _TAKE_ITEM,
    _DROP_ITEM,
    _EQUIP_ITEM,
    _UNEQUIP_ITEM,
    _INVENTORY,
    _LOOT,
    _STATUS,
    _CONSUME_ITEM, 
    _EXAMINE,
    _LIGHT, 
    _EXTINGUISH, 
    _GO,
    _BUY,
    _SELL,
    _ATTACK, 
    _QUIT, 
    _SAVE,
    _OPEN
]   

def displayHelpMenu():
    """Displays available commands."""
    print(18 * "*", "AVAILABLE COMMANDS", 18 * "*")
    print("- HELP: Shows this menu.")
    print("- ATTACK <ENEMY>: Attack someone! Or something!")
    print("- STATUS: Display information about yourself.")
    print("- TAKE <ITEM>: Add an item to your inventory.")
    print("- DROP <ITEM>: Discard of an item in your inventory.")
    print("- EQUIP <ITEM>: Equip an item, such as a helmet or weapon.")
    print("- UNEQUIP <ITEM>: Remove an equipped item.")
    print("- INVENTORY: List all the items your are carrying.")
    print("- LOOT <TARGET>: Loot a slain enemy.")
    print("- CONSUME <ITEM>: Drink a potion, or eat a biscuit.")
    print("- EXAMINE <ITEM>: Examine a thing or a room.")
    print("- LIGHT <ITEM>: Light a fire.")
    print("- EXTINGUISH <ITEM>: Put a fire out.")
    print("- GO <DIRECTION>: Go somewhere and do something.")
    print("- BUY <ITEM>: Buys an item from the shop.")
    print("- SELL <ITEM>: Sells an item to the shop.")
    print("- SAVE: Save your progress.")
    print("- QUIT: Leave the game, for some reason.")
    print(56 * "*")

def playerStatus():

    print(18 * "*", "THIS IS YOU", 18 * "*" )
    print(f"*\tPlayer Level: {player.getLevel()} \t XP: {player.getXP()}/{player.getLevel() * 200}")
    print(f"*\tPlayer Health: {player.getHP()} \t Armor: {player.getArmor()}")
    print(f"*\tStrength: {player.getStr()} \t\t Dexterity: {player.getDex()}")
    print(f"*\tCoins: {int(player.getCoin())}\t\t Weight: {player.getTotalWeight()}")
    print(f"*\tWielded: {player.getWielded()}\t\t Equipped: {player.isEquipped('chestplate')}")
    print(49 * "*")

    
def movePlayer(userMovement, currentRoom):
    """Checks if exit exists and moves the player if true."""
    if userMovement == "west":
        if currentRoom.getExitWest():
            return currentRoom.getExitWest()
        else: 
            print("I run into a wall.")
    elif userMovement == "east":
        if currentRoom.getExitEast():
            return currentRoom.getExitEast()
        else: 
            print("I run into a wall.")
    elif userMovement == "north":
        if currentRoom.getExitNorth():
            return currentRoom.getExitNorth()
        else: 
            print("I run into a wall.")
    elif userMovement == "south":
        if currentRoom.getExitSouth():
            return currentRoom.getExitSouth()
        else: 
            print("I run into a wall.")
    else:
        print("I can't go there.")


def attack(target, currentRoom):
    """Checks if target is in room and if true calls the letsFight() function."""
    if library.canPlayerSee(currentRoom):
        for item in currentRoom.getObjects():
            if item.getType().lower() == target.lower() and item.getObjectType() == MONSTER:
                fight.letsFight(player, item)
                return True
       
def consume(item_to_consume, item_number=None):
    """Checks what potion you want to drink and alters stats accordingly."""
    
    if item_number:
        try:
            item_number = int(item_number)
            potion_list = []
            for item in player.getInventory():
                if item.getItemType() == POTION and item_to_consume.lower() == POTION:
                    potion_list.append(item)
            if item_number > len(potion_list) or item_number == 0:
                return False
            else:
                potion_list[item_number-1].setPotionEffect(player)
            return True
        except ValueError:
            return False
    
    else:
        for item in player.getInventory():
            if item.getItemType() == POTION and item_to_consume.lower() == POTION:
                item.setPotionEffect(player)
            return True

    

def examineMonster(monster):
    """Prints the description and inventory of target monster."""
    print(monster.getDesc())
    print("It's carrying: ")
    for item in monster.getInventory():
        print(item.getType())

def examine(toLookAt, currentRoom):
    """takes user input and examines thing depending on input"""
    if toLookAt == "room":
        library.printInterface(currentRoom)
    
    else :
        for item in currentRoom.getObjects():
            if item.getType().lower() == toLookAt.lower():
                if item.getObjectType() == MONSTER:
                    examineMonster(item)
                elif item.getObjectType() in (ITEM, POTION):
                    print(item.getDesc())
                elif item.getObjectType() == MERCHANT:
                    print("He has these items for sale: ")
                    for thing in item.getInventory():
                        print(f"{thing.getType().title()} for {int(thing.getValue() * 1.2)} coins.")

        for item in player.getInventory():
            if item.getType().lower() == toLookAt.lower():
                if item.getObjectType() == MONSTER:
                    examineMonster(item)
                elif item.getObjectType() in (ITEM, POTION):
                    print(item.getDesc())       

def manageGear(command, item):
    """Checks if you have the equipment in inventory and if it is a piece of equipment. 
        If all is true changes equipment status accordingly."""
    for thing in player.getInventory():
        if thing.getType().lower() == item.lower() and thing.getItemType() == WEAPON:
            if command == EQUIP and not player.getWielded():
                player.setWielded(thing)
                return True
            elif command == UNEQUIP and thing == player.getWielded():
                player.setUnwield(thing)
                return True
            else:
                print(f"I've already done that.")
                return False
        elif thing.getType().lower() == item.lower() and thing.getItemType() == ARMOR:
            if command == EQUIP and not player.isEquipped(item):
                player.setEquipArmor(item)
                player.setArmor(thing.getDamageMitigation())
                return True      
            elif command == UNEQUIP and player.isEquipped(item):
                player.setUnequipArmor(item)
                player.setArmor(-thing.getDamageMitigation())
                return True
            else:
                print("I've already done that.")
                return False
        else:
            print("I can't use that item like that.") 
            return False 
    else:
        print("I don't have that item.")   
        return False
   

def trade(arg, thing):
    """Trading items with the merchant!"""
    if arg.lower() == BUY:
        for item in merchant.getInventory():
            if item.getType().lower() == thing.lower() and player.getCoin() >= item.getValue():
                merchant.sell(item)
                merchant.setCoin(int(item.getValue() * 1.2))
                player.buy(item)
                player.setCoin(int(-item.getValue() * 1.2))
                player.getInventory().append(item)
                merchant.getInventory().remove(item)
                player.setTotalWeight(item.getWeight())
                print(f"You purchased {item.getType()} for {int(item.getValue() * 1.2)} coins.")
                return True
            else:
                print("The Merchant says: 'You can´t afford that.'")
                return False
        else:
            print("The Merchant says: 'I dont have that.'")
    elif arg.lower() == SELL:
        for item in player.getInventory():
            if item.getType().lower() == thing.lower() and merchant.getCoin() >= item.getValue():
                if item.getItemType() == WEAPON:
                    manageGear(UNEQUIP, thing)
                elif item.getItemType() == ARMOR:
                    manageGear(UNEQUIP, thing)
                player.sell(item)
                player.setCoin(int(item.getValue() * 0.8))
                merchant.buy(item)
                merchant.setCoin(int(-item.getValue() * 0.8))
                player.setTotalWeight(-item.getWeight())
                print(f"You sold {item.getType()} for {int(item.getValue() * 0.8)} coins.")
                return True
            else:
                print("The Merchant says: 'I can't afford to buy that item from you, sorry!'")
                return False
        else:
            print("The Merchant says: 'You can't sell stuff you dont have!'")
            return False
    else:
        print("The Merchant says: 'Can't do that, sorry!'")


def takeItem(item_to_take, currentRoom):
    """If item in room inventory, remove from room and add to player inventory."""
    for item in currentRoom.getObjects():
        if item.getObjectType() in (ITEM, POTION):
            if item.getType().lower() == item_to_take.lower() and library.checkWeight(item):
                currentRoom.getObjects().remove(item)
                player.getInventory().append(item)
                player.setTotalWeight(item.getWeight())
                return True
            

def dropItem(item_to_drop, currentRoom):
    """If item's in inventory, remove from inventory and add it to room inventory."""
    for item in player.getInventory():
        if item.getType().lower() == item_to_drop.lower():
            if item == player.getWielded():
                manageGear(UNEQUIP,item_to_drop)
            elif player.isEquipped(item_to_drop):
                manageGear(UNEQUIP, item_to_drop)
            elif item_to_drop == TORCH:
                item.setOnOff(False)
                player.setIlluminated(False)
            currentRoom.getObjects().append(item)
            player.getInventory().remove(item)
            player.setTotalWeight(-item.getWeight())
            return True


def checkInventory():
    """Prints player inventory."""
    print("You're carrying the following items:")
    for item in player.getInventory():
        print(item.getType().title())



def loot(currentRoom, itemToLoot):
    """Checks if monsters are dead and adds their inventory to player inventory."""
    for item in currentRoom.getObjects():
        if item.getObjectType() == MONSTER and item.getIsAlive() == False and item.getInventory():
            while item.getInventory():
                loot = item.getInventory().pop()
                player.getInventory().append(loot)
            return True


def lightExtinguish(command, item):
    """Checks if you have torch in inventory, lights it if true."""
    for thing in player.getInventory():
        if thing.getType().lower() == item.lower() and item.lower() == TORCH:
            if command == LIGHT:
                if thing.getOn() != True:
                    thing.setOnOff(True)
                    player.setIlluminated(True)
                    return True
                else:
                    print("The torch is already lit.")
                    return False
            elif command == EXTINGUISH and thing.getOn():
                thing.setOnOff(False)
                player.setIlluminated(False)
                return True
            
    else:
        print("I can't light that.")
            
#def open():
#    for item in player.getInventory():
#        if item.getDesc() == "key":
