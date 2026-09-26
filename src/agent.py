from collections import defaultdict
import pickle
import os
import numpy as np
import random

if os.path.exists('q_table.pkl'):
    with open('q_table.pkl','rb') as f:
        loaded = pickle.load(f)
        q_table = defaultdict(lambda: np.zeros(4), loaded)
else:
    q_table = defaultdict(lambda: np.zeros(4))

epsilon = 1.0
gamma = 0.95
alpha = 0.1

def choose_action(state,q_table,epsilon):
    if random.random() < epsilon:
        return random.randint(0,3)
    else:
        return np.argmax(q_table[state])
    