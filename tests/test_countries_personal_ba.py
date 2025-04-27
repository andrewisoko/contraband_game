
from src.signups import SignUpProcess
from src.teams import Teams
from src.gamesettings import GameSettings
from src.banks import Banks



def test_countries_personal_ba():
    
    test_signups = SignUpProcess()
    test_teams = Teams(test_signups)
    test_gamesettings = GameSettings(test_teams)
    test_banks = Banks(test_signups,test_teams,test_gamesettings)
    
    test_banks.northern_bankaccount_third_country()
    test_banks.southern_bankaccount_third_country()
    
    test_north_ba = test_banks.northern_country_personal_bankaccounts
    test_south_ba = test_banks.southern_country_personal_bankaccounts
    
    united_country_dict = test_north_ba
    united_country_dict.update(test_south_ba)
    
    for key_names in united_country_dict.keys():
        assert united_country_dict[key_names] == 200_000_000
 
   
    
    
    
    
    
    
    
    
    