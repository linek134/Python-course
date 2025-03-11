import random
import numpy as np

N = 250

# Generate NxN matrix X
X = np.random.randint(0, 101, size=(N, N))

# Generate Nx(N+1) matrix Y
Y = np.random.randint(0, 101, size=(N, N + 1))

# Perform matrix multiplication using NumPy's dot product
@profile
def matrix_multiplication():
    result = np.dot(X, Y)
    return result

result = matrix_multiplication()
