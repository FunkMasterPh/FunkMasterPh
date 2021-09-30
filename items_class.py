class Item:
    def __init__(self):
        self._weight = None
        self._value = None
        self._type = None
        self._itemType = None
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

    def getDesc(self):
        return self._desc


class Weapon(Item):
    def __init__(self):
        super().__init__()
        self._damage = None
        self._itemType = Weapon
    
    #returns weapon damage
    def getDamage(self):
        return self._damage
   
   
class Armor(Item):
    def __init__(self):
        super().__init__()
        self._armor = None
        self._itemType = Armor

    #returns armor stats
    def getStat(self):
        return self._armor
        

class Misc(Item):
    def __init__(self):
        super().__init__()
        self._desc = None
        self._itemType = Misc

    #returns description of item  
    def getDesc(self):
        return self._desc


class Potion(Item):
    def __init__(self, potency, effect):
        super().__init__()
        self._desc = f"A delicious {effect} potion."
        self._isConsumable = True
        self._effect = effect
        self._potency = potency
        self._itemType = Potion
    
    #returns item description
    def getDesc(self):
        return self._desc


potion_types =     [
                    "health", 
                    "strength",
                    "dexterity",
                    "experience", 
                    "invisibility"
                    ]


