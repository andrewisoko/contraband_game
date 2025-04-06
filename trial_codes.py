# import json

   # def Northen_team_options(self):
        
    #     self.northen_player = self.teams.Northern_team_players()
    #     self.northen_inspection_process = self.The_inspector()
    #     self.northen_smuggler_attempt = self.The_smuggler()
        
        
    # def Southern_team_options(self):
        
    #     self.southern_player = self.teams.Southern_team_players()
    #     self.southern_inspector = self.The_inspector()
    #     self.southern_smuggle_attempt = self.The_smuggler() 
     
              
                      

    # def games(self):
        
    #     """General game setting"""
        
    #     for self.game in range(6,0,-1):
            
    #         print(f" {self.southern_player} from the SOUTHERN TEAM. It's your turn to smuggle")
    #         print(self.southern_smuggle_attempt)
            
    #         print(f"{self.northen_player} from the THE NORTHEN TEAM. it's your turn to inspect")
    #         print(self.northen_inspection_process)
            
    #         print(f"{self.game - 1} game(s) remaining.\n")
             
    #         print(f"{self.northen_player} from the SOUTHERN TEAM. It's your turn to smuggle")
    #         print(self.northen_smuggler_attempt)
            
    #         print(f"{self.southern_player}  from the THE NORTHEN TEAM. it's your turn to inspect")
    #         print(self.southern_inspector)
            
    #         print(f"{self.game - 1} game(s) remaining.\n")
     
            
    #     print("Game Over!")
    
    
    # sort out turn in games ✅
    # sort turn switch.
    # sort random players decision 
    # sort out comments
    
import random

mylist = ["banana", "cherry"]
previous = None

for _ in range(5):
    random.shuffle(mylist)
    while mylist[0] == previous:  # Ensure first element is different
        random.shuffle(mylist)
    previous = mylist[0]
    print(mylist)
    
   
   