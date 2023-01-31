import json
from enum import Enum
from EntityCode import EntityCode, Range

class LevelStatus(Enum):
     LOSE           = 0
     WIN            = 1
     UNDECIDED      = 2

class LevelRunner:
     def __init__(self, path):
          self.path = f"levels/{path}.json"

          with open(self.path, "r") as f:
               self.level = json.load(f)
               
               self.level_settings      = self.level[0]["LevelSettings"]
               self.level_variables     = self.level[0]["LevelVariables"]
               self.lawn                = self.level[0]["Lawn"]
               self.level_status        = LevelStatus.UNDECIDED

     def __repr__(self):
          return f"Level Settings: {self.level_settings}\nLevel Variables: {self.level_variables}\nLawn: {self.lawn}"

     def place(self, _class, tile):
          row = tile.split("x")[0]
          column = tile.split("x")[1]

          self.lawn[row[f"row{row}"]][int(column)] = {"name": _class.name, "attack": _class.attack, "defense": _class.defense}

     def run_entity_func(self, func):
          func = func.split(",")
          entity_code = func[0]
          entity = EntityCode(self.level)

          match entity_code:
               case "increase_sun":
                    entity.increase_sun(int(func[1]))
               case "attack_zombie":
                    match func:
                         case Range.LANE.__name__:
                              entity.attack_zombie(Range.LANE, int(func[2]))
                         case Range.LOBBED.__name__:
                              entity.attack_zombie(Range.LOBBED, int(func[2]))
                         case Range.THREEBYTHREE.__name__:
                              entity.attack_zombie(Range.THREEBYTHREE, int(func[2]))
                         case Range.TILE.__name__:
                              entity.attack_zombie(Range.TILE, int(func[2]))
                         case Range.BACK.__name__:
                              entity.attack_zombie(Range.BACK, int(func[2]))
                         case Range.FRONTANDBACK.__name__:
                              entity.attack_zombie(Range.FRONTANDBACK, int(func[2]))
                         case Range.LOBBED_FRONTANDBACK.__name__:
                              entity.attack_zombie(Range.LOBBED_FRONTANDBACK, int(func[2]))
                         case Range.CLOSE.__name__:
                              entity.attack_plant(Range.LOBBED_FRONTANDBACK, int(func[2]))


     def show_level(self):
          row = ""
          i = 1

          print(f"Plants: {self.level_variables['plants']}")

          for _row in self.lawn:
               row += f"Row {i}: ["
               for grid_item in _row:
                    if grid_item == None:
                         row += "\' \'"
                    
                    row += grid_item

          print("==================================================\n")

     def run_level(self):
          while self.level_status == LevelStatus.UNDECIDED:
               self.show_level()

               command = input("> ")

               if command.startswith("restart"):
                    self.run_level()
               
               elif command.startswith("plant"):
                    command_split = command.split(" ")

                    self.place(command_split[1], command_split[3])

               for i in range(5):
                    for j in range(1,10):
                         if self.lawn[f"row{i + 1}"][j] != None:
                            for k in self.lawn[f"row{i + 1}"][j][0]:
                              if self.lawn[f"row{i + 1}"][j][0][k]["class"] == "plant":
                                   self.run_entity_func(self.lawn[f"row{i + 1}"][j][0][k]["on_planted_func"])

               print("==================================================\n")

new_level_runner = LevelRunner("test")
new_level_runner.run_level()
new_level_runner.show_level()