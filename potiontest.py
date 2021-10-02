import potion
from world_creator import *

SMALL = 1
MEDIUM = 2
BIG = 3

potion1 = potion.Flask(potion.PotionType.STR, potion.PotionSize.MEDIUM)

print(player.getStr())

print(potion1.getPotionEffect())
if potion1.getPotionPotency() == MEDIUM:
    print("Yup")
else:
    print("Nope")

potion1.setPlayerEffect(player)

print(player.getStr())