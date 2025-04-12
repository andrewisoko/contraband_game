from teams import Teams
from getpass import getpass
import random
from sign_up_process import SignUpProcess
import time


class GameSettings:
    
    
    def __init__(self,teams:Teams):
        
        self.teams = teams
        self.smuggling_amount = None
        self.inspector = None
        self.smuggler = None
        self.security_amount = None
        self.game = None
        
       
       


    
    
    def doubt_declaration(self):
        
        """All the scenarios occurring from a doubt declaration"""
        
        while True:
             
            try:
                # If it's the default player turn a random statement amount will be generated.
                if self.inspector != self.teams.player1 and self.inspector != self.teams.player2 and self.inspector != self.teams.player3 and self. inspector!= self.teams.player4:
                    self.statement_amount = float(random.randrange(1,100_000_000))
                    
                    self.security_amount = self.statement_amount / 2
                    
                    # Some suspance on the decision.
                    time.sleep(15)
                    print(f"the inspector declared the amount is equal to {self.statement_amount}£ inside the trunk")
                    break
                else:
                    self.statement_amount = float(input("AMOUNT: "))
                    print(f"the inspector declared the amount is equal to {self.smuggling_amount}£ inside the trunk")
                    
                    # the security amount is equal to half of the statement amount. this gets temporary withdrawn from the inspector outside bank account, and given to the smuggler certain circumstances.
                    self.security_amount = self.statement_amount / 2
                    
                    # the statement amount shoudn't exceed 100milion since that is the limit of the money allowed inside the trunk.
                    if self.statement_amount >= 100_000_000:
                        break
                    else:
                        print("Invalid amount")
            except:
                print("Invalid input. Please enter a numeric value.")
                
         # If smuggler has no money inside the trunk and the statement amount from the inspector exceeds the empty trunk the smuggler wins and gets the security amount        
        if self.smuggling_amount == 0 and self.statement_amount > 0:
            print(f"The smuggler {self.smuggler} obtained {self.security_amount:,} £ of security amount.")
            
        # If statement amount higher or equal the smuggler amount the inspector wins  
        elif self.statement_amount >= self.smuggling_amount:
            print(f"Smuggling attempt flopped!!! The inspector {self.inspector} obtained {self.smuggling_amount:,} £ into his/her outside country's bank account.")
                    
        # If the statement amount is lower than the money inside the trunk from the smuggler, The latter wins and carries both the money in the trunk and security amount of the inspector
        elif self.statement_amount < self.smuggling_amount:
            print(f"{self.smuggler} succesfully smuggled {self.smuggling_amount:,} £ on his/her outside country's bank account plus {self.security_amount:,} from the inspector!!!")
        else:
            pass
   
      
    
    def pass_declaration(self):
        
        """All the scenarios occurring from a pass declaration"""

        print(f"Inspector declared PASS, the smuggler carried {self.smuggling_amount:,} £")
        
        # this is the only stalemate scenario
        if self.smuggling_amount == 0:
            print(f"No money has been smuggled to the outside bank account.")
            
         # if pass is called and the smuggler has money inside the trunk the smuggler wins    
        else:
            print(f"The smuggler has been able to carry {self.smuggling_amount:,} £")
   
           
            
    def the_inspector(self):
        
        """Inspector's action"""
        
        default_player_choice = ["PASS","DOUBT"]
            
        # The if statement gives all the delfault players in the game a option between pass and doubt.
        if self.inspector != self.teams.player1 and self.inspector != self.teams.player2 and self.inspector != self.teams.player3 and self.inspector != self.teams.player4 :
            self.inspector_action = random.choice(default_player_choice)
    
            
            # slowing down the pace of the output
            time.sleep(15)
            print("Call PASS if you believe the smuggler is carrying no money. Insert DOUBT if you believe money are carried by the smuggler")
            
            # Adding a bit of suspance before the decision.
            time.sleep(5)
            print(self.inspector_action) 
        else:
            # Otherwise the the user/player inserts the key words.
            self.inspector_action = input(f"{self.inspector} insert PASS if you believe the smuggler is carrying no money. Insert DOUBT if you believe money are carried by the smuggler: ")
            # SORT OUT THIS IF STATEMENT LOGIC
    
        while True:
            
            if self.inspector_action == "PASS":
                time.sleep(5)
                self.pass_declaration()
                break
                
            elif self.inspector_action == "DOUBT":
                time.sleep(5)
                self.doubt_declaration()
                break
            
            else:
                self.inspector_action = input("Invalid input. Please try again:  ")
                print(self.inspector_action)

   
   
    def the_smuggler(self):
        
        """The smuggler's action"""
        
        while True: 
            try:
                # The if statement declares that every non user/player place their amount with the random function.
                if self.smuggler != self.teams.player1 and self.smuggler != self.teams.player2 and self.smuggler != self.teams.player3 and self.smuggler != self.teams.player4:
                    self.smuggling_amount = float(random.randrange(1,100_000_000))
                    
                    # delayed output to make it more fluid
                    time.sleep(10)
                    
                    # The print statement masks the smuggling amount of the default player
                    print("*************")
                    
                    print(f" {self.smuggler}'s turn is over")
                    break
                else:
                # the getpass method is needed to hide the amount placed in the trunk by the smuggler.
                    self.smuggling_amount = float(getpass(f"{self.smuggler} place your amount in the trunk. The max is 100,000,000 £: "))
                    
                    # the amount in the trunk has to be 100 million £ maximum
                    if self.smuggling_amount <= 100_000_000:
                        print(f" {self.smuggler} turn is over")
                        break  
                    else:
                        print("Invalid amount. Please try again.")
            except:
                print("Invalid input. Please enter a numeric value.")
            
                
 
    def games(self,countries_players):
    
        """General game setting, bare in mmind the money are smuggled with a trunk but it is not in this game"""
       # Bare in mind the turn in a game will be 4 since both country wil be inspector and smuggler in the round but it should be two turns for one game.
        for self.game in range(2,0,-1):
            
            # Teams class instance where the log in of the gamer is passed as an argument
            teams_instance = Teams(countries_players)
            
            # Generating players from gamer user credentials. 1 if one player wants to play or multiple.
            teams_instance.player_generator()
            
            # adding trams as argument so players can be accessed in the class
            game_settings_instance = GameSettings(teams_instance)
            
            # Initialising the class on the instance variable which will generate a random player from the southern country. Now the instance variable will have the same value throughout the all functions of the class if present in the following call of a function.
            game_settings_instance.smuggler = random.choice(teams_instance.southern_country_players())
            print(f" The smuggler of the Southern team is: {game_settings_instance.smuggler}")
            
            game_settings_instance.inspector = random.choice(teams_instance.northern_country_players())
            print(f" The inspector of the Northern team is: { game_settings_instance.inspector}")
            
            game_settings_instance.the_smuggler()
            game_settings_instance.the_inspector()
            
            
            game_settings_instance.smuggler = random.choice(teams_instance.northern_country_players())
            print(f" the smuggler of the Northern team is { game_settings_instance.smuggler}")
            
            game_settings_instance.inspector = random.choice(teams_instance.southern_country_players())
            print(f" the inspector of the Southern team is: { game_settings_instance.inspector}")
            
            game_settings_instance.the_smuggler()
            game_settings_instance.the_inspector()
            
            print(f"{self.game - 1} game(s) remaining.\n")
        
        
        print("Game Over!")
    
           

# this object creates the current nicknames and code for playing the game . Nickname is used for identify the user/player in the game.              
# logged_in_players = SignUpProcess().main_sign_in_process()

# # the class teams contain the two countries. logged in player as an argument is needed to access the user/player partecipating in the game.
# teams = Teams(logged_in_players)

# # Teams is passed as an argument to access the two countries for the game.
# game_test = GameSettings(teams)

# # The game function contains a parameter that resembles the main_sign_in_process. This is because it is needed for the teams class instsnce inside the function that requires the same parameter.
# game_test.games(logged_in_players)