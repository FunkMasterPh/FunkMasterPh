from abc import abstractmethod

class Item:
    def __init__(self):
        self._weight = None
        self._value = None
        self._type = None
        self._itemType = "item"
        self._objectType = "item"
        self._desc = None

    #method for getting type desciption
    def getType(self):
        return self._type

    #method for getting item value
    def getValue(self):
        return self._value

    #method for getting item weight
    def getWeight(self):
        return self._weight

    #method for getting what type of item 
    def getItemType(self):
        return self._itemType
    
    #method for getting what type of object  
    def getObjectType(self):
        return self._objectType
    
    @abstractmethod
    def getDesc(self):
        pass
        


class Weapon(Item):
    def __init__(self):
        super().__init__()
        self._damage = None
        self._itemType = "weapon"
        self._value = 1
    
    def getDamage(self):
        """Returns weapon damage."""
        return self._damage
   
  
class Armor(Item):
    def __init__(self, type, armorLocation, damageMitigation):
        super().__init__()
        self._value = 10
        self._itemType = "armor"
        self._type = type
        self._armorLocation = armorLocation
        self._damageMitigation = damageMitigation
        self._weight = 10
    def getArmorLocation(self):
        """Returns armor location."""
        return self._armorLocation
        
    
    def getDamageMitigation(self):
        """Returns damage mitigation."""
        return self._damageMitigation
        

class Potion(Item):
    def __init__(self, potency, effect):
        super().__init__()
        self._desc = f"A delicious {effect} potion."
        self._isConsumable = True
        self._effect = effect
        self._potency = potency
        self._itemType = "potion"
    
    #returns item description
    def getDesc(self):
        return self._desc



