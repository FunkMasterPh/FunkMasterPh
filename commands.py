import fight
import library
from world_creator import *
from character_class import Character


""" Contains commands available through the input loop. """

_HELP = "help"
_WIELD_ITEM = "wield"
_UNWIELD_ITEM = "unwield"
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
_ATTACK = "attack"
_QUIT = "quit"

_PLAYER_COMMANDS = [
    _HELP,
    _WIELD_ITEM,
    _UNWIELD_ITEM,
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
    _ATTACK, 
    _QUIT
]   

def displayHelpMenu():
    """Displays available commands."""
    print(18 * "*", "AVAILABLE COMMANDS", 18 * "*")
    print("- HELP: Shows this menu.")
    print("- ATTACK <ENEMY>: Attack someone! Or something!")
    print("- STATUS: Display information about yourself.")
    print("- WIELD <ITEM>: Wield a weapon from your inventory.")
    print("- UNWIELD <ITEM>: Unwield your wielded weapon.")
    print("- TAKE <ITEM>: Add an item to your inventory.")
    print("- DROP <ITEM>: Discard of an item in your inventory.")
    print("- EQUIP <ITEM>: Equip an item, such as a helmet.")
    print("- UNEQUIP <ITEM>: Remove an equipped item.")
    print("- INVENTORY: List all the items your are carrying.")
    print("- LOOT <TARGET>: Loot a slain enemy.")
    print("- CONSUME <ITEM>: Drink a potion, or eat a biscuit.")
    print("- EXAMINE <ITEM>: Examine a thing or a room.")
    print("- LIGHT <ITEM>: Light a fire.")
    print("- EXTINGUISH <ITEM>: Put a fire out.")
    print("- GO <DIRECTION>: Go somewhere and do something.")
    print("- QUIT: Leave the game, for some reason.")
    print(56 * "*")

    
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
    print(currentRoom)
    if library.canPlayerSee(currentRoom):
        for object in currentRoom.getObjects():
            if object.getType().lower() == target.lower():
                fight.letsFight(player, object)
                return True
       
def consume(self, item):
    """Checks what potion you want to drink and alters stats accordingly."""
    if Potion.getDesc() == [0]:
        self._hp += item.getHP()
        self._inventory.remove(item)
    elif item.getType() == "Strength_Potion":
        self._str += item.getStr()
        self._inventory.remove(item)
    elif item.getType() == "Dexterity_Potion":
        self._dex += item.getDex()
        self._inventory.remove(item)
    elif item.getType() == "XP_Potion":
        self._xp += item.getXP()
        self._inventory.remove(item)
    else:
        return False

def examineMonster(monster):
    """Prints the description and inventory of target monster."""
    print(monster.getDesc())
    print("It's carrying: ")
    for item in monster.getInventory():
        print(item.getType())

#takes user input and prints info about it
def examine(toLookAt, currentRoom):

    if toLookAt == "room":
        library.printInterface(currentRoom)
    
    else :
        for object in currentRoom.getObjects():
            if object.getType().lower() == toLookAt.lower():
                if object.getObjectType() == "monster":
                    examineMonster(object)
                elif object.getObjectType() == "item":
                    print(object.getDesc())

        for object in player.getInventory():
            if object.getType().lower() == toLookAt.lower():
                if object.getObjectType() == "monster":
                    examineMonster(object)
                elif object.getObjectType() == "item":
                    print(object.getDesc())       
            
    
def wieldWeapon(item):
    """Checks if you have weapon in inventory, if it is a weapon and if all 
       true changes wielded status accordingly."""
    for weapon in player.getInventory():
        if weapon.getType().lower() == item.lower():
            if weapon.getItemType() == Weapon:
                if player.setWielded(weapon) == False:
                    print("You've already wielded a weapon.")
                    return False
                else:
                    return True
            else: 
                print("That's not a weapon.")
                return False
    else:
        print("I don't have that item.")    
        

def unwieldWeapon(item):
    """Check if weapon is wielded, unwield if true."""
    for weapon in player.getInventory():
        if weapon.getType().lower() == item.lower():
            if weapon == player.getWielded():
                player.setUnwield(weapon)
                return True
            else: 
                return False


def takeItem(item_to_take, currentRoom):
    """If item in room inventory, remove from room and add to player inventory."""
    for item in currentRoom.getObjects():
        if item.getObjectType() == "item":
            if item.getType().lower() == item_to_take.lower():
                currentRoom.getObjects().remove(item)
                player.getInventory().append(item)
                print(player.getInventory())
                return True
            

def dropItem(item_to_drop, currentRoom):
    """If item's in inventory, remove from inventory and add it to room inventory."""
    for item in player.getInventory():
        if item.getType().lower() == item_to_drop.lower():
            if item == player.getWielded():
                unwieldWeapon(item_to_drop)
            player.getInventory().remove(item)
            currentRoom.getObjects().append(item)
            print(player.getInventory())
            return True



def checkInventory():
    """Prints player inventory."""
    print("You're carrying the following items:")
    for item in player.getInventory():
        print(item.getType().title())



def loot(currentRoom, itemToLoot):
    """Checks if monsters are dead and adds their inventory to player inventory."""
    for object in currentRoom.getObjects():
        if object.getObjectType() == "monster" and object.getIsAlive() == False and object.getInventory():
            while object.getInventory():
                loot = object.getInventory().pop()
                player.getInventory().append(loot)
            return True


def light(item):
    """Checks if you have torch in inventory, lights it if true."""
    for object in player.getInventory():
        if object.getType().lower() == item.lower():
            if item.lower() == "torch":
                if object.getOn() != True:
                    object.setOnOff(True)
                    player.setIlluminated(True)
                    return True
                else:
                    print("The torch is already lit.")
                    return False
            else:
                print("You can't light that.")
                return False
    else:
        print("I don´t have that.")

def extinguish(item):
    """Checks if torch is in player inventory and extinguishes if its lit."""
    for object in player.getInventory():
        if object.getType().lower() == item.lower():
            if object.getType() == "torch" and object.getOn():
                object.setOnOff(False)
                player.setIlluminated(False)
                return True
            