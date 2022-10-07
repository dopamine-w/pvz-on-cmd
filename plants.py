import time
import json

# Every plant will inherit from this class
class Plant:
     def __init__(self, name, levelname, health, attack = 0):
          self.name = name
          self.levelname = f"levels/{levelname}.json"
          self.health = health
          self.attack = attack

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

          with open(self.levelname, "r") as level:
               level_json = json.load(level)

               level_json[0]["level_variables"]["sun"] += 0

               level.close()