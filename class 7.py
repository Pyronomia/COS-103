fruits = ["apple", "banana", "orange"]
fruits[1] = "mango"
print(fruits)

# Adding Items To a List
fruits.append("grape") # adds to the end of the list 
print(fruits)
fruits.insert(1, "guava") # at a particular index
print(fruits)
fruits.extend(["pear", "melon"])
print(fruits)

# Removing elements
fruits.remove("apple")
print(fruits)
print(fruits.pop())
print(fruits)

# 8. Sorting Lists
# Ascending:
numbers = [4,2,8,1]
# numbers.sort()
# print(numbers)
# # Descending:
# numbers.sort(reverse=True)
# print(numbers)

#Sorted without changing original:
new_list = sorted(numbers)
print(new_list)
print(numbers)


# Looping through a list
for fruit in fruits:
    print(fruit)

print(range(len(fruits)))

for i in range(len(fruits)):
    print(fruits[i])

# shorter way of writing a full for loop for this 
squares = [x**2 for x in range(5)]
print(squares)

# Nested Lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[1][2])

# 12. Copying Lists
 #Problem:
a = [1,2,3]
b = a # when changing b, a also changes because they both point to the same list in memory
b[0] = 100
print(a)   # [100,2,3]
# Correct Copy:
b = a.copy()
print(b)
# OR
b = a[:]
print(b)

# z = [1,2,3] * 3 achieves the same thing
z = [1,2,3]
print(z * 3)

# Built in functions

numbers_1 = [4,2,8,1]
print(len(numbers_1))   # Length
print(max(numbers_1))   # Maximum
print(min(numbers_1))   # Minimum
print(sum(numbers_1))   # Sum

# numbers_2 = [4,"boy",8,1] 
# print(sum(numbers_2)) # prints an error

# Example 3: Remove Duplicates
numbers_3 = [1,2,2,3,4,4]
print(set(numbers_3))
unique = list(set(numbers_3))
print(unique)
