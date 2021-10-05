from __future__ import annotations
from items_class import Item


class Torch(Item):
    def __init__(self):
        super().__init__()
        self._weight = 3
        self._value = 5
        self._type = "torch"
        self._desc ="A stick on fire. "
        self._isOn = False
    
    #returns on/off status of torch
    def getOn(self):
        return self._isOn
    
    #sets torch status to on
    def setOnOff(self, arg):
        self._isOn = arg
    
    def getDesc(self):
        return self._desc

class Key(Item):
    def __init__(self, id, desc):
        super().__init__()
        self._weight = 2
        self._value = 50
        self._type = "key"
        self._id = id
        self._desc = desc
    
    def getDesc(self):
       return self._desc
    
    def getID(self):
        return self._id


class Lock(Item):
    def __init__(self, id):
        super().__init__()
        self._isLocked = True
        self._id = id
        self._desc = ""

    def getDesc(self):
        return self._desc
    
    def getID(self):
        return self._id
            
  
class Chest(Item):
    def __init__(self, inventory: list, lock: Lock):
        super().__init__()
        self._inventory = inventory
        self._lock = lock
        self._isOpen = False
        self._desc = "A treasure chest."
        self._type = "chest"
        self._weight = 1000
        

    def getIsOpen(self):
        return self._isOpen
    
    def getIsOpenPrint(self):
        if self._isOpen:
            self._desc += "\nIt's open!"
        elif not self._isOpen:
            self._desc += "\nIt's closed."

    def getDesc(self):
        self.getIsOpenPrint()
        return self._desc

    def setIsOpen(self, arg):
        self._isOpen = arg