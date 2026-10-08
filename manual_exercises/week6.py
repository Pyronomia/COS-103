# Program to print prime numbers up to a certain number
number = int(input("Enter a number: "))
print(f"Prime numbers to {number}")
for i in range(number+1):
    prime = True
    if i < 2:
        prime = False
    for j in range(2,i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)

# Multiplication table
for i in range(1,13):
    for j in range(1,13):
        print(f"{i}*{j} = {i*j}")

# Python guessing game
lowest_num = 1
highest_num = 100
answer = 56
guesses = 0
running = True

print("Python Number Guessing Game")
print((f"Select a number between {lowest_num} and {highest_num}"))

while running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low, Try again")
        elif guess > answer: 
            print("Too high,Try again")
        else: 
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            running = False
    else:
        print("invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")