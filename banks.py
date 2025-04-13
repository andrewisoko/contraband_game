
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
        

        
    
    def northern_bankaccount_third_country(self):
        
        """Returns the total ammount of money obtained from the entire northen country team during the game"""
        
        # getting the northern player's list
        self.northern_bank_players = self.team_list.northern_country_players()
        
        # Placing each player's names by referencing their list position with index.
        self.players_bank_account = {self.northern_bank_players[0]:300_000_000,
                                     self.northern_bank_players[1]:300_000_000,
                                     self.northern_bank_players[2]:300_000_000,
                                     self.northern_bank_players[3]:300_000_000,
                                     self.northern_bank_players[4]:300_000_000
                                     }
         
        # Gathering all the values in the dictionary.
        self.bankaccounts_values = self.players_bank_account.values()
        
        # Total amount of the Southern country.
        self.total_money_northen_country_atm = sum(self.bankaccounts_values) 
        
        return self.total_money_northen_country_atm
        
        
        
    def money_update_as_southern_smuggler(self): 
        
        """Uptdates bank account of each northern country players based on outcome of the game when role is of a smuggler.""" 
             
             
        # Matching the parameter with the keys of the players bank account dictionary for then using the variable of the loop as representation of the name string.
        for name_key in self.players_bank_account.keys():
            
            # Scenario where the smuggler has no money in the trunk and inspector calls doubt.
            if  self.game_settings.smuggler == name_key and self.game_settings.sec_amount_win is True:
                    
                #This is the value of the dictionary. The integer.
                current_val = self.players_bank_account[name_key]
                
                #This is the security amount deriving from the game.
                ammount_won = self.game_settings.security_amount
                
                # Assigning a new value by adding the previous value with the security amount.
                self.players_bank_account[name_key] = current_val + ammount_won
             
             #Scenario where inspector calls DOUBT and it matches or exceeds amount of money inside the smuggler's trunk. 
            elif self.game_settings.smuggler == name_key and self.game_settings.inspector_win is True and self.game_settings.smuggler_win is False: 
            
                current_val = self.players_bank_account[name_key]
                
                # This is the smuggling amount deriving from the game.
                ammount_won = self.game_settings.smuggling_amount
                
                # Assigning a new value by adding the previous value with the smuggling amount.
                self.players_bank_account[name_key] = current_val - ammount_won
                
            # Scenario where inspector calls DOUBT but smuggler's money inside the trunk exceed the amount declared from inspector.
            elif self.game_settings.smuggler == name_key and self.game_settings.smuggler_win is True and self.game_settings.sec_amount_win is True: 
                
                current_val = self.players_bank_account[name_key]
                
                ammount_won = self.game_settings.smuggling_amount
                security_ammount_won = self.game_settings.security_amount
                
                
                # Assigning a new value by adding the previous value with the smuggling amount.
                self.players_bank_account[name_key] = current_val + ammount_won + security_ammount_won
            
            # Scenario where inspector calls PASS but smuggler carries money inside the trunk.   
            elif self.game_settings.smuggler == name_key and self.game_settings.smuggler_win is True and self.game_settings.inspector_win is False:
                
                current_val = self.players_bank_account[name_key]
        
                ammount_won = self.game_settings.smuggling_amount
                
                # Assigning a new value by adding the previous value with the smuggling amount.
                self.players_bank_account[name_key] = current_val + ammount_won 
            else:
                pass  
        
    
    def money_update_as_southern_inspector(self): 
        
        
        """Uptdates bank account of each northern country players based on outcome of the game when role is of a inspector.""" 
        
                # Matching the parameter with the keys of the players bank account dictionary for then using the variable of the loop as representation of the name string.
        for name_key in self.players_bank_account.keys():
            
            if  self.game_settings.inspector == name_key and self.game_settings.sec_amount_win is True:
                    
                #This is the value of the dictionary. The integer.
                current_val = self.players_bank_account[name_key]
                
                #This is the security amount deriving from the game.
                ammount_won = self.game_settings.security_amount
                
                # Assigning a new value by adding the previous value with the security amount.
                self.players_bank_account[name_key] = current_val - ammount_won
                
            elif self.game_settings.inspector == name_key and self.game_settings.inspector_win is True and self.game_settings.smuggler_win is False: 
            
                current_val = self.players_bank_account[name_key]
                
                # This is the smuggling amount deriving from the game.
                ammount_won = self.game_settings.smuggling_amount
                
                # Assigning a new value by adding the previous value with the smuggling amount.
                self.players_bank_account[name_key] = current_val + ammount_won
                
            
            elif self.game_settings.inspector == name_key and self.game_settings.smuggler_win is True and self.game_settings.sec_amount_win is True: 
                
                current_val = self.players_bank_account[name_key]
                
                ammount_won = self.game_settings.smuggling_amount
                security_ammount_won = self.game_settings.security_amount
                
                
                # Assigning a new value by adding the previous value with the smuggling amount.
                self.players_bank_account[name_key] = current_val - ammount_won - security_ammount_won
            
            # Condition occurring in a declared PASS scenario.   
            elif self.game_settings.inspector == name_key and self.game_settings.smuggler_win is True and self.game_settings.inspector_win is False:
                
                current_val = self.players_bank_account[name_key]
        
                ammount_won = self.game_settings.smuggling_amount
                
                # Assigning a new value by adding the previous value with the smuggling amount.
                self.players_bank_account[name_key] = current_val - ammount_won 
            else:
                pass  
        
        
   
        
        
           
             
       
    
    
    

sign_ins = SignUpProcess()      
teams_list = Teams(sign_ins)
gameset = GameSettings(teams_list)
banks = Banks(sign_ins,teams_list,gameset)

    
banks.northern_bankaccount_third_country()

    
