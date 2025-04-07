from sign_up_process import SignUpProcess
from teams import Teams
from game_settings import GameSettings


test = SignUpProcess()

quick_start = input("Sign up = S / log in = L: ")

if quick_start == "S": 
   # This will print the sign up process. 
 test.main_signup_process()
 
elif quick_start == "L":
   #This will print the log in process.
   test.main_sign_in_process()
   
   teams_instance = Teams(test)
   # Creting user/players from the sign in process
   teams_instance.player_generator()

# It is adviced to try the latest updates in the game_setting.py module


