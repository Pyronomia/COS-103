numbers = [0,1,2,3,4,5]
print(numbers[::1])
print(numbers[::-1])
print(6 in numbers)
print(3 in numbers)

fruits = ["apple", "banana", "guava"]
for fruit in fruits:
    print(fruit)

single = (5,) # if you want to have only one tuple, a leading comma is required
single_2 = [5] # its not the same case with a list
single_3 = {5} # its not the same case with a set
print(single)
print(single_2)
print(single_3)

# Lists, Tuple and sets.. yes again :(
dupli_tuple = (1,1,1)
print(dupli_tuple)
# Lists are ordered, mutable and can have duplicates
# Tuples are ordered, immutable and can also have duplicates

# Packing & unpacking
coords = 12.9716, 77.5946
lat, lon = coords
# Multiple return values
def min_max(nums):
 return min(nums), max(nums)
print(min_max([4,1,9,2]))
low, high = min_max([4, 1, 9, 2])

# Tuple packing
tuple_1 = 1,2,3
print(tuple_1)
# Tuple unpacking NOTE: it's basically like a destructuring asssignment in JavaScript
# You can use an _ if you want to throw away values
a,b,c = tuple_1
print(a)

# Slicing in tuples
# [start:stop:step]
# starts at the actual start value but stops an index before the stop index
print(fruits[0:3:3])

# Concatenation
print(dupli_tuple + tuple_1)
# Repitition
print((1,2)*3)
# Membership: verifying that a variable appears in a tuple... returns a boolean; true or false
print(2 in dupli_tuple)
# len gives the length of a variable
# count checks the number of times a particular element appears in a variable
fruits_tup = ("apple", "banana", "mango", 1, 2, 3)
print(fruits_tup.count("apple"))

for number in fruits_tup:
    print(number)

# A list can be converted to a tuple
list_1 = [1,2,3]
tuple_convert = tuple(list_1)
print(tuple_convert)

# Advantages of Tuples
# faster, safer, used for finding geographical location, RGB color values can be stored