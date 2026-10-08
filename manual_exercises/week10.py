import numpy as np
u = np.array([1,2])
v = np.array([3,4])
u[0] = 5

print(u + 5)
print(u + v)
print(u*v)

a = np.array([[4,3],
             [9,7]])

b = np.array([[8,1],
             [2,5]])

print(a@b)