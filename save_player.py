from world_creator import *
import pickle

with open(f'{player._name}.P', 'wb') as f:
    pickle.dump(player, f)

