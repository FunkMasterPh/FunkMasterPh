from world_creator import *
import pickle

with open(f'{player._name}.obj', 'rb') as f:
    player = pickle.load(f)

print(player.getLevel())