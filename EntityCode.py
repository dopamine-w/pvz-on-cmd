from enum import Enum

class Range(Enum):
     LANE                = 0
     LOBBED              = 1
     THREEBYTHREE        = 2
     TILE                = 3
     BACK                = 4
     FRONTANDBACK        = 5
     LOBBED_FRONTANDBACK = 6
     CLOSE               = 7

"""
Code for plants and zombies abilities
"""
class EntityCode:
     def __init__(self, level):
          self.lawn = level[0]["Lawn"]
          self.level_variables = level[0]["LevelVariables"]

     """
     Increases the sun count by a specified amount.
     """
     def increase_sun(self, sun: int):
          self.level_variables["sun"] += sun

     """
     Attacks a zombie in a specified range.
     """
     def attack_zombie(self, range: Range, damage):
          pass

     """
     Attacks a plant in a specified range.
     """
     def attack_plant(self, range: Range, damage):
          pass
