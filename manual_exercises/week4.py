word = input("Enter your word: ")
reversed_word = word[::-1]
print("Your reversed word is:",reversed_word)

if word == reversed_word:
    print(word,"is a palindrome")
else:
    print(f"{word} is not a palindrome")

# Old Style formatting
name = "Sinmi"
age = 18
print("My name is %s and I am %d years old"%(name,age))

# Format() method
print("My name is {} and I am {} years old".format(name,age))
# f string method
print(f"My name is {name} and I am {age} years old")


hangman_word = "batman"
user_guess = "______"
chances = 6
while True:
    if chances == 0:
        break
    choice = input("1 to guess a letter, 2 to guess the full word: ")
    if choice == "1":
        guess = input("Enter a letter you think is in the word: ")
        if guess in hangman_word:
            index = 0
            for char in hangman_word:
                if guess == char:
                    user_guess = user_guess[:index] + guess + user_guess[index + 1:]
                index += 1
            print(user_guess)
        else:
            chances = chances - 1
            print(f"You have {chances} chances left")
    elif choice == "2":
        guess = input("Enter your guess: ")
        if guess == hangman_word:
            print("You have successfully gotten the word!")
            chances = 0
        else:
            chances = chances - 1
            print(f"You have {chances} chances left")