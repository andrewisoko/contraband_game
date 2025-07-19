import json
from   .signups import *
import pkg_resources



class Teams:
  
  
  
  def __init__(self,sign_in: SignUps):
      
      self.sign_in = sign_in
      self.player1 = None
      self.player2 = None
      self.player3 = None
      self.player4 = None
      
      
   
   
    
  def player_generator(self):
    
      """Dinamically assign players values"""
      
      user_players = pkg_resources.resource_filename('contraband_game', 'data/players.json')

      with open(user_players, "r") as file:
        
          self.user_players_json = json.load(file) 
   
      self.player_values = [player_nickname for dictionaries in self.user_players_json for player_nickname in dictionaries.values()] # Appending json values on a list
      
      if self.player_values[0] == "player0": 
          self.player_values.pop(0) 
      
     
      for index_list_value, value in enumerate(self.player_values[ :4]): 
          
          setattr(self, f"player{index_list_value + 1}", value)
      
      return "Player/s in the game :)"



  
  def southern_country_players(self) -> list:
    
    """It returns a list containing the southern country's players"""
       
    
    team1 = [ "Lupin", "Clyde","Charles Ponzi"]
    
    # It is mandatory to have at least a player in the game, player1. the additional players will be replaced by other invented players if they do not partake in the game.
    if self.player1 is None:
      team1.append("Jordan Belfort")
    else:
        team1.append(self.player1)
        
    # With the if statement containing else statement I have inverted the block structure pay attention.
    if self.player3 is None:
        team1.append("Bonnie")
    else:
        team1.append(self.player3)
    
  
    return team1



  
  def northern_country_players(self) -> list:
     
    """It returns a list containing the northern country's players"""
       
     
    team2 = ["Maradona","Berlusconi", "Diddy"]

    if self.player2 is None:
        team2.append("S.Bankman-Fried")
    else:
        team2.append(self.player2)
        
        
    if self.player4 is None:
        team2.append("Ted Bundy")
    else:
        team2.append(self.player4)
        

    return team2
  
  
