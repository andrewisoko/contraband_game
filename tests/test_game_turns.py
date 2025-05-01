from src.signups import SignUpProcess
from src.teams import Teams
from src.gamesettings import GameSettings
from src.banks import Banks
from src.game import Game


def test_game_turns():
    
    test_signups = SignUpProcess()
    test_teams = Teams(test_signups)
    test_gamesettings = GameSettings(test_teams)
    test_banks_atm = Banks(test_signups,test_teams,test_gamesettings)
    test_game = Game()
    
    test_game.games(test_signups)
    assert test_game.game <= 25