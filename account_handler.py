from world_creator import *
from world_class import World
import pickle
import time

playername = input("What is your name? ")
def loginPlayer(playername):
    """"""
    try:
        open(f'{playername.lower()}.P')
        return True
    except IOError:
        return False

def savePlayer(player):

    
    with open(f'{player._name.lower()}.P', 'wb') as f:
        pickle.dump(player, f)

def saveWorld(cave_1, cave_2, cave_3, cave_4, cave_5):
    
    with open(f'{player._name.lower()}_cave1.P', 'wb') as f:
        pickle.dump(cave_1, f)
    with open(f'{player._name.lower()}_cave2.P', 'wb') as f:
        pickle.dump(cave_2, f)
    with open(f'{player._name.lower()}_cave3.P', 'wb') as f:
        pickle.dump(cave_3, f)
    with open(f'{player._name.lower()}_cave4.P', 'wb') as f:
        pickle.dump(cave_4, f)
    with open(f'{player._name.lower()}_cave5.P', 'wb') as f:
        pickle.dump(cave_5, f)
   
def autoSave():
    while True:
        time.sleep(120)
        savePlayer(player)  
        saveWorld(cave_1, cave_2, cave_3, cave_4, cave_5)
        

if loginPlayer(playername):
    with open(f'{playername.lower()}.P', 'rb') as f:
        player = pickle.load(f)
        
else:
    player = Character(f'{playername.title()}', [])
    

print(player.getName()) 
print(player.getStr())

