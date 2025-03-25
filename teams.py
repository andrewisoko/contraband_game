import random

class Teams:
  
  def Southern_team(self):
    
    """Southern team, it will return a random player of this team."""
    
    
    
    team1_list = [ {"name0": "Lupin"},
                  {"name1": "Bonnie"},
                  {"name2": "Clyde"},
                  {"name3":self.name},
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
  