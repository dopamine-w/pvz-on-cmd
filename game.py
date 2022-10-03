import json
import levels

# Basically just the game UI. Everything else will be implemented later
class Game:
     def __init__(self):
          self.menu()

     # UI for menu. Very simplistic
     def menu(self):
          response = input("Enter a number\n1: Play Game\n2: Exit\nResponse: ")

          if response == 2:
               return

          print(self.play_level("testlevel"))

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
          return levels.Level_Runner(level)

game1 = Game()
