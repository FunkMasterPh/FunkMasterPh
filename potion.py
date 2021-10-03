from enum import Enum, IntEnum, auto

class PotionType(Enum):
    HP = auto()
    DEX = auto()
    STR = auto()
    XP = auto()
    INVIS= auto()

class PotionSize(IntEnum):
    SMALL = 1
    MEDIUM = 2
    BIG = 3
    
class Flask():
    
    def __init__(self, potion: PotionType, potency: PotionSize):
        self._potion = potion
        self._potency = potency
        self._objectType = "potion"
        self._weight = 1
        
    def getWeight(self):
        return self._weight

    def getPotionType(self):
        return self._potion
  
    def getPotionPotency(self):
        return self._potency

    def getPotionEffect(self):

        return self._potion
    
    def getObjectType(self):
        return self._objectType

    def getType(self):
        return "potion"

    def getDesc(self):
        """Returns a description of the potion, ranging from a small to big 
        str/dex/hp/xp/invis potion."""
        if self._potency == PotionSize.SMALL:
            flask_size = "small"
        elif self._potency == PotionSize.MEDIUM:
            flask_size = "medium"
        elif self._potency == PotionSize.BIG:
            flask_size = "big"

        if self._potion == PotionType.HP:
            potion_type = "health"
        elif self._potion == PotionType.STR:
            potion_type = "strength"
        elif self._potion == PotionType.DEX:
            potion_type = "dexterity"
        elif self._potion == PotionType.XP:
            potion_type = "experience"
        elif self._potion == PotionType.INVIS:
            potion_type = "invisibility"

        return f"A {flask_size} potion of {potion_type}."    
    
    def setPlayerEffect(self, player):

        if self._potion == PotionType.HP:
            player.setHP(self._potency * 15)

        elif self._potion == PotionType.STR:
            player.setStr(self._potency)
        
        elif self._potion == PotionType.DEX:
            player.setDex(self._potency)

        elif self._potion == PotionType.XP:
            player.setXP(self._potency * 50) 