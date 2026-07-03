import numpy as np

# Define matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# 1. Element-wise multiplication
elementwise = A * B
print("\nElement-wise Multiplication (A * B):")
print(elementwise)

# 2. Matrix multiplication
matmul = A @ B   # or np.dot(A, B)
print("\nMatrix Multiplication (A @ B):")
print(matmul)

"""
Explanation:
- Element-wise multiplication (A * B) multiplies corresponding elements:
  Example: A[0][0] * B[0][0]

- Matrix multiplication (A @ B) follows linear algebra rules:
  Row of A × Column of B → sum of products
"""