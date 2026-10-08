num = float(input("Enter a number: "))

if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else: 
    print(num, "is zero")


# Password strength checker
password = input("Enter your password: ")
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*._-/"
uppercase_check = False
lowercase_check = False
digit_check = False
symbol_check = False
length_check = False
for char in password:
    if char in uppercase_letters:
        uppercase_check = True
    if char in lowercase_letters:
        lowercase_check = True
    if char in digits:
        digit_check = True
    if char in symbols:
        symbol_check = True
if len(password) >= 8:
    length_check = True

if uppercase_check and lowercase_check and digit_check and symbol_check and length_check:
    print("Your password is very strong")
else:
    print("Your password is weak")

score = int(input("Enter a score: "))
if score >= 70 and score <= 100:
    print("Your Grade is A")
elif score >= 60:
    print("Your Grade is B")
elif score >= 50:
    print("Your Grade is C")
elif score >= 45:
    print("Your Grade is D")
elif score >= 40:
    print("Your Grade is E")
elif score >= 0:
    print("Your Grade is F")
else: 
    print("Invalid score")