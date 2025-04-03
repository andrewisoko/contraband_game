import json
import random
from sign_up_process import *


class Teams:
  
  
  
  def __init__(self):
    
      self.player1 = None
      self.player2 = None
      self.player3 = None
      self.player4 = None
    
    
  def __init__(self,sign_in: SignUpProcess):
      self.sign_in = sign_in
    
  def player_generator(self):
    
      """Dinamically assign players values"""

      with open("players.json", "r") as file:
          # Read Json file
          self.player_json_list = json.load(file) 
          
      # A list of values from the players.json's dictionaries
      self.player_list_values = [player_nickname for dictionaries in self.player_json_list for player_nickname in dictionaries.values()] # Appending json values on a list
      
      # Remove "player0" if it exists
      if self.player_list_values[0] == "player0": 
          self.player_list_values.pop(0) 
      
      # Creating an index paired with a value for the first 4 items in the list
      for index_list_value, value in enumerate(self.player_list_values[:4]): 
          
           # Assigning values to initialised instance attribute matched with index of list item.
          setattr(self, f"player{index_list_value + 1}", value)
      
      return "Player/s in the game :)"


  
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
  
  
