
import string
import random


class SignUpProcess:
  
  """initial sign up credentials"""

  def __init__ (self):
    
    self.user_accounts_history_list = []
    self.name = None
    self.surname = None
    self.email_address = None
    self.nickname = None
    self.code = None
    
    
  
    
  def sign_up(self) -> str:
    
      """User initial information."""
      
      print("Welcome to the contraband game please sign up")  
      
      self.name = input("Name:  ")
      self.surname = input("Surame:  ")
      
      while True:
        
        self.email_address = input("email: ")
          
        if "@" in self.email_address and "." in self.email_address: # Checking requirements needed for an email
          
          print("account created")
          break
        
        else:
          print("Not matching email standards. Please add a @ and a . into your email.")  
          
    
           
    
  def dict_credentials(self) -> dict: 
        
      """Data where each user generated credentials are stored"""
      
      
      user_dict = {"nickname": self.nickname,
                  "code": self.code,
                  "email": self.email_address,
                  }
      self.user_accounts_history_list.append(user_dict)
      print("Data inserted on database")
   
    
    
  def game_generated_credentials(self) -> str:
    
        """Generating nickname and code for each user."""  
    
        if self.email_address != None and self.email_address in self.user_accounts_history_list:
    
            print("Account already exists") # preventing creation of multiple accounts
    
        else:
    
            self.nickname = self.name[0:3] + self.surname  

    
            letters_uppercase = string.ascii_uppercase
            my_tuppy = (string.ascii_lowercase,string.punctuation,string.digits)

            code_chars = letters_uppercase.join(my_tuppy)

            list_char = [char for char in code_chars]
            random.shuffle(list_char)
            empty = ""

            code_string = empty.join(tuple(list_char))
            
            self.code = code_string[0:18]
            
        
            print(f"Please save and use the generated user credentials to login. NICKNAME:{self.nickname} USER CODE:{self.code}")
     
     
        
        
  def sign_in(self) -> str:
      
      
        """Login for user after obtained the game credentials"""
        

        if self.name == None and self.surname == None and self.email_address == None:
            
            print("User credentials missing, your game credentials have not been generated")
        
        else:
            
            while True:
              
              print("Insert 'skip' on both nickname and code if convenient to skip.") 
              nickname = input("Nickname: ")
              code = input("code: ")
              
              if nickname == self.nickname and code == self.code:
              
                print(f"{nickname} and {code} accepted")
                break
              
              if nickname == "skip" and code == 'skip':
                break
          
              else:
                  print("Incorrect gamer credentials")
                
          
         
    
  def main_signup_process(self):
        
        """Sign up function that summarises all the sign up process, from sign up to log in"""
    
        self.sign_up() # sign up first gamer
        
        self.game_generated_credentials()  
        
        self.dict_credentials()
        
        self.sign_in()
        
        
        additional_player = input("to join a second gamer press S otherwise press N: ")  # sign up second player
      
        if additional_player == "S":
          
          self.sign_up()
          self.game_generated_credentials() 
          self.dict_credentials()
          self.sign_in()
          
          print(self.user_accounts_history_list)
          
        elif additional_player == "N":
          print("Only 1 player logged in")
        
        else:
         print("invalid character")
        
  



  def main_signin_process(self):
        
        """Log in process, remember your gaming credentials"""
        
        try:
          self.sign_in()
        except:
          print("Login process invalid")
    
