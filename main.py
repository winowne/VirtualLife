import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


cmap = ListedColormap([
    '#202020',
    'white',
    '#FCF2F7',
])  # Empty cells, worm body, worm head, and nutrition.

INTERNAL_TYPES = ['fatty', 'strong', 'weak', 'thin']


class Nutrition:
    def __init__(self, size):
        self.satiety = random.randint(5, 10)
        self.x = random.randint(0, size[0] - 1)
        self.y = random.randint(0, size[1] - 1)


class Worm:
    def __init__(self):
        self.internals = random.choice(INTERNAL_TYPES)

        match self.internals:
            case 'strong':
                self.health = random.randint(12, 18)
                self.hunger = random.randint(12, 18)

            case 'fatty':
                self.health = random.randint(9, 15)
                self.hunger = random.randint(20, 30)

            case 'weak':
                self.health = random.randint(5, 11)
                self.hunger = random.randint(6, 15)

            case 'thin':
                self.health = random.randint(7, 13)
                self.hunger = random.randint(5, 10)

        self.body = [(1,0), (2,0), (3,0)]
        self.max_health = self.health
        self.max_hunger = self.hunger
        self.state = 'alive'
        self.age = 0
        self.age_limit = random.randint(50, 100)

        if self.health <= 0:
            self.state = 'dead'


class World:
    def __init__(self):
        self.size = np.array([20, 20])
        self.grid = np.zeros(self.size)
        self.worm = Worm()

        self.redraw()

    def spawn_nutrition(self):
        while True:
            nutrition = Nutrition(self.size)
            if self.grid[nutrition.x][nutrition.y] == 0:
                self.nutrition = nutrition
                self.grid[nutrition.x][nutrition.y] = 3
                return

    def tick(self):
        if self.worm.state == 'dead':
            return

        self.worm.hunger -= 1
        self.worm.age += 1

        if self.worm.hunger <= 0:
            self.worm.health -= 1

        if self.worm.health <= 0 or self.worm.age >= self.worm.age_limit:
            self.worm.state = 'dead'
            return

        self.move()
        self.redraw()

    def draw_worm(self):
        for (x,y) in self.worm.body[:-1]:
            self.grid[x][y] = 1

        (x,y) = self.worm.body[-1]
        self.grid[x][y] = 2

    def move(self):
        head_x, head_y = self.worm.body[-1]
        new_head = (head_x + 1, head_y)

        if 0 <= new_head[0] < self.size[0] and 0 <= new_head[1] < self.size[1]:
            self.worm.body.append(new_head)
            self.worm.body.pop(0)
        



    def redraw(self):
        self.grid = np.zeros(self.size)
        self.draw_worm()

world = World()
worm = world.worm

plt.ion()
figure, axis = plt.subplots()

while True:
    world.tick()
    print(f'health: {worm.health}, hunger: {worm.hunger}')

    axis.clear()
    axis.imshow(world.grid, cmap=cmap)
    plt.pause(0.1)
