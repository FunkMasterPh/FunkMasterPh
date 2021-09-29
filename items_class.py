class Item:
    def __init__(self):
        self._weight = None
        self._value = None
        self._type = None
        self._itemType = None
        self._objectType = "item"
      
    def getType(self):
        return self._type

    def getValue(self):
        return self._value

    def getWeight(self):
        return self._weight

    def getItemType(self):
        return self._itemType
        
    def getObjectType(self):
        return self._objectType


class Weapon(Item):
    def __init__(self):
        super().__init__()
        self._damage = None
        self._itemType = Weapon

    def getDamage(self):
        return self._damage
   
   
class Armor(Item):
    def __init__(self):
        super().__init__()
        self._armor = None
        self._itemType = Armor

    def getStat(self):
        return self._armor
        

class Misc(Item):
    def __init__(self):
        super().__init__()
        self._desc = None
        self._itemType = Misc
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
    def getDesc(self):
        return self._desc


potion_types =     [
                    "health", 
                    "strength",
                    "dexterity",
                    "experience", 
                    "invisibility"
                    ]


