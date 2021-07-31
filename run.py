import random
from users import User
 

def main():
 print("Welcome to PassLOCKER!")
 print('\n')

while True:
   print("Please user one of the short-cods below to navigate the platform.")
   print('\n')
   print("1.cr to create a new account. 2.lg to log into your account. 3.vi to view your saved passwords. 3.de to delete your saved passwords. 4.ex to exit the platform")
   codes = input("Code..").lower()

   if codes == "cr":
      print("Create new username")
      new_username = input("Username..")

      print("Create new password")
      new_password = input("Password..")

      print("Confirm password")
      new_confirm = input("Password.")

      while new_confirm != new_password:
         print("Passwords did not match.Please input correct password")
         new_password = input("Password..")

         print("Confirm password")
         new_confirm = input("Password.")
         print("\n")

      else:
         print("Successful")
         print("\n")
         print("Please log in to your account to edit passwords.")
         print("\n")
         log_username = input("Username..")
         log_password = input("Password...")

      while log_username != new_username or log_password != new_password:
         print("Invalid username or password.Please try again.")
         print("\n")
         log_username = input("Username..")
         log_password = input("Password...")
         

      else:
         print(f"Welcome {log_username} to your password account")
         print("\n")
         
   elif codes == "lg":
      print("Welcome back")
      print("\n")
      print("Input your login credentials below.") 
      print("\n")
      ent_username = input("Username..")
      ent_password = input("Password..")
      print("\n")

   while ent_username != "Testing" or ent_password != "12345":
      print("Invalid username or password.Try this Username = Testing and Password = 12345")
      print("\n")
      ent_username = input("Username..")
      ent_password = input("Password..")
      print("\n")

   else:
      print("Log in successful")
      print("\n")
     
