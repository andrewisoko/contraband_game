from src.signups import SignUpProcess
from src.teams import Teams
from src.gamesettings import GameSettings
from src.banks import Banks



def test_countries_personal_ba():
    
    """Testing the amount of each players'initial loan is equal to 300 million"""
    
    test_signups = SignUpProcess()
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
    
    test_signups = SignUpProcess()
    test_teams = Teams(test_signups)
    test_gamesettings = GameSettings(test_teams)
    test_banks_atm = Banks(test_signups,test_teams,test_gamesettings)
    
    test_banks_atm.northern_atm()
    test_banks_atm.southern_atm()
    
    test_north_atm = test_banks_atm.northern_atm_bankaccounts
    test_south_atm = test_banks_atm.southern_atm_bankaccounts
    
    united_atm_country_dict = test_north_atm
    united_atm_country_dict.update(test_south_atm)
    

