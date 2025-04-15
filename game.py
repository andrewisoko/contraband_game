from teams import Teams
from sign_up_process import SignUpProcess
from game_settings import GameSettings
from banks import Banks
import random
import time


class Game():
    
       def games(self,sign_in):
    
        """General game setting, bare in mind the money are smuggled with a trunk but it is not in this game"""
       # Bare in mind the turn in a game will be 4 since both country wil be inspector and smuggler in the round but it should be two turns for one game.
        for self.game in range(2,0,-1):
            
            # Teams class instance where the log in of the gamer is passed as an argument
            teams_instance = Teams(sign_in)
            
            # Generating players from gamer user credentials. 1 if one player wants to play or multiple.
            teams_instance.player_generator()
            
            # adding trams as argument so players can be accessed in the class
            game_settings_instance = GameSettings(teams_instance)
            
            # Initialising the class on the instance variable which will generate a random player from the southern country. Now the instance variable will have the same value throughout the all functions of the class if present in the following call of a function.
            game_settings_instance.smuggler = random.choice(teams_instance.southern_country_players())
            print(f" The smuggler of the Southern team is: {game_settings_instance.smuggler}")
            
            game_settings_instance.inspector = random.choice(teams_instance.northern_country_players())
            print(f" The inspector of the Northern team is: { game_settings_instance.inspector}")
            
            game_settings_instance.the_smuggler()
            game_settings_instance.the_inspector()
            
            
            game_settings_instance.smuggler = random.choice(teams_instance.northern_country_players())
            print(f" the smuggler of the Northern team is { game_settings_instance.smuggler}")
            
            game_settings_instance.inspector = random.choice(teams_instance.southern_country_players())
            print(f" the inspector of the Southern team is: { game_settings_instance.inspector}")
            
            game_settings_instance.the_smuggler()
            game_settings_instance.the_inspector()
            
            print(f"{self.game - 1} game(s) remaining.\n")
         
        
        
        print("Game Over!")
        

sign_up = SignUpProcess()
teams = Teams(sign_up)
gameset = GameSettings(teams)
game = Game()
game.games(sign_up)