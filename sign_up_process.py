
import string
import random
import json


class SignUpProcess:
  
  """initial sign up credentials"""

  def __init__ (self):
    
    self.json_value_validation = True
    self.values_from_json_list = []
    self.name = None
    self.surname = None
    self.email_address = None
    self.nickname = None
    self.code = None
    
    
  def json_append_data(self):
      
      """Append gamer credentials' dictionary in the json file"""
      
      with open ("json_user_data","r") as file:
         self.data_history_to_append = json.load(file)
      
      self.data_history_to_append.append(self.user_dict) # the dictionary comes from the dict credential function 
         
      with open ("json_user_data","w") as file:
        return json.dump(self.data_history_to_append,file, indent=4)
    
    
  def json_read_data(self,filename) ->list:
    
      """Reads the gamer credentials' dictionary"""
    
      with open (filename,"r") as file:
         return json.load(file) # returns a list object
       
      
      
       
  def json_account_check_process(self):
    
    """Checks if value is in the json dictionary"""
    
    read_data_for_signin = self.json_read_data("json_user_data")   
      
    for dictionaries in read_data_for_signin:
      for values in dictionaries.values(): 
            
        self.values_from_json_list.append(values)
      
    if self.nickname_signin in self.values_from_json_list and self.code_signin in self.values_from_json_list:
   
        index1 = self.values_from_json_list.index(self.nickname_signin) 
        index2 = self.values_from_json_list.index(self.code_signin)
        
        if index1 + 1 == index2: # This will avoid accessing the game with credentials deriving from two different account but still present in the json list
          
          self.json_value_validation = False # Stopping the while self.json_value_validation in sign in.
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
        
        while self.json_value_validation:
          
          print("Insert 'skip' on both nickname and code if convenient to skip.") 
          self.nickname_signin = input("Nickname: ")
          self.code_signin = input("code: ")
          
          
          try:
            
            self.json_account_check_process()
            
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
    
        self.sign_up() # sign up first gamer
        
        self.game_generated_credentials()  
        self.dict_credentials()
        print(self.json_append_data())
        
        
        additional_player = input("to join a second gamer press S otherwise press N: ")  # sign up second player
      
        if additional_player == "S":
          
          self.sign_up()
          self.game_generated_credentials() 
          
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
              
              self.dict_credentials()
              print(self.json_append_data())
              break 
            
            elif try_again_invalid_char == "N":
            
              print("Only 1 account generated")
              break
        

  def main_sign_in_process(self):
    
    """Sign up function that summarises all the sign up process"""
    
  
    self.sign_in()
    
    try:
      
      second_sign_in = int(input("Insert 2 to sign up another player else Insert 0: "))
      
      if second_sign_in == 0:
        
        print("only one player in the game")
        
      elif second_sign_in == 2:
        
        self.json_value_validation = True # needed to be added since after the first call of the functions the boolian turns in False.
        self.sign_in()
   
    
    except:
        print("I Know it sounds frustrating, please restart the log in process.")
      
      
      




    
