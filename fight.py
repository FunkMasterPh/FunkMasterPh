from monster_class import Monster
from goblin_class import *
from character_class import Character
from world_creator import *
import random
import time
from library import *

def chanceToHit(attacker, defender):
    """randomises the chance to hit your target based on character and monster dexterity level"""

    if random.randint(1, attacker.getDex()) >= random.randint(1, defender.getDex()):
        return True

def letsFight(player, monster):
    """starts a combat loop where if monster is defeated it sets monster alive status to false and it gives player experience"""
    while True:
        if chanceToHit(player, monster):
            print(f"You attack the {monster.getType()} and do {monster.takeDamage(player.doDamage())} damage!")
            if monster.getHP() <= 0:
                print("You killed your foe.")
                monster.setIsAlive(False)
                player.setXP(monster.giveXP())
                if player.levelUp():
                    print("You leveled up!")
                break
        else:
            print("You missed!")
        if chanceToHit(monster, player):
            print(f"The {monster.getType()} attacks you and does {player.takeDamage(monster.doDamage())} damage!")
            if player.getHP() <= 0:
                print("You die.")
                library.playerDeath(player.getName())
                break
        else:
            print(f"The {monster.getType()} missed!")
        print(f"##### You: {player.getHP()} HP ************ ",
        f"{monster.getType()}: {monster.getHP()} HP #####\n")
        time.sleep(2)
               