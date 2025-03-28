from sign_up_process import SignUpProcess

test = SignUpProcess()

quick_start = input("SIng up = S / log in = L: ")

if quick_start == "S":
 test.main_signup_process()
 
elif quick_start == "L":
   test.sign_in()
