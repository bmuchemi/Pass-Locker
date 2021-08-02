import random
from users import Credentials
from users import User
from tkinter import *



def create_account(account_name,created_username,created_password):
   '''
   function to create a new account
   '''
   new_account = Credentials(account_name,created_username,created_password)
   return new_account

def save_accounts(credentials):
   '''
   function to save the new account
   '''
   credentials.save_account()

def display_account():
   '''
   function to display all accounts saved
   '''
   return Credentials.display_passwords()

def delete_account(credentials):

   credentials.delete_passwords()

def main():
 print("Welcome to PassLOCKER!")
 print('\n')

while True:
   print("Please user one of the short-cods below to navigate the platform.")
   print('\n')
   print("1.cr to create a new account. 2.lg to log into your account. 3.vi to view your saved passwords. 4.cp to create a new password to save 5.de to delete your saved passwords. 6.ex to exit the platform")
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
         
   
     
   elif codes == "cp":
      print("Lets create a new account")
      print("\n")
      account_name = input("Account name..")
      created_username = input("Username..")
      created_password = input("Password..")
      save_accounts(create_account(account_name,created_username,created_password))
      print ('\n')
      print(f"New account: {account_name} has been successfully created with the following credentials: \n Username: {created_username} --- Password:{created_password}")
      print ('\n')
   
   elif codes == "vi":
      print("-"*10)
      if display_account():
         print("\nHere is a list of all your accounts:\n")
         for item in display_account():
            print(item.init_account +"\t --> "+ item.account_username +"\t --> "+ item.account_passsword)
      else:
         print("\n You do not have any accounts saved \n")

   elif codes == "de":
      print("-"*10)
      print("Input account you want to delete.")
      print("-"*10)
      delete = input("Account name..")
      if delete:
         delete_account(delete)
         for left in display_account():
            print(left.account_name + -"--> "+ left.username +"---> "+ left.password)
      else:
         print("\n")
         print("There is no such saved account to delete")

if __name__ == "__main__":
    main()