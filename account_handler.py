from world_creator import *
from world_class import World
import pickle
import time, os

playername = input("What is your name? ")
def loginPlayer(playername):
    """"""
    try:
        open(f'{playername}/{playername.lower()}.P')
        return True
    except IOError:
        return False

def savePlayer(player):

    
    with open(f'{playername}/{player._name.lower()}.P', 'wb') as f:
        pickle.dump(player, f)

def saveWorld(caves):
    
    with open(f'{playername}/{player._name.lower()}_caves.P', 'wb') as f:
        pickle.dump(caves, f)
    
   
def autoSave():
    while True:
        time.sleep(120)
        savePlayer(player)  
        saveWorld([cave_1, cave_2, cave_3, cave_4, cave_5])
        

if loginPlayer(playername):
    with open(f'{playername}/{playername.lower()}.P', 'rb') as f:
        player = pickle.load(f)
        
else:
    player = Character(f'{playername.title()}', [])

    os.mkdir(f'{playername}')
    

print(player.getName()) 
print(player.getStr())

