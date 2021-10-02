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

    def getPotionType(self):
        return self._potion
  
    def getPotionPotency(self):
        return self._potency

    def getPotionEffect(self):

        return self._potion

    def getType(self):
        return f"A {self._potion} potion of {self._potency} potency."    
    
    def setPlayerEffect(self, player):

        if self._potency == PotionType.HP:
            player.setHP(self._potency * 15)

        elif self._potion == PotionType.STR:
            player.setStr(self._potency)
        
        elif self._potion == PotionType.DEX:
            player.setDex(self._potency)

        elif self._potion == PotionType.XP:
            player.setXP(self._potency * 50) 