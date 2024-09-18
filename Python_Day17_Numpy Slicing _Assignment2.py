#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np

# Create a 3x3 matrix with values ranging from 2 to 10
matrix_3x3 = np.arange(2, 11).reshape(3, 3)

# Print the matrix
print("3x3 Matrix with values from 2 to 10:")
print(matrix_3x3)


"""Output: 3x3 Matrix with values from 2 to 10:
              [[ 2  3  4]
               [ 5  6  7]
               [ 8  9 10]]"""
