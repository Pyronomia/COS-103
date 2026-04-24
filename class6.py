# text = "Python"
# print(f"{text:<10}") # Left aligned
# print(f"{text:>10}") # Right aligned
# print(f"{text:^10}") # Center aligned
# print('\nisn\'t \tit')

# # raw strings
# path = r"C:\Users\Name\Documents"
# print(path)

# text = "J" + text[1:]
# print(text)
    # reversed_string += string[len(string) - (i+1)] 

# Exercise 
# Reverse a string without slicing
string = input("Enter your word: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string

print(f"The reverse of {string} is {reversed_string}")

# Program to count the number of words in a sentence
sentence = input("Enter your sentence: ")
number_of_words = len(sentence.split())
print(f"The number of words in the sentence is {number_of_words}")

# Program to replace all vowels in a word with *
word = input("Enter a word/sentence: ")
vowels = "aeiouAEIOU"

# i = 0
# while i < len(word):
#     if word[i] in vowels:
#         word = word[:i] + "*" + word[i+1:]
        
#     i+=1
# print(word)

for i in range(len(word)):
    if word[i] in vowels:
        word = word[:i] + "*" + word[i+1:]

print(word)