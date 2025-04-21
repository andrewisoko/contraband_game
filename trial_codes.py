# import json

import random

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
    
    
# import random

# southern_player = "Southside"
# northern_player = "Northside"

# mylist = ["Smuggler", "Inspector"]
# previous = None

# for _ in range(10):
    
#     while mylist[0] == previous:  # Ensure first element is different
#         random.shuffle(mylist)
#         if mylist[0] == "Smuggler":
                
#             smuggler = southern_player
#             inspector = northern_player
#             print(smuggler)
            
#         else:
#             smuggler = northern_player
#             inspector = southern_player
#             print(smuggler)
            
#     previous = mylist[0]
    
#     print(mylist)

 
# southern_player = "South"
# northern_player = "North"
# previous_player = northern_player

# for _ in range(5):
            
#     smuggler = northern_player if previous_player == southern_player else southern_player 
#     inspector = northern_player if smuggler == southern_player else southern_player
#     previous_player = southern_player if previous_player == northern_player else northern_player

# print(f"The Smuggler is: {smuggler} and the inspector is: {inspector}")


    # sort out turn in games ✅
    # sort turn switch. ✅
    # sort random players decision ✅
    # sort out comments ✅
    # sort out your test.py
    
    # check name key it could be an issue.


    # self.bankaccounts_list_values = [tot_amount for players_bank_account_dict in self.players_bank_account for tot_amount in players_bank_account_dict.values()] 
    # prova = self.players_bank_account[0]
        
    #     # prova1 will become the new value 
    #     prova1 = prova['Berlusconi'] - 1 # minus or plus
        
    #     self.total_northern_players_ba = sum(self.bankaccounts_list_values) 
        
    #     print(prova1)
    

# what worked in game.py:

# sign_up = SignUpProcess()
# teams = Teams(sign_up)
# gameset = GameSettings(teams)
# game = Game()
# game.games(sign_up)
# print(game.game_aftermath())