# Functions in python
# They are reusable codes
# Parameters are placeholders passed into the function when defining it
# A function is a name reusable

# Lambda functions NOTE: the other types of functions had been covered in the bro code tutorial
square = lambda x:x*x
print(square(5))
# It only works once

# Docstrings; used to add commment to a function
def add(*args):
    """Add all numbers"""
    return sum(args)

print(add(1,2,24,432))

# Math functions... just make reference to your slide and the bro code tutorial
# An extra one not there is:
remainder = divmod(17,5) 
print(remainder) # I believe it returns the number times the number goes for the first index and the remainder for the second index

import math
print(math.gcd(12,18)) # greatest common divisor, basically lcm
print(math.factorial(5))
print(math.sin(math.radians(120)))
# remember ceil rounds up while floor rounds down

# Exercise
def greet(name, greetings = "Hello"):
    print(greetings + " my name is " + name)

greet("Sinmi")
greet(greetings = "Hi!", name = "Joel")

# Function to return max of three numbers
def max_function(num_1, num_2, num_3):
    if num_1 >= num_2 and num_1 >= num_3:
        return num_1
    elif num_2 >= num_1 and num_2 >= num_3:
        return num_2
    else: 
        return num_3

print(f"The max of the numbers is: {max_function(200, 100, 1000)}")

# Lambda function
numbers = [10, 189, 56]
doubled_number = list(map(lambda x:x*2, numbers))
print(doubled_number)

# Recursive function to count from n to 0
def count_down(n):
    if n == 0:
        print(n)
        return 
    print(n)
    n -= 1
    count_down(n)

count_down(10)
