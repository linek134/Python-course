import random

N = 250

# Generate NxN matrix X
X = [[random.randint(0, 100) for _ in range(N)] for _ in range(N)]

# Generate Nx(N+1) matrix Y
Y = [[random.randint(0, 100) for _ in range(N+1)] for _ in range(N)]

# Initialize result matrix
result = [[0] * (N+1) for _ in range(N)]

@profile
def matrix_multiplication():
    for i in range(len(X)):  # Iterate through rows of X
        for j in range(len(Y[0])):  # Iterate through columns of Y
            for k in range(len(Y)):  # Iterate through rows of Y
                result[i][j] += X[i][k] * Y[k][j]

# Run the function
matrix_multiplication()

# Print result
for r in result:
    print(r)
