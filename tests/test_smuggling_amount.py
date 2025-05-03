from src.signups import SignUps
from src.teams import Teams
from src.gamesettings import GameSettings



def test_smuggling_amount():
    
    """Testing the smuggling amount of the smuggler does not exceed 100 million"""
    
    test_signups = SignUps()
    test_teams = Teams(test_signups)
    test_gamesettings = GameSettings(test_teams)

    test_gamesettings.smuggler = "test player"
    
    test_gamesettings.the_smuggler()
    assert test_gamesettings.smuggling_amount <= 100_000_000
 