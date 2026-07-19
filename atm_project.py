# Users
atm_users = [
   {    "Name": "Sinmiloluwa",
        "Account No": "9042089471",
        "Pin": "9873",
        "Balance": 23290
    },
    {
        "Name": "David",
        "Account No": "9112189081",
        "Pin": "3256",
        "Balance": 3550
    },
     {
        "Name": "Elijah",
        "Account No": "8088901234",
        "Pin": "7654",
        "Balance": 100000
    },
     {
        "Name": "Esther",
        "Account No": "7135654321",
        "Pin": "2987",
        "Balance": 54780
    },
    {
        "Name": "Sarah",
        "Account No": "7029876123",
        "Pin": "4018",
        "Balance": 78240
    }
]

transaction_history = []
accessed = "no"

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
            print("Press q to quit the action below")
            new_username = input("Please Enter Your Desired Username: ")
            if(new_username == "q"):
                return

            running_loop_2 = True
            while running_loop_2:
                number = "valid"
                print("Press q to quit the action below")
                new_account_no = input("Please Input Your Phone Number: ")
                if(new_account_no == "q"):
                    return
                if (new_account_no.isdigit() and len(new_account_no) == 11):
                    for user_1 in atm_users:
                        if (new_account_no[1:] == user_1["Account No"]):
                            print(f"{long_div}\nThis Number Already Exists. Please Try Another One\n{long_div}")
                            number = "invalid"
                else:
                    print(f"{long_div}\nPlease Input a Valid 11-Digit Number\n{long_div}")
                    number = "invalid"

                if (number == "valid"):
                    print(f"{long_div}\nYour Account Number is {new_account_no[1:]}\n{long_div}")
                    running_loop_2 = False
                    break

            running_loop = True
            while running_loop:
                pin = "valid"
                print("Press q to quit the action below")
                new_pin = input(f"Please Create Your Unique Pin: \n{long_div}")
                if (new_pin == "q"):
                    return
                if (new_pin.isdigit() and len(new_pin) == 4):
                    pin = "valid"
                else:
                    print(f"{long_div}\nPlease Input a Valid 4-Digit Pin\n{long_div}")
                    pin = "invalid"

                if (pin == "valid"):
                    running_loop = False
                    break 
    
            while True:
                print("Press q to quit the action below")
                new_balance = input("Please Enter the Amount You Wish to Deposit: ")
                if(new_balance == "q"):
                    return
                if (new_balance.isdigit()):
                    break
                else:
                    print(f"{long_div}\nPlease Input a Valid Number\n{long_div}")

            new_balance = int(new_balance)
            new_user ={"Name": new_username, "Account No": new_account_no[1:], "Pin": new_pin, "Balance": new_balance}
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
        print("----------MAIN MENU----------")
        print(f"Select 1 to Check Current Balance")
        print(f"Select 2 to Withdraw Cash")
        print(f"Select 3 to Deposit Cash")
        print(f"Select 4 to Change Pin")
        print(f"Select 5 to Check Transaction History")
        print(f"Select 6 to Pay Bills")
        print(f"Select 7 to Exit\n{long_div}")
        action_input_num = input("Please Input a Number: ")
        if (action_input_num == "1"):
            check_current_balance(user_check_in_object["Balance"])
        elif(action_input_num == "2"):
            withdraw_cash(user_check_in_object["Balance"])
        elif(action_input_num == "3"):
            deposit_cash(user_check_in_object["Balance"])
        elif(action_input_num == "4"):
            change_pin()
        elif(action_input_num == "5"):
            trans_history()
        elif(action_input_num == "6"):
            pay_bills(user_check_in_object["Balance"])
        elif(action_input_num == "7"):
            print(f"{long_div}\nGoodbye. Thank you for your time {user_check_in_object["Name"]}\n{long_div}")
            break
        else:
            print("Please Input a Valid Number")
        

# Authentication
user_check_in_object = ""
def user_authentication():
    global user_pin_tries_pass
    global break_loop
    global user_check_in_object
    user_pin_tries_pass = ""
    pin_tries = 5
    break_loop = ""

    while True:
        print(f"{long_div}\nPress q to quit the action below")
        user_account_no = input(f"Enter Your Account Number: ")
        if(user_account_no == "q"):
            return 
        elif (user_account_no.isdigit() and len(user_account_no) == 10):
            for user in atm_users:
                if (user_account_no == user["Account No"]):
                    user_check_in_object = user
                    break_loop = "break"
                    break

        if(break_loop == "break"):
            break
        else:
            print(f"{long_div}\nPlease Input a Valid Account Number")

    while True:
        if (pin_tries == 0):
            print(f"{long_div}\nYou Have Exhausted All Your Tries...\n{long_div}")
            break
        

        print(f"{long_div}\nPress q to quit the action below")
        user_check_in_pin = input(f"Enter Your 4-Digit Pin: ")
        if(user_check_in_pin == "q"):
            return
        if user_check_in_pin.isdigit() and len(user_check_in_pin) == 4:
            # Checking if the pin is correct
            if (user_check_in_pin == user_check_in_object["Pin"]):
                tran_his_exists = ""
                print(f"{long_div}\nWelcome {user_check_in_object["Name"]}\n{long_div}")
                user_pin_tries_pass = True
                # Transaction history
                global transaction_history
                global accessed
                if (accessed == "no"):
                    new_user_history = {user_check_in_object["Account No"]: []}
                    transaction_history.append(new_user_history)
                    accessed = "yes"
                    return
                if (accessed == "yes"):
                    for item in transaction_history:
                        if (list(item)[0] == user_check_in_object["Account No"]):
                            tran_his_exists = "yes"
                            return 
                    if (tran_his_exists == ""):
                        new_user_history = {user_check_in_object["Account No"]: []}
                        transaction_history.append(new_user_history)
                return
            pin_tries -= 1
            print(f"{long_div}\nUser Not Found!")
            print(f"{long_div}\nYou Have {pin_tries} tries left")
        elif user_check_in_pin.isdigit() and (len(user_check_in_pin) != 4):
            pin_tries -= 1
            print(f"{long_div}\nPlease Input a Valid Pin")
            print(f"{long_div}\nYou Have {pin_tries} tries left")
        else: 
            pin_tries -= 1
            print(f"{long_div}\nPlease Input Valid Digits")
            print(f"{long_div}\nYou Have {pin_tries} tries left")

   
      

# Check Current Balance Function
def check_current_balance(user_balance):
    print(f"{long_div}\nYour Current Account Balance is {user_balance:,.2f} Naira\n{long_div}")

# Withdraw Cash Function
def withdraw_cash(user_balance):
    while True:
        print("Press q to quit the action below")
        amount_to_be_withdrawn = input("Please Enter the Amount You Wish to Withdraw: ")
        if (amount_to_be_withdrawn == "q"):
            print("")
            return
        elif(amount_to_be_withdrawn == "0"):
            print(f"{long_div}\nAmount Must Be Greater Than Zero\n{long_div}")
        elif(amount_to_be_withdrawn.isdigit()) and int(amount_to_be_withdrawn) <= user_balance and int(amount_to_be_withdrawn) >= 50:
            amount_to_be_withdrawn = int(amount_to_be_withdrawn)
            print(f"{long_div}\n{amount_to_be_withdrawn:,.2f} Naira Has Been Successfully Withdrawn!\n{long_div}")
            break
        elif(amount_to_be_withdrawn.isdigit()) and int(amount_to_be_withdrawn) <= user_balance and int(amount_to_be_withdrawn) < 50:
            print(f"{long_div}\nThe Minimum Amount You Can Withdraw is 50 Naira\n{long_div}")
        elif((amount_to_be_withdrawn.isdigit()) and int(amount_to_be_withdrawn) > user_balance):
            print(f"{long_div}\nInsufficient Balance\n{long_div}")
            return
        else:
            print(f"{long_div}\nPlease Input a Valid Number\n{long_div}")
    new_balance = user_balance - amount_to_be_withdrawn
    user_check_in_object["Balance"] = new_balance
    for item in transaction_history:
        if (list(item)[0] == user_check_in_object["Account No"]):
            item[user_check_in_object["Account No"]].append(f"Withdrew {amount_to_be_withdrawn:,.2f} Naira")
    
# Deposit Cash Function
def deposit_cash(user_balance):
    while True:
        print("Press q to quit the action below")
        amount_to_be_deposited = input("Please Enter the Amount You Wish to Deposit: ")
        if (amount_to_be_deposited == "q"):
            print("")
            return
        elif(amount_to_be_deposited.isdigit() and int(amount_to_be_deposited) > 0):
            amount_to_be_deposited = int(amount_to_be_deposited)
            print(f"{long_div}\n{amount_to_be_deposited:,.2f} Naira Has Been Successfully Deposited!\n{long_div}")
            break
        elif(amount_to_be_deposited.isdigit() and int(amount_to_be_deposited) == 0):
            print(f"{long_div}\nYou Cannot Deposit 0 Naira!\n{long_div}")
        else:
            print(f"{long_div}\nPlease Input a Valid Number\n{long_div}")
    new_balance = user_balance + amount_to_be_deposited
    user_check_in_object["Balance"] = new_balance
    for item in transaction_history:
        if (list(item)[0] == user_check_in_object["Account No"]):
            item[user_check_in_object["Account No"]].append(f"Deposited {amount_to_be_deposited:,.2f} Naira")
    
# Change Pin Function
def change_pin():
    while True:
        while True:
            print("Press q to quit the action below")
            new_pin = input("Please Input Your New Pin: ")
            if (new_pin == "q"):
                print("")
                return
            elif(new_pin == user_check_in_object["Pin"]):
                print(f"{long_div}\nYour New Pin Cannot Be The Same As Your Old Pin\n{long_div}")
            elif (new_pin.isdigit() and len(new_pin) == 4):
                break
            elif (new_pin.isdigit() and len(new_pin) != 4):
                print(f"{long_div}\nYour New Pin Must Be 4 Digits!\n{long_div}")
            else:
                print(f"{long_div}\nPlease Input a Valid Pin\n{long_div}")

        confirm_new_pin = input("Confirm The Pin: ")
        if (confirm_new_pin == new_pin):
            user_check_in_object["Pin"] = new_pin
            print(f"{long_div}\nPin Successfully Changed!\n{long_div}")
            break
        else: 
            print(f"{long_div}\nThe Pins Did Not Match!\n{long_div}")

# Pay Bills Function
def pay_bills(user_balance):
    while True:
        print("Press q to quit the action below")
        amount_to_be_paid = input("Please Enter the Amount You Wish to Pay: ")
        if (amount_to_be_paid == "q"):
            print("")
            return
        elif(amount_to_be_paid == "0"):
            print(f"{long_div}\nAmount Must Be Greater Than Zero\n{long_div}")
        elif(amount_to_be_paid.isdigit()) and int(amount_to_be_paid) <= user_balance:
            amount_to_be_paid = int(amount_to_be_paid)
            print(f"{long_div}\n{amount_to_be_paid:,.2f} Naira Has Been Successfully Paid!\n{long_div}")
            break
        elif((amount_to_be_paid.isdigit()) and int(amount_to_be_paid) > user_balance):
            print(f"{long_div}\nInsufficient Balance\n{long_div}")
            return
        else:
            print(f"{long_div}\nPlease Input a Valid Number\n{long_div}")
    new_balance = user_balance - amount_to_be_paid
    user_check_in_object["Balance"] = new_balance
    for item in transaction_history:
        if (list(item)[0] == user_check_in_object["Account No"]):
            item[user_check_in_object["Account No"]].append(f"Paid {amount_to_be_paid:,.2f} Naira")

# Transaction History
def trans_history(): 
    print(f"{long_div}\n\t  TRANSACTION HISTORY\n{long_div}")
    for item in transaction_history:
        if (list(item)[0] == user_check_in_object["Account No"]):
            if(len(item[user_check_in_object["Account No"]]) == 0):
                print("You Have Not Made Any Transactions Yet")
            else:   
                for history in item[user_check_in_object["Account No"]]:
                    print(history)     
    print("") 

def runAtmApp():
    while True:
        login_page()
        if (login_pass):
            user_authentication()
            if (user_pin_tries_pass):
                action_input()

runAtmApp()