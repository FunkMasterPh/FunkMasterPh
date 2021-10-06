import fight
import library
from world_creator import *
from character_class import Character
from merchant_class import Merchant
from account_handler import *
import potion

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
_UNLOCK = "unlock"


EQUIP = "equip"
UNEQUIP = "unequip"
TORCH = "torch"
POTION = "potion"
MONSTER = "monster"
ITEM = "item"
WEAPON = "weapon"
ARMOR = "armor"
SHOP = "shop"
BUY = "buy"
SELL = "sell"
LIGHT = "light"
EXTINGUISH = "extinguish"
KEY = "key"
CHEST = "chest"
OPEN = "open"
UNLOCK = "unlock"


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
    _OPEN,
    _UNLOCK
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
    print("- UNLOCK: Use a key to unlock locks.")
    print("- OPEN: Open containers, such as chests.")
    print("- LOOT <TARGET>: Loot a slain enemy or a container.")
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
    if player.getWielded():
        print(f"*\tYou're wielding a {player.getWielded().getType()}\t\t") 
    if player.isEquipped("chestplate"):
        print(f"*\tYou're wearing a chestplate.")
    if player.isEquipped("helmet"):
        print(f"*\tYou're wearing a helmet.")   
    print(49 * "*")

    
def movePlayer(userMovement, currentRoom):
    """Checks if exit exists and moves the player if true."""
    if userMovement == "west":
        if currentRoom.getExitWest():
            return currentRoom.getExitWest()
        else: 
            print("You run into a wall.")
    elif userMovement == "east":
        if currentRoom.getExitEast():
            return currentRoom.getExitEast()
        else: 
            print("You run into a wall.")
    elif userMovement == "north":
        if currentRoom.getExitNorth():
            return currentRoom.getExitNorth()
        else: 
            print("You run into a wall.")
    elif userMovement == "south":
        if currentRoom.getExitSouth():
            return currentRoom.getExitSouth()
        else: 
            print("You run into a wall.")
    else:
        print("You can't go there.")


def attack(target, currentRoom):
    """Checks if target is in room and if true calls the letsFight() function."""
    if library.canPlayerSee(currentRoom):
        if findObjectInRoom(currentRoom, target):
            item = findObjectInRoom(currentRoom, target)
            if item.getObjectType() == MONSTER and item.getIsAlive():
                fight.letsFight(player, item)
                return True

       
def consume(item_to_consume, item_number=None):
    """Checks what potion you want to drink and alters stats accordingly."""

    if item_number:
        try:
            item_number = int(item_number)
            potion_list = []
            for item in player.getInventory():
                if item.getType() == POTION and item_to_consume.lower() == POTION:
                    potion_list.append(item)
            if item_number > len(potion_list) or item_number == 0:
                return False
            else:
                potion_list[item_number-1].setPotionEffect(player)
                player.getInventory().remove(potion_list[item_number-1])
                return True
        except ValueError:
            return False
    else:
        for item in player.getInventory():
            if item.getType() == POTION and item_to_consume.lower() == POTION:
                item.setPotionEffect(player)
                player.getInventory().remove(item)
                return True

    
def examineMonster(monster):
    """Prints the description and inventory of target monster."""
    print(monster.getDesc())
    if monster.getInventory():
        print("It's carrying:")
        printInventory(monster)


def examine(toLookAt, currentRoom):
    """takes user input and examines thing depending on input"""
    for item in currentRoom.getObjects():
        defineExamine(toLookAt, item)
    for item in player.getInventory():
        if item.getType() == toLookAt.lower():
            print(item.getDesc())
    
    if not findObjectInPlayer(player, toLookAt) and not findObjectInRoom(currentRoom, toLookAt):
        print("That doesn't exist.") 

def defineExamine(toLookAt, item):
    if item.getType() == toLookAt.lower():
        if item.getObjectType() == MONSTER:
            examineMonster(item)
        elif item.getObjectType() == ITEM:
            print(item.getDesc())
        elif item.getObjectType() == CHEST:
            print(item.getDesc())
            if item.getInventory() and item.getIsOpen():
                print("It contains:")
                printInventory(item)
        elif item.getObjectType() == SHOP:
            print("He has these items for sale: ")
            for thing in item.getInventory():
                print(f"{thing.getType().title()} for {int(thing.getValue() * 1.2)} coins.")
            


def manageGear(command, item):
    """Checks if you have the equipment in inventory and if it is a piece of equipment. 
        If all is true changes equipment status accordingly."""
    for thing in player.getInventory():
        if thing.getType().lower() == item.lower() and thing.getItemType() == WEAPON:
            if command == EQUIP and not player.getWielded():
                player.setWielded(thing)
                return True
            elif command == EQUIP and player.getWielded():
                print("You're already wielding a weapon.")
                return False
            elif command == UNEQUIP and thing == player.getWielded():
                player.setUnwield(thing)
                return True
            elif command == UNEQUIP and not player.getWielded():
                print("You're not wielding anything.") 
                return False
        elif thing.getType().lower() == item.lower() and thing.getItemType() == ARMOR:
            if command == EQUIP and not player.isEquipped(item):
                player.setEquipArmor(item)
                player.setArmor(thing.getDamageMitigation())
                return True
            elif command == EQUIP and player.isEquipped(item):
                print("You're already wearing that.")
                return False
            elif command == UNEQUIP and player.isEquipped(item):
                player.setUnequipArmor(item)
                player.setArmor(-thing.getDamageMitigation())
                return True
            else:
                print("You're not wearing that item.")
                return False
    else:
        print("I can't do that.")   
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
                player.setTotalWeight(item.getWeight())
                print(f"You purchased {item.getType()} for {int(item.getValue() * 1.2)} coins.")
                return True
            else:
                print("The Merchant says: 'You can´t purchase that.'")
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
        if item.getObjectType() == ITEM:
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


def lootCheck(currentRoom, target):
    """Checks if monsters are dead and adds their inventory to player inventory."""
    if findObjectInRoom(currentRoom, target):
        item = findObjectInRoom(currentRoom, target)
        if item.getObjectType() == MONSTER and item.getIsAlive() == False and item.getInventory():
            loot(item)
            return True
        elif item.getType() == CHEST and item.getIsOpen():
            loot(item)
            return True


def loot(item):
    while item.getInventory():
        loot = item.getInventory().pop()
        player.getInventory().append(loot)


def lightExtinguish(command, item):
    """Checks if you have torch in inventory, lights it if true."""
    if findObjectInPlayer(player, item) and findObjectInPlayer(player, item).getType() == TORCH:
        torch = findObjectInPlayer(player, item)
        if command == LIGHT and not torch.getOn():
            torch.setOnOff(True)
            player.setIlluminated(True)
            return True
        elif command == LIGHT and torch.getOn():
            return False
        elif command == EXTINGUISH and torch.getOn():
            torch.setOnOff(False)
            player.setIlluminated(False)
            return True
        elif command == EXTINGUISH and not torch.getOn():
            return False

            
def openContainer(currentRoom, item):
    for thing in currentRoom.getObjects():
        if thing.getType() == CHEST and item.lower() == CHEST and not thing.getIsOpen(): 
            if thing.getLock().getLocked():
                print(f"The {item.lower()} is locked.")
                return False
            elif not thing.getLock().getLocked():
                thing.setIsOpen(True)
                print(f"The {item.lower()} opens.")
                return True
        elif thing.getType() == CHEST and item.lower() == CHEST and thing.getIsOpen(): 
            print("It's already open.")
    else:
        print("You can't do that.")   
        return False


def unlock(currentRoom, item):
    if findObjectInRoom(currentRoom, item) and item == CHEST:
        if findObjectInPlayer(player, KEY):
            container = findObjectInRoom(currentRoom, item)
            return tryToUnlock(item, container)
        else:
            print("You don't have the matching key.")
    else:
        print("There is nothing to unlock.")

def tryToUnlock(item, container):
    if container.getType() == item.lower():
        if container.getLock().getID() == findObjectInPlayer(player, KEY).getID():
            container.getLock().setLocked(False)
            print("You unlocked the chest.")
        else:
            return False
    else:
        print("You can't unlock that.")


def findObjectInRoom(currentRoom, item):
    for thing in currentRoom.getObjects():
        if thing.getType().lower() == item.lower():
            return thing
    else:
        return False


def findObjectInPlayer(player, item):
    for thing in player.getInventory():
        if thing.getType().lower() == item.lower():
            return thing
    else:
        return False


def printInventory(target):
    for thing in target.getInventory():
        print(thing.getType().title())