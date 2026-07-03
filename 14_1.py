import numpy as np

# Generate a 1D array of 20 random numbers between 1 and 50
array = np.random.randint(1, 51, size=20)

# Print the array
print("Generated Array:")
print(array)

# Statistical methods
print("\nMinimum Value:", np.min(array))
print("Index of Minimum Value:", np.argmin(array))

print("\nMaximum Value:", np.max(array))
print("Index of Maximum Value:", np.argmax(array))

print("\nSum of All Elements:", np.sum(array))

print("Mean:", np.mean(array))
print("Standard Deviation:", np.std(array))
