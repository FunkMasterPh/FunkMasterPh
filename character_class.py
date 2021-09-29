import random
from items_class import *

class Character:
    """Initializes a template for character creation."""
    def __init__(self, name, item : list):
        self._name = name
        self._armor = None
        self._hp = 100
        self._str = 2
        self._dex = 2
        self._isAlive = True
        self._damageModifier = 0
        self._xp = 0
        self._inventory = item
        self._wielded = False
        self._hands = None
        #self._head = None
        #self._chest = None
        #self._legs = None
        

    def getName(self):
        return self._name

    def getHP(self):
        return self._hp
    
    def getXP(self):
        return self._xp

    def setXP(self, XP):
        self._xp += XP

    def setHP(self, newHP):
        self._hp = newHP
    
    def setStr(self, newStr):
        self._str = newStr
    
    def getStr(self):
        return self._str

    def getIsAlive(self):
        return self._isAlive

    def getDex(self):
        return self._dex

    def takeDamage(self, dmg):
        self._hp = self._hp - dmg
        return dmg
        
    def getDamageModifier(self):
        return self._damageModifier 
    
    def doDamage(self):
        return (random.randint(1, (self._str + self._damageModifier)))
    
    def pickUp(self, item):
        self._inventory.append(item)

    def getInventory(self):
        return self._inventory

    def setWielded(self, weapon):
        if self._wielded:
            return False
        else:
            self._wielded = weapon
            self._damageModifier += weapon.getDamage()

    def getWielded(self):
        return self._wielded
            
    def setUnwield(self, weapon):
        self._wielded = False
        self._damageModifier -= weapon.getDamage()

    def levelUp(self):
        if self._xp >= 200:
            self._hp += 10
            self._str += 1
            self._dex += 1
            return True
        else:
            return False
        


    