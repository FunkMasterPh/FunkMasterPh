from world_creator import *
import pickle

with open(f'{player._name}.obj', 'wb') as f:
    pickle.dump(player, f)

