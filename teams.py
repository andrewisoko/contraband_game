import json
import random
from sign_up_process import *


class Teams:
  
  def __init__(self):
    
    self.player1 = None
    self.player2 = None
    self.float_player = None
    
    
    
  def __init__(self,sign_in: SignUpProcess):
    self.sign_in = sign_in
    
  def player_generator(self):
    
     with open ( "players.json","r") as file:
         self. player_json_list = json.load(file) # Json list instance
       
         player_list_values= [player_nickname for dictionaries in self.player_json_list for player_nickname in dictionaries.values()]
         
         self.player1 = player_list_values[-1]
      
       
         if self.player1 is not None:
         
           self.player1 = player_list_values[-2]
           self.player2 = player_list_values[-1]
           
           return f"player one {self.player1} and player two {self.player2}"
         
         else:
           return self.player1
    
  
  def Southern_team(self):
    
    """Southern team, it will return a random player of this team."""
    
    
    team1_list = [ {"name0": "Lupin"},
                  {"name1": "Bonnie"},
                  {"name2": "Clyde"},
                  {"name3":""},
                  {"name4":"C.Ponzi"}]
    
    
  
    return  f" this is what you got {team1_list}"

    # return random.choice(team1_list)
  
  
  def Northern_team(self):
    
    team2_list = [ {"name5": "Maradona"},
                  {"name6": "Berlusconi"},
                  {"name7": "S.Bankman-Fried"},
                  {"name8": ""}, 
                  {"name9": "Diddy"}]
    
    
    return random.choice(team2_list)
  
  
# teams = Teams()
# teams.player_generator()