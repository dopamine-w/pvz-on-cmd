import time
import json

# Every plant will inherit from this class
class Plant:
     def __init__(self, name, levelname, health, attack = 0):
          self.name = name
          self.level = json.load(open(f"levels/{levelname}.json", "r"))
          self.health = health
          self.attack = attack

     def destroy(self):
          del self

class Sunflower(Plant):
     def __init_subclass__(cls):
          return super().__init_subclass__()

     def usage(self):
          pass