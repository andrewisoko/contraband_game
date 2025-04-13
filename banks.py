
from game_settings import GameSettings
from sign_up_process import SignUpProcess
import random
from teams import Teams

class Banks:
    
    def __init__(self, countries_players: SignUpProcess , team_list: Teams, game_settings: GameSettings):
        
        self.countries_players = countries_players
        self.team_list = team_list
        self.game_settings = game_settings
        
        self.outside_the_country_ba = None
        self.personal_bank_account = None
        

        
    
    def southern_country_atm(self):
        
        # getting the northern player's list
        self.northern_bank_players = self.team_list.northern_country_players()
        
        # Placing each player's names by referencing their list position with index.
        self.players_bank_account = {self.northern_bank_players[0]:300_000_000,
                                     self.northern_bank_players[1]:300_000_000,
                                     self.northern_bank_players[2]:300_000_000,
                                     self.northern_bank_players[3]:300_000_000,
                                     self.northern_bank_players[4]:300_000_000
                                     }
         
        # Gathering all the values in the dictionary
        self.bankaccounts_values = self.players_bank_account.values()
        
        #Total amount of the Southern country.
        self.total_northern_players_ba = sum(self.bankaccounts_values) 
        
        
        if  self.game_settings.smuggler == "Maradona" and self.game_settings.sec_amount_win is True:
            
            #This is the value of the dictionary. The integer
            current_val = self.players_bank_account[self.northern_bank_players[0]]
            
            #This is the security amount deriving from the game
            ammount_won = self.game_settings.security_amount
            
            # Assigning a new value by adding the previous value with the security amount
            self.players_bank_account[self.northern_bank_players[0]] = current_val + ammount_won
            
            
    
    
       
        
        # return self.outside_the_country_ba
        #to create money update after each round.
        
        # print(f'{sum(self.bank_list_values):,}')

sign_ins = SignUpProcess()      
teams_list = Teams(sign_ins)
gameset = GameSettings(teams_list)
banks = Banks(sign_ins,teams_list,gameset)

    
banks.southern_country_atm()

    
