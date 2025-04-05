from sign_up_process import SignUpProcess
from teams import Teams
from game_settings import GameSettings


test = SignUpProcess()

quick_start = input("Sign up = S / log in = L: ")

if quick_start == "S":  
 test.main_signup_process()
 
elif quick_start == "L":
   test.main_sign_in_process()
   
   teams_instance = Teams(test)
   teams_instance.player_generator()

   game_settings_instance = GameSettings(teams_instance)
   game_settings_instance.assign_roles()

   print(f"The Smuggler is: {game_settings_instance.smuggler}")
   print(f"The Inspector is: {game_settings_instance.inspector}")

   game_settings_instance.the_smuggler()
   game_settings_instance.the_inspector()
   


