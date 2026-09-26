import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Значения сетки соответствуют цветам: 0 — пустая клетка, 1 — тело, 2 — еда.
cmap = ListedColormap([
    '#202020',
    'white',
    'red'
])

# Для каждого действия задаётся смещение по координатам x и y.
action_table = {
            0: (0, -1),
            1: (0, 1),
            2: (-1, 0),
            3: (1, 0),
        }

class Nutrition:
    def __init__(self, size):
        self.x = random.randint(0, size[0] - 1)
        self.y = random.randint(0, size[1] - 1)

class Cell:
    def __init__(self):
        self.body = [(1, 0)]


class World:
    def __init__(self):
        self.size = np.array([20, 20])
        self.grid = np.zeros(self.size)
        self.step_count = 0
        self.episode = 0
        self.max_steps = 200

        self.cell = Cell()
        self.nutrition = None
        self.spawn_nutrition()
        self.redraw()

    def spawn_nutrition(self):
        # Еда создаётся заново, пока случайно не попадёт на свободную клетку.
        while True:
            nutrition = Nutrition(self.size)
            if self.grid[nutrition.x][nutrition.y] == 0:
                self.nutrition = nutrition
                self.grid[nutrition.x][nutrition.y] = 2
                return
            
    def move(self, action):
        x, y = self.cell.body[0]
        dx, dy = action_table[action]
        new_cell = (x + dx, y + dy)

        if 0 <= new_cell[0] < self.size[0] and 0 <= new_cell[1] < self.size[1]:
            # Новая координата заменяет старую: сейчас тело состоит из одной клетки.
            self.cell.body.append(new_cell)
            self.cell.body.pop(0)
            return True
        else:
            return False
        
    def get_state(self):
        x, y = self.cell.body[0]
        # Агент получает не абсолютные координаты, а расстояние до еды.
        difference = x - self.nutrition.x, y - self.nutrition.y
        return difference
    
    def step(self, action):
        reward = 0
        self.step_count += 1
        moved = self.move(action)

        # Агент получает небольшую награду за движение и штраф за столкновение со стеной.
        if moved:
            reward -= 0.01
        else:
            reward -= 1
        if self.cell.body[0] == (self.nutrition.x, self.nutrition.y):
            reward += 1
            self.nutrition = None
            self.spawn_nutrition()

        # Эпизод заканчивается после заданного количества шагов.
        done = self.step_count >= self.max_steps

        return self.get_state(), reward, done

    def draw_cell(self):
        for (x,y) in self.cell.body:
            self.grid[x][y] = 1

    def redraw(self):
        # Сетка полностью создаётся заново, чтобы убрать старое положение клетки и еды.
        self.grid = np.zeros(self.size)
        self.draw_cell()
        if self.nutrition is not None:
            self.grid[self.nutrition.x][self.nutrition.y] = 2

    def reset(self):
        self.step_count = 0
        self.grid = np.zeros(self.size)
        self.cell.body = [(1,0)]
        self.nutrition = None
        self.spawn_nutrition()
        self.episode += 1
        return self.get_state()

world = World()
cell = world.cell

plt.ion()
figure, axis = plt.subplots()

while True:
    world.step()
    world.redraw()
    axis.clear()
    axis.imshow(world.grid, cmap=cmap)
    plt.pause(0.1)
