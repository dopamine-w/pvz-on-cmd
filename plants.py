from game import Game
import time

# Every plant will inherit from this class
class Plant:
     def __init__(self, game: Game, tile, sun, health, attack = 0, plantonfield = False):
          self.sun = sun
          self.health = health
          self.attack = attack
          self.game = game
          self.plantonfield = plantonfield

     def destroy(self):
          del self

class Sunflower(Plant):
     def __init_subclass__(cls):
          return super().__init_subclass__()

     def usage(self):
          while self.plantonfield == True:
               if self.health == 0:
                    self.plantonfield = False
                    self.destroy()

               self.game.sun += 50
               time.sleep(15)

     def plantfood(self):
          self.game.sun += 150