import numpy as np

# Create a 4x5 matrix of random integers between 20 and 80
matrix = np.random.randint(20, 81, size=(4, 5))

# Print the matrix
print("4x5 Matrix:")
print(matrix)

# Statistical methods for the entire matrix
print("\nMinimum Value:", np.min(matrix))
print("Maximum Value:", np.max(matrix))
print("Sum of All Elements:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Standard Deviation:", np.std(matrix))

# Row-wise sum
print("\nSum of Each Row:")
print(np.sum(matrix, axis=1))

# Column-wise sum
print("\nSum of Each Column:")
print(np.sum(matrix, axis=0))