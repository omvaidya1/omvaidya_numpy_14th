import numpy as np

# Create a 1D array from 1 to 24
arr = np.arange(1, 25)

print("Original Array:")
print(arr)
print("Shape:", arr.shape)

# Reshape into (4, 6)
reshape_1 = arr.reshape(4, 6)
print("\nReshaped into (4, 6):")
print(reshape_1)
print("Shape:", reshape_1.shape)

# Reshape into (3, 8)
reshape_2 = arr.reshape(3, 8)
print("\nReshaped into (3, 8):")
print(reshape_2)
print("Shape:", reshape_2.shape)

# Reshape into (2, 3, 4)
reshape_3 = arr.reshape(2, 3, 4)
print("\nReshaped into (2, 3, 4):")
print(reshape_3)
print("Shape:", reshape_3.shape)