# CONDITIONAL STATEMENTS
""" if
if else 
if elif else
"""

# pass statement used as a placeholder when a statement is required but no action is to be performed

# Program using if..elif..else to find the maximum of four numbers
num_1 = float(input("Enter your 1st number: "))
num_2 = float(input("Enter your 2nd number: "))
num_3 = float(input("Enter your 3rd number: "))
num_4 = float(input("Enter your 4th number: "))

max_num = ""

if (num_1 >= num_2 and num_1 >= num_3 and num_1 >= num_4 ):
    max_num = num_1
elif (num_2 >= num_1 and num_2 >= num_3 and num_2 >= num_4 ):
    max_num = num_2
elif (num_3 >= num_1 and num_3 >= num_2 and num_3 >= num_4 ):
    max_num = num_3
else:
    max_num = num_4
print("The maximum number is: ", max_num)




# Program to calculate a simple login
saved_username = "sinmi"
saved_password = "password"

username = input("Input your username: ")
password = input("Input your password: ")

if (username == saved_username and password == saved_password):
    print("You have successfully logged in")
else:
    print("Invalid username or password")