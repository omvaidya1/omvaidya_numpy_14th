import numpy as np

# Create a 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, size=(5, 5))

print("Original Matrix:")
print(matrix)

# 1. Diagonal elements
diagonal = np.diag(matrix)
print("\nDiagonal Elements:")
print(diagonal)

# 2. Elements greater than 50
greater_than_50 = matrix[matrix > 50]
print("\nElements Greater Than 50:")
print(greater_than_50)

# 3. Replace elements less than 30 with 0
matrix[matrix < 30] = 0

print("\nModified Matrix (elements < 30 replaced with 0):")
print(matrix)