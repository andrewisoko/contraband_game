from src.signups import SignUps
from src.teams import Teams
from src.gamesettings import GameSettings
from src.banks import Banks
import random
import pytest



def test_countries_personal_ba():
    
    """Testing the amount of each players'initial loan is equal to 300 million"""
    
    test_signups = SignUps()
    test_teams = Teams(test_signups)
    test_gamesettings = GameSettings(test_teams)
    test_banks_atm = Banks(test_signups,test_teams,test_gamesettings)
    
    test_banks_atm.northern_atm()
    test_banks_atm.southern_atm()
    
    test_north_atm = test_banks_atm.northern_atm_bankaccounts
    test_south_atm = test_banks_atm.southern_atm_bankaccounts
    
    united_atm_country_dict = test_north_atm
    united_atm_country_dict.update(test_south_atm)
    
    for key_names in united_atm_country_dict.keys():
        assert united_atm_country_dict[key_names] == 300_000_000
 
   
def test_smuggling_amount_from_bank():
    
    """Testing withdrawal from atm does not exceed the amount of 100 million"""
    
    player_name_list = []
    united_country_players = []
    
    test_signups = SignUps()
    test_teams = Teams(test_signups)
    test_gamesettings = GameSettings(test_teams)
    test_banks_atm = Banks(test_signups,test_teams,test_gamesettings)
    
    northern_players_list = test_teams.northern_country_players()
    southern_players_list = test_teams.southern_country_players()
    
    for southern_players in southern_players_list:
      united_country_players.append(southern_players)
      
    for northern_players in northern_players_list:
        united_country_players.append(northern_players)

    for name_players in united_country_players:
        player_name_list.append(name_players)
        
    test_gamesettings.smuggler = random.choice(player_name_list)
    smuggling_amount_limit = range(1,100_000_000)
    initial_players_loaned_amount =  300_000_000
    
    test_gamesettings.the_smuggler()
    
    if test_gamesettings.smuggler in northern_players_list:
        test_banks_atm.northern_atm()
        
        if initial_players_loaned_amount - test_banks_atm.northern_atm_bankaccounts[test_gamesettings.smuggler]  == test_gamesettings.smuggling_amount:
           assert test_gamesettings.smuggling_amount in smuggling_amount_limit
        
        else:
            print(f"{test_gamesettings.smuggling_amount:,} Smuggling amount exceeded the settled limit")
        
    
    else:
        test_banks_atm.southern_atm()
        
        if initial_players_loaned_amount - test_banks_atm.southern_atm_bankaccounts[test_gamesettings.smuggler]  == test_gamesettings.smuggling_amount:
           assert test_gamesettings.smuggling_amount in smuggling_amount_limit
        
        else:
            print(f"{test_gamesettings.smuggling_amount:,} Smuggling amount exceeded the settled limit")
    
 



           
    

