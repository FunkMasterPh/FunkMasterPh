from enum import *

class PotionType(Enum):
    HEALTH = auto()
    DEXTERITY = auto()
    STRENGTH = auto()
    EXPERIENCE = auto()
    INVISIBILITY = auto()

class PotionPotency(IntEnum):
    FIVE = 5
    TEN = 10
    FIFTEEN = 15
    TWENTY = 20

class Flask():
    
    def __init__(self, potion: PotionType, potency: PotionPotency):
        self._potion = potion
        self._potency = potency

    def getPotionType(self):
        return self._potion
  
    def getPotionPotency(self):
        return self._potency

    def getType(self):
        return f"A {self._potion} potion of {self._potency} potency."
    
    def getPotionEffect(self):

        if self._potion == PotionType.HEALTH:
           potency = self.getPotionPotency()
           print(str(potency.name()))
        elif self._potion == PotionType.DEXTERITY:
            print("DEX")
        elif self._potion == PotionType.EXPERIENCE:
            print("XP")
        elif self._potion == PotionType.STRENGTH:
            print("STRENGTH")
        elif self._potion == PotionType.INVISIBILITY:
            print("Invisibility")