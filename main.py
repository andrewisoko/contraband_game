from sign_up_process import SignUpProcess
from teams import Teams


test = SignUpProcess()

quick_start = input("Sign up = S / log in = L: ")

if quick_start == "S":  
 test.main_signup_process()
 
elif quick_start == "L":
   test.main_sign_in_process()
   
   players = Teams(test)
   print(players.player_generator())
   
   print(players.Southern_team())
   print(players.Northern_team())


