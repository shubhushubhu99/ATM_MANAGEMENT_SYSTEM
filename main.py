import os

# CLEAR SCREEN FOR ALL OS
def clear():
    if os.name == "nt":
        os.system("cls") # cls command is used to clear terminal in windows
    else:
        os.system("clear") # clear for mac and linux

# STORING CUSTOMER DETAILS IN DICTIONARY
database = {2546284:{"name":"shubham", "balance":10000, "pin":1122},
            2546268:{"name":"Md Anas", "balance":10000, "pin":2233}}
            # You can add more data in same structure..

def authenticate():
    account_no = int(input("Enter your account number : "))
    if account_no in database:
        user_pin = int(input("Enter your pin : "))
        if user_pin == database[account_no]["pin"]:
            return account_no
        else:
            print("Your pin is wrong")
            exit()
    else:
        print("Account doesn't exist..")
        exit()

# function for checking balance 
def show_balance():
    account_no = authenticate()
    print(f"your available balance is {database[account_no]["balance"]}")

# FUNCTION FOR WITHDRAWING AMOUNT
def withdraw_balance():
    account_no = authenticate()
    withdraw_amount = int(input("Enter withdraw amount : "))
    if withdraw_amount <= database[account_no]["balance"]:
        database[account_no]["balance"] = database[account_no]["balance"] - withdraw_amount
        print(f"withdrawl sucessfull.. your available balance is {database[account_no]["balance"]}")
    else:
        print("You do not have sufficiant balance in your account")
        exit()

# FUNCTION FOR DEPOSITING BALANCE
def deposite_balance():
    account_no = authenticate()
    deposite_amount = int(input("Enter your deposite amount : "))
    if deposite_amount > 1000000:
        print("deposite amount can not be more than 10 lakh")
        exit()
    else:
        database[account_no]["balance"] = database[account_no]["balance"] + deposite_amount
        print(f"deposite sucessfully.. your current balance is {database[account_no]["balance"]}")

# FUNCTION FOR CHANGING PIN
def change_pin():
    account_no = authenticate()
    new_pin = input("Enter your new pin")
    if len(new_pin) == 4:
        database[account_no]["pin"] = int(new_pin)
        print("Pin changed sucessfully")
    else:
        print("pin can't be of more than 4 digit")
        exit()

# MAIN MENU FUNCTION

def main_menu():
    print("""
HELLO !! HOW MAY I ASSIST YOU ..

[1] SHOW BALANCE
[2] WITHDRAW BALANCE
[3] DEPOSITE BALANCE
[4] CHANGE PIN
[5] EXIT          
          """)
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        show_balance()
        main_menu()
    elif choice == 2:
        withdraw_balance()
        main_menu()
    elif choice == 3:
        deposite_balance()
        main_menu()
    elif choice == 4:
        change_pin()
        main_menu()
    elif choice == 5:
        exit()
    else:
        print("Invalid option !!!")
        exit()


clear()
main_menu()