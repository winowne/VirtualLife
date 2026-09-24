import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

cmap = ListedColormap([
    '#202020',
    'white',
    'green',
    'red'
])

class Nutrition:
    def __init__(self, size):
        self.satiety = random.randint(5, 10)
        self.x = random.randint(0, size[0] - 1)
        self.y = random.randint(0, size[1] - 1)

class Cell:
    def __init__(self):
        self.body = [(1,0)]


class World:
    def __init__(self):
        self.size = np.array([20, 20])
        self.grid = np.zeros(self.size)

        self.cell = Cell()
        self.nutrition = None
        self.spawn_nutrition()
        self.redraw()

    def spawn_nutrition(self):
        while True:
            nutrition = Nutrition(self.size)
            if self.grid[nutrition.x][nutrition.y] == 0:
                self.nutrition = nutrition
                self.grid[nutrition.x][nutrition.y] = 3
                return

    def tick(self):
        self.move()
        if self.nutrition is not None and self.cell.body[0] == (self.nutrition.x, self.nutrition.y):
            self.nutrition = None
        if self.nutrition is None:
            self.spawn_nutrition()
        self.redraw()

    def draw_cell(self):
        for (x,y) in self.cell.body:
            self.grid[x][y] = 1


    def move(self):
        action_table = {
            0: (0, -1),
            1: (0, 1),
            2: (-1, 0),
            3: (1, 0),
        }

        x, y = self.cell.body[0]
        new_cell = (x + 1, y)

        if 0 <= new_cell[0] < self.size[0] and 0 <= new_cell[1] < self.size[1]:
            self.cell.body.append(new_cell)
            self.cell.body.pop(0)


    def redraw(self):
        self.grid = np.zeros(self.size)
        self.draw_cell()
        if self.nutrition is not None:
            self.grid[self.nutrition.x][self.nutrition.y] = 3

world = World()
cell = world.cell

plt.ion()
figure, axis = plt.subplots()

while True:
    world.tick()
    axis.clear()
    axis.imshow(world.grid, cmap=cmap)
    plt.pause(0.1)