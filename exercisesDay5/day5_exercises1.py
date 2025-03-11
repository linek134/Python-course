#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 12:08:16 2025

@author: linnekst
"""
import numpy as np
from scipy.linalg import solve
import pandas as pd

#1. Scipy

A = np.array([[1, -2, 3],  #1a
              [4, 5, 6],
              [7, 1, 9]])

B = np.array([1, 2, 3]) #1b

x = solve(A, B) #1c

#Calculate dotproduct using numpy
# Ax = B
solution = np.dot(A,x) #1d

print("Solution x:", x)
print("Computed b (A * x):", solution)
print("Given B:", B)

#%%
#1e
A = np.array([[1, -2, 3],
              [4, 5, 6],
              [7, 1, 9]])

B = np.random.randint(9, size=(3, 3))

x = solve(A, B)
solution = np.dot(A,x)
 
# print("Solution x:", x)

print("Computed b (A * x):", solution)
print("Input B:", B)

#%%
#1f
from scipy.linalg import eig

#from scipy.linalg import eig

A = np.array([[1, -2, 3],  #1a
              [4, 5, 6],
              [7, 1, 9]])

eigenvalues, eigenvectors = eig(A)

print("Eigenvalues for matrix A:", eigenvalues)
print("Eigenvectors for matrix A:", eigenvectors)

#%%
#1g. Calculate the inverse, determinant of A
from scipy.linalg import inv, det

inverse = inv(A)
determinant = det(A)

print("Inverse of A:", inverse)
print("Determinant of A:", determinant)
#%%
#1h. Calculate the norm of A with different orders
from scipy.linalg import norm

Anorm1 = norm(A, 1) #max(sum(abs(a), axis=0))
Anorm2 = norm(A, -1) #min(sum(abs(a), axis=0))
Anorm3 = norm(A, 2) #2-norm (largest sing. value)
Anorm4 = norm(A, -2) #smallest singular value

print("1-Norm (Max column sum):", Anorm1)
print("-1norm (Min column sum): ", Anorm2)
print("2-norm (largest sing. value):", Anorm3)
print("-2norm: (smallest singular value)", Anorm4)



#%%
# Statistics
# a.Create a discrete random variable with poissonian distribution and plot its probability mass function (PMF), cummulative distribution function (CDF) and a histogram of 1000 random realizations of the variable
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

mu = 5  
x = np.arange(0, 20)

pmf_values = poisson.pmf(x, mu)
cdf_values = poisson.cdf(x, mu)

# generate 1000 random samples from a poisson distribution
r = poisson.rvs(mu, size=1000)

# Plot PMF, CDF and histogram in 3 different subplots
# Plot PMF
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.bar(x, pmf_values, color='red', alpha=0.5)
plt.xlabel("x")
plt.ylabel("PMF")
plt.title("Poisson PMF")

# Plot CDF
plt.subplot(1, 3, 2)
plt.plot(x, cdf_values, marker="o", linestyle="-", color='green')
plt.xlabel("x")
plt.ylabel("CDF")
plt.title("Poisson CDF")

# Plot histogram
plt.subplot(1, 3, 3)
plt.hist(r, bins=np.arange(0, 20), alpha=0.5, color='blue')
plt.xlabel("x")
plt.ylabel("Frequency")
plt.title("Histogram of 1000 Samples")

plt.show()

#%%
# b. Create a continious random variable with normal distribution and plot its probability mass function (PMF), cummulative distribution function (CDF) and a histogram of 1000 random realizations of the variable
from scipy.stats import norm
r2 = norm.rvs(size=1000)

mu = -2  
x2 = np.arange(-5, 5)

pmf_values = norm.pdf(x2, mu)
cdf_values = norm.cdf(x2, mu)

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.bar(x2, pmf_values, color='red', alpha=0.5)
plt.xlabel("x")
plt.ylabel("PMF")
plt.title("Norm PMF")

# Plot CDF
plt.subplot(1, 3, 2)
plt.plot(x2, cdf_values, marker="o", linestyle="-", color='green')
plt.xlabel("x")
plt.ylabel("CDF")
plt.title("Norm CDF")

# Plot histogram
plt.subplot(1, 3, 3)
plt.hist(r2, bins=np.arange(-5, 5), alpha=0.5, color='blue')
plt.xlabel("x")
plt.ylabel("Frequency")
plt.title("Histogram of 1000 Samples")

plt.show()

#%%
#c  Test if two sets of (independent) random data comes from the same distribution
from scipy import stats
result = stats.ttest_ind(r, r2)
print(result)