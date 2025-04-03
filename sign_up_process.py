
import string
import random
import json


class SignUpProcess:
  
  """initial sign up credentials"""

  def __init__ (self):
    
    self.json_value_validation = True
    self.name = None
    self.surname = None
    self.email_address = None
    self.nickname = None
    self.code = None
    
    
    
  def json_append_data(self,filename,*args):
      
      """Append gamer credentials' dictionary in the json file"""
      
      with open (filename,"r") as file:
        # Json list object
         self.data_to_append = json.load(file) 
      
      # This is uselful to append any other object beside self.user dict in a json file.   
      if self.name is None and self.surname is None: 
        for arg in args:
            self.data_to_append.append(arg) 
      else:
       # The dictionary comes from the dict credential function 
       self.data_to_append.append(self.user_dict) 
         
      with open (filename,"w") as file:
        return json.dump(self.data_to_append,file, indent=4)
    
    
    
  def json_read_data(self,filename) ->list:
    
      """Reads list from json files"""
    
      with open (filename,"r") as file:
         # returns a list object
         return json.load(file) 
       
      
      
       
  def json_account_check_process(self):
    
    """Checks if value is in the json dictionary"""
    
    read_data_for_signin = self.json_read_data("json_user_data")  
    read_data_for_players = self.json_read_data("players.json")
       
    # list containing all the values from the json_user_data's dictionary
    self.json_user_data_list = [values for dictionaries in read_data_for_signin for values in dictionaries.values()] 
    # List containing all the values from players.json's dictionary
    self.players_json_list = [value_players for dictionaries_players in read_data_for_players for value_players in dictionaries_players.values()] 
    
    # Check if nickname has been already in the player.json file in order to avoid multiple sign in with the same gamer credentials.
    if self.nickname_signin in self.players_json_list:
      print("player already generated")
      
    else:
      
      if self.nickname_signin in self.json_user_data_list and self.code_signin in self.json_user_data_list:
    
          index1 = self.json_user_data_list.index(self.nickname_signin) 
          index2 = self.json_user_data_list.index(self.code_signin)
          
          # This will avoid accessing the game with credentials deriving from two different account but still present in the json list
          if index1 + 1 == index2: 
          # Stopping the while self.json_value_validation in sign in.
            self.json_value_validation = False
            print("Credentials present on database")
            
          else:
            print("Incorrect credentials")
      
       
          
    

    
  def sign_up(self) -> str:
    
      """User initial information."""
      
      print("Welcome to the contraband game please sign up")  
      
      self.name = input("Name:  ")
      self.surname = input("Surame:  ")
      
      while True:
        
        self.email_address = input("email: ")
        
         # Checking requirements needed for an email 
        if "@" in self.email_address and "." in self.email_address:
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
          
            # preventing creation of multiple accounts
            print("Account already exists")
    
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
        
        while self.json_value_validation:
          
          print("Insert 'skip' on both nickname and code if convenient to skip.") 
          self.nickname_signin = input("Nickname: ")
          self.code_signin = input("code: ")
          
          
          try:
            
            # Checking if gamer credentials are in the json_user_data file, avoiding access with nickname and code from two different game credentials in the json file etc...
            self.json_account_check_process()
            
            # this is an additional layer (probably redundant)
            if self.nickname_signin in self.nickname and self.code_signin in self.code:
              
            
              print(f"{self.nickname_signin} and {self.code_signin} accepted")
              print("ACCOUNT CREATED")   
              
              break
            
          except:
            pass
            
          if self.nickname_signin == "skip" and self.code_signin == 'skip':
            break
      
          else:
            pass
                
          
         
    
  def main_signup_process(self):
        
        """Sign up function that summarises all the sign up process"""
        
        
        # sign up first gamer.
        self.sign_up() 
        
        self.game_generated_credentials()  
        self.dict_credentials()
        # Adding dict_credentials in the json_user_data file.
        self.json_append_data("json_user_data")
        
        # sign up second player.
        additional_player = input("to join a second gamer press S otherwise press N: ")  
      
        if additional_player == "S":
          
          self.sign_up()
          self.game_generated_credentials() 
          
          self.dict_credentials()
          self.json_append_data("json_user_data")
          
        elif additional_player == "N":
            
            print("Only 1 player logged in")
        
        else:
          
          while True:
            
            try_again_invalid_char = input("invalid character, try again: ")
            
            if try_again_invalid_char == "S":
              print("Character now accepted")
            
            
              self.sign_up()
              self.game_generated_credentials() 
              
              self.dict_credentials()
              self.json_append_data("json_user_data")
              break 
            
            elif try_again_invalid_char == "N":
            
              print("Only 1 account generated")
     
              break
        

 
  def main_sign_in_process(self):
    
    """Sign up function that summarises all the sign up process"""
    
    # Used to multiple log in requests. Maximum 4 players.
    count_players  = 3 
    
    self.sign_in()
    
    # Unlike the sign up this will grab the user nickname data for then store it in a json file
    self.json_append_data("players.json",{"Nickname": self.nickname_signin})
    
    while count_players > 0:
      
      try:
        
        second_sign_in = int(input("Insert 2 to sign up another player else Insert 0: "))
        
        if second_sign_in == 0:
          break
          
        elif second_sign_in == 2:
          
           # Needed to be added since after the first call of the functions the boolian turns in False.
          self.json_value_validation = True
          self.sign_in()
          self.json_append_data("players.json",{"Nickname": self.nickname_signin})
          count_players -= 1
      
      except:
          print("I Know it sounds frustrating, please restart the log in process.")
        
      
      




    
      
      




    
