#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 14:00:24 2025

@author: linnekst
"""

"""2. Numpy exercises"""
import numpy as np
#1a. Create a null vector of size 10 but the fifth value which is 1

a = np.zeros(10)
a[4] = 1
print(a)

#%%
#b. Create a vector with values ranging from 10 to 49
a = np.arange(49)[10:50]
print (a)

#%%
#c. Reverse a vector (first element becomes last)
a = np.arange(10)[::-1]
print(a)

#%%
#d. Create a 3x3 matrix with values ranging from 0 to 8
a = np.arange(9).reshape(3,3)
print(a)

#%%
#e. Find indices of non-zero elements from [1,2,0,0,4,0]
a = np.array([1,2,0,0,4,0])
b = a != 0
print(b)

#%%
#f. Create a random vector of size 30 and find the mean value
a = np.random.rand(30)
mean_a=np.mean(a)
print(mean_a)

#%%
#g. Create a 2d array with 1 on the border and 0 inside
a = np.arange(16).reshape(4,4)
a[:, :] =1
a[1:3, 1:3] = 0
print(a)


#%%
#h. Create a 8x8 matrix and fill it with a checkerboard pattern
a = np.zeros((8, 8), dtype=int)
a[1::2, ::2] = 1  # Setting alternate rows starting from the second row with alternate columns to 1
a[::2, 1::2] = 1
print(a)

#%%
#i. Create a checkerboard 8x8 matrix using the tile function
a= np.array([[1, 0],
             [0, 1]])

a = np.tile(a, (4, 4))
print(a)

#%%
#j. Given a 1D array, negate all elements which are between 3 and 8, in place
Z = np.arange(11)
Z[3:8] *= -1
print(Z)

#%%
#k. Create a random vector of size 10 and sort it
Z = np.random.random(10)
Z = np.sort(Z)
print(Z)

#%%
#l. Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A,B) 
print(equal)

#%%
#m. How to calculate the square of every number in an array in place (without creating temporaries)?
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = Z**2
print(Z.dtype)

#%%
#n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diagonal(C)
print(D)

#%%
"""3. Speed optimization using Numpy"""
import random
import numpy as np

N = 250

# Generate NxN matrix X
X = np.random.randint(0, 101, size=(N, N))

# Generate Nx(N+1) matrix Y
Y = np.random.randint(0, 101, size=(N, N + 1))

# Perform matrix multiplication using NumPy's dot product
def matrix_multiplication():
    result = np.dot(X, Y)
    return result

result = matrix_multiplication()

#%%