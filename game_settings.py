from teams import Teams


class GameSettings:
    
    
    def __init__(self,team:Teams):
        pass
    
    def games(self):
        
        """General game setting"""
        
        games = 10 #trial
        
        while games > 0:
            
            smuggler = int(input("place your amount. the max is 100.000.000 £: "))
            if smuggler > 100000000:
                print("Invalid amount")
            else:
                print("Smuggler turn is over")
                
            while True:
                
                inspector = input("insert PASS if you believe the smuggler is carrying no money. Insert DOUBT if you believe money are carried by the smuggler: ")
                
                if inspector == "PASS":
                    print(f"Inspector declared PASS, the smuggler carried {smuggler} £")
                    
                    if smuggler == 0:
                        print("No money has been smuggled to the outside bank account")
                        break   
                    else:
                        print(f"The smuggler has been able to carry {smuggler} £ into his/her's outside bank account")
                        break
                
                elif inspector == "DOUBT":
                    statement_amount = int(input("AMOUNT: "))
                    
                    if statement_amount > 100000000:
                        print("Invalid amount")
                    else:
                        pass
                        
                    security_amount = statement_amount / 2
                    
                    if statement_amount >= smuggler:
                        print(f"Smuggling attempt flopped. The inspector obtained {smuggler} into his/her's bank account")
                        break
                    elif smuggler == 0:
                        print(f"Smuggler obtained {security_amount} £ of security amount")
                        break
                    elif statement_amount < smuggler:
                        print(f"Smugglers succesfully smuggled {smuggler} £ on his/her's outside bank account plus {security_amount} from the inspector")
                        break
                else:
                    print("invalid try again")
                