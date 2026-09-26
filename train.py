from env import world
from agent import q_table, choose_action, epsilon, gamma, alpha
import numpy as np
import pickle

for i in range(3000):
    state = world.reset()
    done = False
    total_reward = 0

    while not done:
        action = choose_action(state,q_table,epsilon)
        old_state = state
        state, reward, done = world.step(action)
        total_reward += reward
        best_next = np.max(q_table[state])
        target = reward + gamma * best_next
        q_table[old_state][action] += alpha * (target - q_table[old_state][action])

    epsilon = max(epsilon * 0.995, 0.05)

    print(total_reward)

with open('q_table.pkl','wb') as f:
    pickle.dump(dict(q_table), f)
