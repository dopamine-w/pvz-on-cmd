from concurrent.futures import thread
import time
import json
import threading
from enum import Enum

# Just to show if the player wins or loses
class Level_Status(Enum):
     FAIL = 0
     WIN  = 1

# Runs everything in the level
class Level_Runner:
     def __init__(self, level_name):
          self.level_name = level_name
          self.level_status: bool
          self.read_level()

     # Reads the level data from the json file
     def read_level(self):
          with open(f"{self.level_name}.json", "r") as level_file:
               level_read = json.load(level_file)

               self.level_options = level_read[0]["level_options"]
               self.wave_options = level_read[0]["waves"]
               self.level_variables = level_read[0]["level_variables"]

               level_file.close()

     # Places something on a tile. If the item parameter is none, whatever is on the tile will be desroyed
     def tile_place(self, tile, item):
          tile_row = f"row{tile.split('x')[0]}"
          tile_column = int(tile.split("x"))[1]

          with open(f"{self.level_name}.json", "w") as level:
               level_json = json.load(level)
               tile: dict = level_json[0]["lawn"][tile_row][tile_column]
               tile.update(item)

     # Summons new waves
     def new_wave(self):
          current_wave = 1
          max_waves = self.wave_options["number_of_waves"]

          for i in range(self.wave_options["number_of_waves"]):
               time.sleep(self.wave_options["time_before_zombies"])

               for i in range(len(self.wave_options["wave_zombies"][f"wave_{current_wave}"])):
                    self.tile_place(self.wave_options["wave_zombies"][f"wave_{current_wave}"], self.wave_options["wave_zombies"][f"wave_{current_wave}"])
               
               current_wave += 1
               
               if current_wave == max_waves:
                    self.level_status = Level_Status.WIN
                    return

               time.sleep(self.wave_options["time_before_waves"])

     # Shows the level stuff, like zombies, plants, etc
     def show_level(self):
          with open(f"{self.level_name}.json", "r") as level:
               level_json = json.load(level)
               lawn = level_json[0]["lawn"]

               for i in range(len(lawn)):
                    i += 1
                    print(f"Row {i}: " + str(lawn[f"row{i}"]))

     # Runs the level
     def run_level(self):
          processes = [threading.Thread(target=self.new_wave())]

# This is just for testing purpouses
level1 = Level_Runner("levels/testlevel")
level1.show_level()