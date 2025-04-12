
from game_settings import GameSettings
from sign_up_process import SignUpProcess
import random
from teams import Teams

class Banks:
    
    def __init__(self, countries_players: SignUpProcess , team_list: Teams):
        
        self.countries_players = countries_players
        self.team_list = team_list
        
        self.outside_the_country_ba = None
        self.personal_bank_account = None

        
    
    def third_country_bank_accounts(self):
        
        # getting the northern player's list
        self.northern_bank_players = self.team_list.northern_country_players()
        
        self.players_bank_account = [{self.northern_bank_players[0]:300_000_000},
                                     {self.northern_bank_players[1]:300_000_000},
                                     {self.northern_bank_players[2]:300_000_000},
                                     {self.northern_bank_players[3]:300_000_000},
                                     {self.northern_bank_players[4]:300_000_000}]
         
        self.total_northern_players_ba = [tot_amount for players_bank_account_dict in self.players_bank_account for tot_amount in players_bank_account_dict.values()] 
        
        
        #to create money update after each round.
        
        # print(f'{sum(self.total_northern_players_ba):,}')

sign_ins = SignUpProcess()      
teams_list = Teams(sign_ins)
banks = Banks(sign_ins,teams_list)

    
banks.third_country_bank_accounts()

    
