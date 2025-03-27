
import string
import random
import json


class SignUpProcess:
  
  """initial sign up credentials"""

  def __init__ (self):
    
    # self.user_accounts_history_list = []
    self.name = None
    self.surname = None
    self.email_address = None
    self.nickname = None
    self.code = None
    
    
  def json_append_data(self):
      
      """Append gamer credentials' dictionary in the json file"""
      
      with open ("json_user_data","r") as file:
         self.data_history_to_append = json.load(file)
      
      self.data_history_to_append.append(self.user_dict)
         
      with open ("json_user_data","w") as file:
        return json.dump(self.data_history_to_append,file, indent=4)
    
    
  def json_read_data(self,filename):
    
      """Reads the gamer credentials' dictionary"""
    
      with open (filename,"r") as file:
         self.read_data_history = json.load(file)
         return self.read_data_history
         

    
  def sign_up(self) -> str:
    
      """User initial information."""
      
      print("Welcome to the contraband game please sign up")  
      
      self.name = input("Name:  ")
      self.surname = input("Surame:  ")
      
      while True:
        
        self.email_address = input("email: ")
        
          
        if "@" in self.email_address and "." in self.email_address: # Checking requirements needed for an email
          
          print("Succesful sign up")
          break
        
        else:
          print("Not matching email standards. Please add a @ and a . into your email.")  
          
    
           
    
  def dict_credentials(self) -> str: 
        
      """Data where each user generated credentials are stored"""
      
      
      self.user_dict = {"nickname": self.nickname,
                  "code": self.code,
                  "email": self.email_address,
                  }
    
      print("Data inserted on database")
     

    
  def game_generated_credentials(self) -> str:
    
        """Generating nickname and code for each user."""  
        
        game_hist_data_instance = self.json_read_data("json_user_data")
        
    
        if self.email_address != None and self.email_address in game_hist_data_instance:
          
    
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
                print("ACCOUNT CREATED")
                
                break
              
              if nickname == "skip" and code == 'skip':
                break
          
              else:
                  print("Incorrect gamer credentials")
                
          
         
    
  def main_signup_process(self):
        
        """Sign up function that summarises all the sign up process, from sign up to log in"""
    
        self.sign_up() # sign up first gamer
        
        self.game_generated_credentials()  
        
        self.sign_in()
        
        
        additional_player = input("to join a second gamer press S otherwise press N: ")  # sign up second player
      
        if additional_player == "S":
          
          self.sign_up()
          self.game_generated_credentials() 
          self.sign_in()
          
          self.dict_credentials()
          print(self.json_append_data())
          
        elif additional_player == "N":
          
            self.dict_credentials()
            print(self.json_append_data())
            
            print("Only 1 player logged in")
        
        else:
          
          while True:
            
            try_again_invalid_char = input("invalid character, try again: ")
            
            if try_again_invalid_char == "S":
              print("Character now accepted")
            
            
              self.sign_up()
              self.game_generated_credentials() 
              self.sign_in()
              
              self.dict_credentials()
              print(self.json_append_data())
              break 
            
            elif try_again_invalid_char == "N":
              
              self.dict_credentials()
              print(self.json_append_data())
              
              print("Only 1 player logged in")
              break
        
  



  def main_signin_process(self):
        
        """Log in process, remember your gaming credentials"""
        
        try:
          self.sign_in()
        except:
          print("Login process invalid")
    
