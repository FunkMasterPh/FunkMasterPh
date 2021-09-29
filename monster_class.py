class Monster:
    """A template for creating a monster object."""
   
    def __init__(self, inventory: list):
        self._hp = 40
        self._str = 1
        self._dex = 5
        self._type = None
        self._inventory = inventory
        self._desc = None
        self._isAlive = True
        self._corpse = "decomposing body"
        self._corpseDesc = None
        self._objectType = "monster"

    def setIsAlive(self, arg):
        self._isAlive = arg
    
    def getIsAlive(self):
        return self._isAlive
        
    def setType(self, type):
        self._type = type
    
    def getObjectType(self):
        return self._objectType

    def getType(self):
        if self._isAlive == True:
            return self._type
        else:
            return self._corpse

    def getDesc(self):
        if self._isAlive == True:
            return self._desc
        else:
            return self._corpseDesc
    
    def getHP(self):
        return self._hp

    def getDex(self):

        return self._dex
    
    def takeDamage(self, dmg):
        
        self._hp = self._hp - dmg
        return dmg

    def setInventory(self, inventory: list):
        # To-Do    
        self._inventory = inventory

    def getInventory(self):
        # To-Do
        return self._inventory

    def doDamage(self):

        return self._str
        

    
