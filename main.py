import random

# Traits
INTERNAL_TYPES = ['fatty','strong','weak','thin']

# Create a worm.
class Worm:
    def __init__(self):
        self.internals = random.choice(INTERNAL_TYPES)

        match self.internals:
            case 'strong':  # If the trait is strong.
                self.health = random.randint(12, 18)  # Health.
                self.hunger = random.randint(12, 18)  # Hunger units.
                self.width = random.randint(10, 15)  # Width.
                self.length = random.randint(12, 18)  # Length.

            case 'fatty':  # If the trait is fatty.
                self.health = random.randint(9, 15)
                self.hunger = random.randint(20, 30)
                self.width = random.randint(15, 25)
                self.length = random.randint(10, 20)

            case 'weak':  # If the trait is weak.
                self.health = random.randint(5, 11)
                self.hunger = random.randint(6, 15)
                self.width = random.randint(7, 12)
                self.length = random.randint(8, 15)

            case 'thin':  # If the trait is thin.
                self.health = random.randint(7, 13)
                self.hunger = random.randint(5, 10)
                self.width = random.randint(3, 7)
                self.length = random.randint(8, 14)

        self.size = self.width + self.length  # Worm size.
        self.step = self.width  # Distance the worm travels at a time.
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
