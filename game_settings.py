from teams import Teams
from getpass import getpass
import random

class GameSettings:
    
    
    def __init__(self,teams:Teams):
        
        self.teams = teams
        self.smuggling_amount = None
        self.inspector = None
        self.security_amount = None
        self.game = None
       
       
       
    def assign_roles(self):
        """Assign roles (Smuggler and Inspector) to players"""
        
        southern_player = self.teams.southern_team_players()
        northern_player = self.teams.northern_team_players()

        # Randomly assign roles
        roles = ["Smuggler", "Inspector"]
        random.shuffle(roles)

        if roles[0] == "Smuggler":
            
            self.smuggler = southern_player
            self.inspector = northern_player
        else:
            self.smuggler = northern_player
            self.inspector = southern_player
        
    
    
    def doubt_declaration(self):
        
        """All the scenarios occurring from a doubt declaration"""
        
        while True:
             
            try:
                self.statement_amount = int(input("AMOUNT: "))
                self.security_amount = self.statement_amount / 2
                
                if self.statement_amount < 100_000_000 and self.statement_amount.is_integer():
                    break
                else:
                    print("Invalid amount")
            except:
                print("Invalid input. Please enter a numeric value.")
                
        if self.smuggling_amount == 0 and self.statement_amount > 0:
            print(f"The smuggler {self.smuggler} obtained {self.security_amount:,} £ of security amount.")
            
        elif self.statement_amount >= self.smuggling_amount:
            print(f"Smuggling attempt flopped!!! The inspector {self.inspector} obtained {self.smuggling_amount:,} £ into his/her outside country's bank account.")
                    
    
        elif self.statement_amount < self.smuggling_amount:
            print(f"Smugglers succesfully smuggled {self.smuggling_amount:,} £ on his/her outside country's bank account plus {self.security_amount:,} from the inspector!!!")
        else:
            pass
   
      
    
    def pass_declaration(self):
        
        """All the scenarios occurring from a pass declaration"""

        print(f"Inspector declared PASS, the smuggler carried {self.smuggling_amount:,} £")
        
        if self.smuggling_amount == 0:
            print(f"No money has been smuggled to the outside bank account.")
            
        else:
            print(f"The smuggler has been able to carry {self.smuggling_amount:,} £")
   
           
            
    def the_inspector(self):
        
        """Inspector's action"""
        
        while True:
            
             
        
            self.inspector_action = input(f"{self.inspector} insert PASS if you believe the smuggler is carrying no money. Insert DOUBT if you believe money are carried by the smuggler: ")
            
            if self.inspector_action == "PASS":
                self.pass_declaration()
                break
                
            elif self.inspector_action == "DOUBT":
                self.doubt_declaration()
                break
            
            else:
                print("Invalid input. Please try again")
   
   
   
    def the_smuggler(self):
        
        """The smuggler's action"""
        
        while True: 
            try:

                self.smuggling_amount = int(getpass(f"{self.smuggler} place your amount. The max is 100,000,000 £: "))
                if self.smuggling_amount <= 100_000_000 and self.smuggling_amount.is_integer():
                    print(f" {self.smuggler} smuggler turn is over")
                    break  
                else:
                    print("Invalid amount. Please try again.")
            except:
                print("Invalid input. Please enter a numeric value.")
 
       

    
           
  
           
                

# game_test = GameSettings()
# game_test.games()