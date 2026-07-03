import numpy as np

# Generate a 6x6 matrix using np.random.randn()
matrix = np.random.randn(6, 6)

print("Original Matrix:")
print(matrix)

# Shape, size, dtype
print("\nShape:", matrix.shape)
print("Size:", matrix.size)
print("Data Type (dtype):", matrix.dtype)

# Index of maximum and minimum values
max_index = np.unravel_index(np.argmax(matrix), matrix.shape)
min_index = np.unravel_index(np.argmin(matrix), matrix.shape)

print("\nIndex of Maximum Value:", max_index)
print("Index of Minimum Value:", min_index)

# Top-left 3x3 submatrix
submatrix = matrix[:3, :3]
print("\nTop-left 3x3 Submatrix:")
print(submatrix)

# Replace negatives with absolute values
matrix = np.abs(matrix)

print("\nMatrix after replacing negative values:")
print(matrix)

# Mean of modified matrix
print("\nMean of Modified Matrix:", np.mean(matrix))