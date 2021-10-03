from world_creator import *
import pickle

playername = input("What is your name? ")

def loginPlayer(playername):

    try:
        open(f'{playername.lower()}.P')
        return True
    except IOError:
        return False

def savePlayer(player):
    with open(f'{player._name.lower()}.P', 'wb') as f:
        pickle.dump(player, f)
        return True
        

def autoSave():
    while True:
        time.sleep(120)
        savePlayer(player)
        

if loginPlayer(playername):
    with open(f'{playername.lower()}.P', 'rb') as f:
        player = pickle.load(f)

else:
    player = Character(f'{playername.title()}', [axe2, torch1])
    savePlayer(player)

print(player.getName()) 
print(player.getStr())

