# 10TH APRIL, 2026
# Exercise
# Program to check if a number is even or odd
num = int(input("Enter your number: "))
if (num % 2 == 0 ):
    print("The number is even")
else:
    print("The number is odd")

# Program to check if a number is positive, negative or zero
num_2 = int(input("Enter your number: "))
if (num_2 > 0):
    print("The number is positive")
elif (num_2 < 0):
    print("The number is negative")
else :
    print("The number is zero")

# Program to count the number of vowels in a string
word = input("Enter a string: ")

# string containing all vowels
vowels = "aeiouAEIOU"

# counting the number of vowels
vowel_count = 0
for i in range(len(word)):
    if (word[i] in vowels):
        print(i)
        vowel_count += 1

print("The number of vowel(s) in the string is/are: ", vowel_count)