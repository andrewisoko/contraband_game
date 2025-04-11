import json
import random
from sign_up_process import *


class Teams:
  
  
  
  def __init__(self,sign_in: SignUpProcess):
      
      self.sign_in = sign_in
      self.player1 = None
      self.player2 = None
      self.player3 = None
      self.player4 = None
      self.team1_list = None
      self.team2_list = None
   
   
    
  def player_generator(self):
    
      """Dinamically assign players values"""

      with open("players.json", "r") as file:
          # Read Json file.
          self.player_json_list = json.load(file) 
          
      # A list of values from the players.json's dictionaries.
      self.player_list_values = [player_nickname for dictionaries in self.player_json_list for player_nickname in dictionaries.values()] # Appending json values on a list
      
      # Remove "player0" if it exists.
      if self.player_list_values[0] == "player0": 
          self.player_list_values.pop(0) 
      
      # Creating an index paired with a value for the first 4 items in the list.
      for index_list_value, value in enumerate(self.player_list_values[:4]): 
          
           # Assigning values to initialised instance attribute matched with index of list item.
          setattr(self, f"player{index_list_value + 1}", value)
      
      return "Player/s in the game :)"



  
  def southern_country_players(self) -> str:
    
    """Southern team, it will return a random player of this team."""
       
    
    self.team1_list = [ "Lupin", "Clyde","C.Ponzi"]
    
    # It is mandatory to have at least a player in the game, player1. the additional players will be replaced by other invented players if they do not partake in the game.
    if self.player1 is not None:
        self.team1_list.append(self.player1)
        
    # With the if statement containing else statement I have inverted the block structure pay attention.
    if self.player3 is None:
        self.team1_list.append("Bonnie")
    else:
        self.team1_list.append(self.player3)
    
  
    return random.choice(self.team1_list)



  
  def northern_country_players(self) -> str:
     
    """Northern team, it will return a random player of this team."""
     
    self.team2_list = ["Maradona","Berlusconi", "Diddy"]

    if self.player2 is None:
        self.team2_list.append("S.Bankman-Fried")
    else:
        self.team2_list.append(self.player2)
        
        
    if self.player4 is None:
        self.team2_list.append("Ted Bundy")
    else:
        self.team2_list.append(self.player4)
        

    return random.choice(self.team2_list)
  
  
