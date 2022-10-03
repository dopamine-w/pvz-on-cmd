from concurrent.futures import thread
import time
import json
import threading
from enum import Enum

# Just to show if the player wins or loses
class Level_Status(Enum):
     FAIL      = 0
     WIN       = 1
     UNDECIDED = 2

# Runs everything in the level
class Level_Runner:
     def __init__(self, level_name):
          self.level_name = f"levels/{level_name}.json"
          self.level_status = Level_Status.UNDECIDED
          self.read_level()
          self.run_level()

     def __repr__(self):
          return self.show_level()

     # Reads the level data from the json file
     def read_level(self):
          with open(f"{self.level_name}", "r") as level_file:
               level_read = json.load(level_file)

               self.level_options = level_read[0]["level_options"]
               self.wave_options = level_read[0]["waves"]
               self.level_variables = level_read[0]["level_variables"]
               self.lawn = level_read[0]["lawn"]

               level_file.close()

     # Places something on a tile. If the item parameter is none, whatever is on the tile will be desroyed
     def tile_place(self, tile, item):
          tile_row = f"row{tile.split('x')[0]}"
          tile_column = int(tile.split('x')[1])

          self.lawn[tile_row][tile_column] = item

     # Summons new waves
     def new_wave(self):
          current_wave = 1
          max_waves = self.wave_options["number_of_waves"]

          for i in range(self.wave_options["number_of_waves"]):
               time.sleep(self.wave_options["time_before_zombies"])

               for i in range(len(self.wave_options["wave_zombies"][f"wave_{current_wave}"])):
                    zombies = self.wave_options["wave_zombies"][f"wave_{current_wave}"]

                    for j in range(len(zombies)):
                         zomb_type = zombies[j].split("@")[0]
                         # tile = zombies[j].split("@")[1]
                         # self.tile_place(zomb_type, tile)
               
               current_wave += 1
               
               if current_wave == max_waves:
                    self.level_status = Level_Status.WIN
                    return

               time.sleep(self.wave_options["time_between_waves"])

     # Moves zombies around.
     def move_zombies(self):
          with open(self.level_name, "r") as level:
               for i in range(len(self.lawn)):
                    i += 1

                    for j in range(len(self.lawn[f"row{i}"])):
                         if self.lawn[f"row{i}"][j].startswith("Zombie"):
                              self.lawn[f"row{i}"][j - 1] = self.lawn[f"row{i}"][j]
                              self.lawn[f"row{i}"][j] = f"column[{j}]"

                    time.sleep(3)

     # Shows the level stuff, like zombies, plants, etc
     def show_level(self):
          levelstr = ""

          for i in range(len(self.lawn)):
               i += 1
               levelstr += (f"Row {i}: " + str(self.lawn[f"row{i}"]) + "\n")

          print(levelstr)

     # Runs the level
     def run_level(self):
          processes = [threading.Thread(target=self.show_level()), threading.Thread(target=self.new_wave()), threading.Thread(target=self.move_zombies())]
          
          for process in processes:
               process.start()

          while self.level_status not in [Level_Status.WIN, Level_Status.FAIL]:
               if self.level_status in [Level_Status.WIN, Level_Status.FAIL]:
                    return

               self.tile_place("3x9", "Zombie")

               self.show_level()

               time.sleep(1)

# This is just for testing purpouses
level1 = Level_Runner("testlevel")