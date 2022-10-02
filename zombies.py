from game import Game
from plants import Plant
import time

# Every zombie will inherit from this class
class Zombie:
     def __init__(self, game: Game, tile, name, health, attack):
          self.name = name
          self.health = health
          self.attack = attack

     def destroy(self):
          del self

class basic(Zombie):
     def __init_subclass__(cls):
          return super().__init_subclass__()

     def eat_plant(self, plant: Plant):
          plant.health -= 10
          time.sleep(0.5)