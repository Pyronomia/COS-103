#fun code
print("I'm writing my first python program")
print(5+2)
# This is a comment haha
print("Hello World")
name = "Sinmi"
print(name)
firstValue = 2
secondValue = 5
print(firstValue + secondValue)
def add(a, b):
    return a + b
print (add(5,7))

# SYNTAX ERRORS IN PYHTON
# 1. Lack of parenthesis
# 2. Incorrect use of words or keywords e.g def = 10
# 3. Missing colon e.g if x>10
# print("hello") note.. there's a missing colon there
# e.g.2 def COS103()
#print("Hello")
# 4. Indentation error e.g if x ==3:
                        #  print('Hello') 
# 5. Unterminated string literal (Unmatched parenthesis)
# 6. Extra or missing bracket
# 7. Incorrect function definition
# 8. Use of special characters in declaring a variable and numbers at the end of letters.. invalid variable name e.g 2name = "jene"
# 9. Using commas in a list
# # 10. Type error e.g
# score = 70
# print("you score = " + score)
# ii. Wrong number of arguments
# 11. zero division e.g x = 10/0
# 12. Index Error number1 = [1,2,3,4] 
# print(number1[2])
# 13. Key Error student = {"name": "John"}
#print(student["age"])

# 14. Attribute Error 
# x = 10
# x.append(5)
# print(x)

# 15. Import error e.g from math import square
# 16. Module not found error
# 17. Value error
# 18. infinite loop e.g while True:
    # print("Hello")
# 19. Forgetting the return syntax in your code
valeef = 10
print(valeef)

def COS103():
    print("Hello")
COS103()
num = [1, 2, 3]

print(num)

score = 70
print("you score = ", score)
len({1,2,3})

# x = 10/0
# print(x)

number1 = [1,2,3,4] 
print(number1[2])

student = {"name": "John"}
print(student["name"])

x = [10]
x.append(5)
print(x)

from math import sqrt

# import numpy

x =int("20")
print(x)
counter = 0
while counter < 5:
    print("Hello")
    counter += 1

def add(a,b):
    c= a + b 
    return c
    #if return is in a function you dont need print but if print is there you can just call the function normally
print(add(3,2))

# EXERCISE
pi = 3.142
d =  12  
r = d/2

def circum():
    c = 2 * pi * r
    return c
print("Your score = ", circum())