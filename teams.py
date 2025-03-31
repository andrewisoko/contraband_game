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
    
  def player_data(self, nickname):
    
    """Store temporary sign-in data"""
    self._current_signin = nickname
    
  def player_generator(self):
    """Assign sign-in data to player slots"""
    if not self._current_signin:
        return "No sign-in data"
        
    if  hasattr(self, 'player1') and not self.player1:  # First player assignment
        self.player1 = self._current_signin
        self._current_signin = None  # Clear temporary storage
        return f"Player1: {self.player1}"
        
    if hasattr(self, 'player2') and not self.player2 and self._current_signin != self.player1:  # Second player assignment
        self.player2 = self._current_signin
        self._current_signin = None  # Clear temporary storage
        
        return f"Player1: {self.player1} and player2: {self.player2}"

    

     
      
    
    # with open ("json_user_data" ,"r") as file:
    #   self.json_user_data_instance = json.load(file)
      
    #   json_list_values = [json_val for dicts in self.json_user_data_instance for json_val in dicts.values()]
    
    
    
    
      
    
  
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