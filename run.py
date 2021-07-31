import random
from users import User
 

def main():
 print("Welcome to PassLOCKER!")
 print('\n')

while True:
   print("Please user one of the short-cods below to navigate the platform.")
   print('\n')
   print("1.cr to create a new account. 2.lg to log into your account. 3.vi to view your saved passwords. 3.de to delete your saved passwords. 4.ex to exit the platform")
   codes = input().lower()

   if codes == cr:
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

      else:
         print("Successful")
         print("Please log in to your account to edit passwords.")

   
   