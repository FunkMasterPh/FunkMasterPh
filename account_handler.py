from world_creator import *
from world_class import World
import pickle

playername = input("What is your name? ")
def loginPlayer(playername):
    """"""
    try:
        open(f'{playername.lower()}.P')
        return True
    except IOError:
        return False

def savePlayer(player, world):
    with open(f'{player._name.lower()}.P', 'wb') as f:
        pickle.dump(player, f)
    
    with open(f'{player._name.lower()}_world.P', 'wb') as f:
        pickle.dump(world, f)
    

def autoSave():
    while True:
        time.sleep(120)
        savePlayer(player, world)
        

if loginPlayer(playername):
    with open(f'{playername.lower()}.P', 'rb') as f:
        player = pickle.load(f)

    with open(f'{playername.lower()}_world.P', 'rb') as f:
        world = pickle.load(f)
        
else:
    player = Character(f'{playername.title()}', [])
    create_world()
    savePlayer(player)

print(player.getName()) 
print(player.getStr())

