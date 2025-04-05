from sign_up_process import SignUpProcess
from teams import Teams
from game_settings import GameSettings


test = SignUpProcess()

quick_start = input("Sign up = S / log in = L: ")

if quick_start == "S":  
 test.main_signup_process()
 
elif quick_start == "L":
   test.main_sign_in_process()
   
   teams = Teams(test)
   print(teams.player_generator())
   teams.Southern_team_players()
   teams.Northern_team_players()
   
   


