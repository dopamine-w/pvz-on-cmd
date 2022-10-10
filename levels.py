import time
import json
import threading
from enum import Enum
import plants, zombies

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
          
          with open(f"{self.level_name}", "r") as level_file:
               level_read = json.load(level_file)

               self.level_options = level_read[0]["level_options"]
               self.wave_options = level_read[0]["waves"]
               self.level_variables = level_read[0]["level_variables"]
               self.lawn = level_read[0]["lawn"]

               level_file.close()

          self.run_level()

     def __repr__(self):
          return self.show_level()

     # Places something on a tile. If the item parameter is none, whatever is on the tile will be desroyed
     def tile_place(self, tile, item, _type = None):
          tile_row = f"row{tile.split('x')[0]}"
          tile_column = int(tile.split('x')[1])

          if type(item) == plants.Plant:
               plant_data = {
                    item.name: {
                         "health": item.health,
                         "attack": item.attack
                    }
               }

               self.lawn[f"row{tile_row}"][f"col{tile_column}"]["plants"].update(plant_data)
          
          if type(item) == zombies.Zombie:
               zombie_data = {
                    item.name: {
                         "health": item.health,
                         "attack": item.attack
                    }
               }

               self.lawn[f"row{tile_row}"][f"col{tile_column}"]["zombie"].update(zombie_data)

          if _type != None:
               self.lawn[f"row{tile_row}"][f"col{tile_column}"][_type].update(item)

     # Summons new waves
     def new_wave(self):
          current_wave = 1
          max_waves = self.wave_options["number_of_waves"]
          waves = self.wave_options["wave_zombies"]

          while current_wave != max_waves:
               for j in waves[f"wave_{current_wave}"]:
                    tile = waves[f"wave_{current_wave}"][j]["tile"]

                    self.tile_place(tile, j)

     # Moves zombies around.
     def move_zombie(self):
          for i in range(len(self.lawn)):
               i += 1
               if i == 10: break

               for j in range(len(self.lawn[f"row{i}"])):
                    j += 1
                    if j == 10: break

                    for zombie in self.lawn[f"row{i}"][f"col{j}"]["zombie"]:
                         self.tile_place(f"{i}x{j}", zombie, "zombie")
                         del self.lawn[f"row{i}"][f"col{j}"]["zombie"][zombie]

               time.sleep(3)

     # Shows the level stuff, like zombies, plants, etc
     def show_level(self):
          levelstr = ""
          levelarr: list = ["lawnmower"]
          temp_arr = []

          for i in range(len(self.lawn)):
               i += 1

               for j in range(len(self.lawn[f"row{i}"])):
                    j += 1

                    if j == 10: break

                    if "pumpkin" in self.lawn[f"row{i}"][f"col{j}"]["plants"]:
                         for k in self.lawn[f"row{i}"][f"col{j}"]["plants"]:
                              if k != "pumpkin":
                                   levelarr.append(f"({k})")

                    if (len(self.lawn[f"row{i}"][f"col{j}"]["plants"]) == 0) and len(self.lawn[f"row{i}"][f"col{j}"]["zombie"]) == 0:
                         levelarr.append(f"col{j}")

                    elif (len(self.lawn[f"row{i}"][f"col{j}"]["plants"]) == 0) and (len(self.lawn[f"row{i}"][f"col{j}"]["zombie"]) > 0):
                         for k in self.lawn[f"row{i}"][f"col{j}"]["zombie"]:
                              temp_arr.append(k)

                              levelarr.append(temp_arr)

               levelstr += (f"Row {i}: " + str(levelarr) + "\n")
               levelarr = ["lawnmower"]

          print(levelstr)

     # Runs the level
     def run_level(self):
          processes = [threading.Thread(target=self.show_level()), threading.Thread(target=self.new_wave())]
          
          for process in processes:
               process.start()

          while self.level_status not in [Level_Status.WIN, Level_Status.FAIL]:
               if self.level_status in [Level_Status.WIN, Level_Status.FAIL]:
                    return

               self.show_level()
               self.new_wave()

               time.sleep(1)

# This is just for testing purpouses
level1 = Level_Runner("testlevel")