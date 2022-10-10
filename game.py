import json

# Basically just the game UI. Everything else will be implemented later
class Game:
     def __init__(self):
          self.menu()

     # UI for menu. Very simplistic
     def menu(self):
          response = input("""
______ _             _         _   _ _____   ______                _     _               _____         _____ ___  ________ _ 
| ___ \ |           | |       | | | /  ___| |___  /               | |   (_)          _  |  _  |       /  __ \|  \/  |  _  \ |
| |_/ / | __ _ _ __ | |_ ___  | | | \ `--.     / /  ___  _ __ ___ | |__  _  ___  ___(_) | | | |_ __   | /  \/| .  . | | | | |
|  __/| |/ _` | '_ \| __/ __| | | | |`--. \   / /  / _ \| '_ ` _ \| '_ \| |/ _ \/ __|   | | | | '_ \  | |    | |\/| | | | | |
| |   | | (_| | | | | |_\__ \ \ \_/ /\__/ / ./ /__| (_) | | | | | | |_) | |  __/\__ \_  \ \_/ / | | | | \__/\| |  | | |/ /|_|
\_|   |_|\__,_|_| |_|\__|___/  \___/\____/  \_____/\___/|_| |_| |_|_.__/|_|\___||___(_)  \___/|_| |_|  \____/\_|  |_/___/ (_)
\nEnter a number\n1: Play Game\n2: Exit\nResponse: """)

          if response == 2:
               _quit = input("Are you sure you want to quit? (y/n)\n")

               if _quit == "y": return
               elif _quit == "n": self.menu()
               else: 
                    print("Not a valid response.")
                    self.menu()

     def pick_save(self):
          pass

     def save_file(self, id):
          pass

     def open_save(self):
          pass

     def open_worlds(self):
          pass

     # Plays a level chosen through the worlds menu. Unfortunately, moving the zombies and making them eat plants, and etc
     # Hasn't been figured out yet, so for now we will just play the default level.
     def play_level(self, level):
          pass

game1 = Game()
