print("Amigos! I am practicing python programming")

# Create a simple calculator that takes user input for two numbers and an operator then prints the result
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operator = input("Enter your desired operation(+,-,/,*): ")
result = ""

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    result = num1 / num2
elif operator == "*":
    result = num1 * num2
else:
    print("Please input a valid operator")

print(num1, operator, num2, "=", result)