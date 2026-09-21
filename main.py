import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

cmap = ListedColormap(['#202020', 'pink'])  # Color palette for the grid: black for empty cells and pink for the worm.

# Traits
INTERNAL_TYPES = ['fatty','strong','weak','thin']

# Create a world.
class World:
    def __init__(self):
        self.size = np.array([20, 20])  # World size.
        self.grid = np.zeros(self.size)  # Each grid cell represents an empty cell (0).

# Create a worm.
class Worm:
    def __init__(self):
        self.internals = random.choice(INTERNAL_TYPES)  # Randomly selected worm trait.

        match self.internals:
            case 'strong':  # If the trait is strong.
                self.health = random.randint(12, 18)  # Health.
                self.hunger = random.randint(12, 18)  # Hunger units.
                self.length = random.randint(12, 18)  # Length.

            case 'fatty':  # If the trait is fatty.
                self.health = random.randint(9, 15)
                self.hunger = random.randint(20, 30)
                self.length = random.randint(10, 20)

            case 'weak':  # If the trait is weak.
                self.health = random.randint(5, 11)
                self.hunger = random.randint(6, 15)
                self.length = random.randint(8, 15)

            case 'thin':  # If the trait is thin.
                self.health = random.randint(7, 13)
                self.hunger = random.randint(5, 10)
                self.length = random.randint(8, 14)

        self.max_health = self.health  # Maximum health at the start of the worm's life.
        self.max_hunger = self.hunger  # Maximum hunger at the start of the worm's life.
        self.state = 'alive'  # Worm status: alive or dead.
        self.x = 0  # Worm's starting x-coordinate (birth x-coordinate).
        self.y = 0  # Worm's starting y-coordinate (birth y-coordinate).

        if self.health <= 0:  # Worm death logic.
            self.state = 'dead'

    def tick(self):  # Logic for each program tick.
        self.hunger -= 1

        if self.hunger <= 0:
            self.health -= 1

worm = Worm()
world = World()

for i in range(worm.length):  # Draw the worm on the grid according to its length.
    world.grid[worm.x][worm.y] = 1
    worm.x += 1

plt.imshow(world.grid, cmap=cmap)  # Display the grid with the worm using the color palette.
plt.show()
