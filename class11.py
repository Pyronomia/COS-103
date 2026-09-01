import math
import numpy as np
# import 
# Matrices And Vectors
v = [3,4]

# Vector addition and subtraction
def add(u,v):
    return [a+b for  a, b in zip(u,v)]

def subtract(u,v):
    return [a-b for  a, b in zip(u,v)]
print(add([3,4], [6,7]))
print(subtract([3,4], [6,7]))

# Scalar multiplication
def scale(v, k):
    return[k * x for x in v]

print(scale([1,2], 4))
print(scale([1,2], 0.5))
# NOTE: When multiplying with a float, the output will be in float. But if multiplying an integer with an integer, it remains an integer

# Dot Product
def dot(u,v):
    return sum(a * b for a,  b  in zip(u,v))

print(dot([1,2,3], [4,5,6]))

# Magnitude and normalisation
def magnitude(v):
    return math.sqrt(sum(x ** 2 for x in v ))

print(magnitude([3,4])) # The output is going to be a float

def normalise(v): #basically unit vector
    m = magnitude(v) 
    return [x/m for x in v]

print(normalise([3,4]))

# Numpy - a library for numbers


# Matrix
A = [[1,2,3],
     [4,5,6]]

print(A[0]) 
print(A[0][2])

# Matric summation and multiplication... do it later
v = np.array([3,4])
w = np.array([5,6])


# Class Exercise
# Write a function that returns the angle-free 'distance' between two vectors
def distance(u,v):
    return math.sqrt(sum([(b-a)**2  for a,b in zip(u,v)]))
print(distance([3,4],[5,6]))

# Multiply a 2x2 matrix by a 2x1 vector by hand then check it with numpy
C = [[2,5],
     [1,9]]
D = [[7],
     [6]]
a = np.array(C)
b = np.array(D)

print(a @ b)

# Write a function that checks if a matrix is symmetric(equals its transpose)

def check_transpose(A):
    if A == [list(row) for row in zip(*A)]: 
        return "The matrix is symmetric"
    else: 
        return "The matrix is not symmetric"

D  = [[1,2,3],
      [4,5,6],
      [7,8,9]]
print(check_transpose(D))

# Use a scaling matrix [[2,0],[0,2]] to double the size of a shape's points
S = np.array([[2, 0], 
              [0, 2]])

points = np.array([
    [1, 2, 4],  
    [1, 3, 1] 
])

scaled_points = S @ points

print(f"Original points:\n {points}")
print(f"Scaled Points:\n {scaled_points}")