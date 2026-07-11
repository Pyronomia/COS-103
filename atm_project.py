# Users
atm_users = [
   {    "Name": "Sinmiloluwa",
        "Pin": "9873",
        "Balance": 23290
    },
    {
        "Name": "David",
        "Pin": "3256",
        "Balance": 3550
    },
     {
        "Name": "Elijah",
        "Pin": "7654",
        "Balance": 100000
    },
     {
        "Name": "Esther",
        "Pin": "2987",
        "Balance": 54780
    },
    {
        "Name": "Sarah",
        "Pin": "4018",
        "Balance": 78240
    }
]

# To make the things in the terminal look neater
long_div = "-------------------------------------------"
login_pass = ""
user_pin_tries_pass = ""

def login_page():
    global login_pass
    login_pass = ""
    print(f"{long_div}\nWelcome To Sinmiloluwa's Python ATM Machine")
    print(f"{long_div}\nActive Users: {len(atm_users)}")
    print(f"{long_div}\nPlease Select What You Would Like to do Below ")
    print(f"   Select 1 To Create a New User")
    print(f"   Select 2 To Login Into an Existing Account\n{long_div}")
    while True:
        login_input = input("Please Input a Number: ")
        if (login_input == "1"):
            new_username = input("Please Enter Your Desired Username: ")
            running_loop = True
            while running_loop:
                pin = "valid"
                new_pin = input("Please Create Your Unique Pin: ")
                if (new_pin.isdigit() and len(new_pin) == 4):
                    for user_1 in atm_users:
                        if (new_pin == user_1["Pin"]):
                            print(f"{long_div}\nThis Pin Already Exists. Please Try Another One\n{long_div}")
                            pin = "invalid"
                else:
                    print(f"{long_div}\nPlease Input a Valid 4-Digit Pin\n{long_div}")
                    pin = "invalid"

                if (pin == "valid"):
                    running_loop = False
                    break 
    
            while True:
                new_balance = input("Please Enter the Amount You Wish to Deposit: ")
                if (new_balance.isdigit()):
                    break
                else:
                    print(f"{long_div}\nPlease Input a Valid Number\n{long_div}")

            new_balance = int(new_balance)
            new_user ={"Name": new_username, "Pin": new_pin, "Balance": new_balance}
            print(f"{long_div}\nNew User Successfully Created!")
            atm_users.append(new_user)
            break
        elif (login_input == "2"):
            login_pass = True
            break
            
        else: 
            print(f"{long_div}\nPlease Input a Valid Number\n{long_div}")



def action_input():
    while True:
        print(f"{long_div}\nSelect 1 to Check Current Balance\nSelect 2 to Withdraw Cash\nSelect 3 to Deposit Cash\nSelect 4 to Exit\n{long_div}")
        action_input_num = input("Please Input a Number: ")
        if (action_input_num == "1"):
            check_current_balance(user_check_in_object["Balance"])

        elif(action_input_num == "2"):
            withdraw_cash(user_check_in_object["Balance"])
        elif(action_input_num == "3"):
            deposit_cash(user_check_in_object["Balance"])
        elif(action_input_num == "4"):
            print(f"{long_div}\nGoodbye. Thank you for your time {user_check_in_object["Name"]}\n{long_div}")
            break
        else:
            print("Please Input a Valid Number")
        

# Authentication
user_check_in_object = ""
def user_authentication():
    global user_pin_tries_pass
    user_pin_tries_pass = ""
    pin_tries = 5
    while True:
        if (pin_tries == 0):
            print(f"{long_div}\nYou Have Exhausted All Your Tries...\n{long_div}")
            break
        user_check_in_pin = input("Enter Your 4-Digit Pin: ")
        if user_check_in_pin.isdigit() and len(user_check_in_pin) == 4:
            # Checking if the pin is correct
            for user in atm_users:
                if (user_check_in_pin == user["Pin"]):
                    global user_check_in_object
                    print(f"{long_div}\nWelcome {user["Name"]}")
                    user_check_in_object = user
                    user_pin_tries_pass = True
                    return
            pin_tries -= 1
            print(f"{long_div}\nUser Not Found!\n{long_div}")
            print(f"{long_div}\nYou Have {pin_tries} tries left\n{long_div}")
        elif user_check_in_pin.isdigit() and (len(user_check_in_pin) != 4):
            print(f"{long_div}\nPlease Input a Valid Pin\n{long_div}")
            print(f"{long_div}\nYou Have {pin_tries} tries left\n{long_div}")
        else: 
            pin_tries -= 1
            print(f"{long_div}\nPlease Input Valid Digits\n{long_div}")
            print(f"{long_div}\nYou Have {pin_tries} tries left\n{long_div}")

   
      

# Check Current Balance Function
def check_current_balance(user_balance):
    print(f"{long_div}\nYour Current Account Balance is {user_balance}")

# Withdraw Cash Function
def withdraw_cash(user_balance):
    while True:
        amount_to_be_withdrawn = input("Please Enter the Amount You Wish to Withdraw: ")
        if(amount_to_be_withdrawn.isdigit()) and int(amount_to_be_withdrawn) < user_balance:
            print(f"{long_div}\n{amount_to_be_withdrawn} Naira Has Been Successfully Withdrawn")
            break
        elif((amount_to_be_withdrawn.isdigit()) and int(amount_to_be_withdrawn) > user_balance):
            print(f"{long_div}\nInsufficient Balance\n{long_div}")
            return
        else:
            print(f"{long_div}\nPlease Input a Valid Number\n{long_div}")
    amount_to_be_withdrawn = int(amount_to_be_withdrawn)
    new_balance = user_balance - amount_to_be_withdrawn
    user_check_in_object["Balance"] = new_balance
    
# Deposit Cash Function
def deposit_cash(user_balance):
    while True:
        amount_to_be_deposited = input("Please Enter the Amount You Wish to Deposit: ")
        if(amount_to_be_deposited.isdigit()):
            print(f"{long_div}\n{amount_to_be_deposited} Naira Has Been Successfully Deposited")
            break
        else:
            print(f"{long_div}\nPlease Input a Valid Number\n{long_div}")
    amount_to_be_deposited = int(amount_to_be_deposited)
    new_balance = user_balance + amount_to_be_deposited
    user_check_in_object["Balance"] = new_balance

def runAtmApp():
    while True:
        login_page()
        if (login_pass):
            user_authentication()
            if (user_pin_tries_pass):
                action_input()

runAtmApp()