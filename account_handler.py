from character_class import Character
from world_creator import *
from world_class import World
import pickle
import time, os
import commands as cmd

playername = input("What is your name? ")

def loginPlayer(playername):
    """"""
    try:
        open(f'{playername}/{playername.lower()}.P')
        return True
    except IOError:
        return False


def saveGame(player, caves):

    with open(f'{playername}/{player._name.lower()}.P', 'wb') as f:
        pickle.dump(player, f)
    
    with open(f'{playername}/{player._name.lower()}_caves.P', 'wb') as f:
        pickle.dump(caves, f)
     

def autoSave(caves):
    while True:
        saveGame(player, caves)  
        time.sleep(60)
        

if loginPlayer(playername):
    with open(f'{playername}/{playername.lower()}.P', 'rb') as f:
        player = pickle.load(f)
        print(f"Character {player.getName()} logged in.") 
else:
    player = Character(f'{playername.title()}', [])
    print(f"Character {player.getName()} created.") 
    os.mkdir(f'{playername}')
    
