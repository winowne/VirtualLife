import matplotlib.pyplot as plt
from env import world, cmap
import numpy as np
from agent import q_table

plt.ion()
figure, axis = plt.subplots()
state = world.reset()

for step in range(200):
    action = np.argmax(q_table[state])
    state, reward, done = world.step(action)
    world.redraw()
    axis.clear()
    axis.imshow(world.grid, cmap=cmap)
    plt.pause(0.1)