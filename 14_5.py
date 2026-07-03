import numpy as np

# Given array
arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

print("Original Array:")
print(arr)

# 1. Extract first row
first_row = arr[0]
print("\nFirst Row:")
print(first_row)

# 2. Extract last column
last_column = arr[:, -1]
print("\nLast Column:")
print(last_column)

# 3. Extract center 2x2 submatrix
# From rows 1 to 2 (index 0-based), columns 1 to 2
center_submatrix = arr[0:2, 1:3]
print("\nCenter 2x2 Submatrix:")
print(center_submatrix)

# 4. Extract all even numbers using boolean indexing
even_numbers = arr[arr % 2 == 0]
print("\nEven Numbers in Array:")
print(even_numbers)