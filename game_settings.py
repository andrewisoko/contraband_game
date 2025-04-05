from teams import Teams
from getpass import getpass


class GameSettings:
    
    
    def __init__(self,teams:Teams):
        
        self.teams = teams
        self.smuggler = None
        self.inspector = None
        self.security_amount = None
        self.game = None
       
    
    
    
    
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
                
        if self.smuggler == 0 and self.statement_amount > 0:
            print(f"Smuggler obtained {self.security_amount:,} £ of security amount.")
            
        elif self.statement_amount >= self.smuggler:
            print(f"Smuggling attempt flopped!!! The inspector obtained {self.smuggler:,} £ into his/her outside country's bank account.")
                    
    
        elif self.statement_amount < self.smuggler:
            print(f"Smugglers succesfully smuggled {self.smuggler:,} £ on his/her outside country's bank account plus {self.security_amount:,} from the inspector")
        else:
            pass
   
      
    
    def pass_declaration(self):
        
        """All the scenarios occurring from a pass declaration"""

        print(f"Inspector declared PASS, the smuggler carried {self.smuggler:,} £")
        
        if self.smuggler == 0:
            print(f"No money has been smuggled to the outside bank account.")
            
        else:
            print(f"The smuggler has been able to carry {self.smuggler:,} £")
   
           
            
    def The_inspector(self):
        
        """Inspector's action"""
        
        while True:
            
            self.inspector = input("insert PASS if you believe the smuggler is carrying no money. Insert DOUBT if you believe money are carried by the smuggler: ")
            
            if self.inspector == "PASS":
                self.pass_declaration()
                break
                
            elif self.inspector == "DOUBT":
                self.doubt_declaration()
                break
            
            else:
                print("Invalid input. Please try again")
   
   
   
    def The_smuggler(self):
        
        """The smuggler's action"""
        
        while True: 
            try:

                self.smuggler = int(getpass("Place your amount. The max is 100,000,000 £: "))
                if self.smuggler <= 100_000_000 and self.smuggler.is_integer():
                    print("Smuggler turn is over")
                    break  
                else:
                    print("Invalid amount. Please try again.")
            except:
                print("Invalid input. Please enter a numeric value.")
 
       

    
           
  
           
                

# game_test = GameSettings()
# game_test.games()