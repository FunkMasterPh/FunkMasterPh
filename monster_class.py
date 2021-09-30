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
        self._giveXP = None
    
    def giveXP(self):
        return self._giveXP
    
    #returns monster health
    def getHP(self):
        return self._hp

    #returns monster dexterity
    def getDex(self):

        return self._dex
    
    #returns what type of object this is
    def getObjectType(self):
        return self._objectType
    
    #returns a monster type if monster is alive, if dead returns a corpse
    def getType(self):
        if self._isAlive == True:
            return self._type
        else:
            return self._corpse
    
    #returns a description of monster if monster is alive, if dead returns a description of corpse
    def getDesc(self):
        if self._isAlive == True:
            return self._desc
        else:
            return self._corpseDesc

    #returns monster dead/alive status
    def getIsAlive(self):
        return self._isAlive
    
    #returns monsters inventory
    def getInventory(self):
        return self._inventory
    
    #changes monster dead/alive status
    def setIsAlive(self, arg):
        self._isAlive = arg
        
    #changes monsters type
    def setType(self, type):
        self._type = type
    
    #changes monsters inventory
    def setInventory(self, inventory: list):   
        self._inventory = inventory
    
    #allows monster to take damage
    def takeDamage(self, dmg):
        
        self._hp = self._hp - dmg
        return dmg

    #allows monster to do damage
    def doDamage(self):

        return self._str
        

    
