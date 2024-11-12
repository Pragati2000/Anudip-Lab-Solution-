"""Using SciPy Linear Algebra please solve the below problem. Input: 7x + 2y = 8 4x + 5y = 10"""

import numpy as np
from scipy.linalg import solve

# Coefficient matrix A
A = np.array([[7, 2],
              [4, 5]])

# Right-hand side matrix B
B = np.array([8, 10])

# Solve the system of linear equations
solution = solve(A, B)

# Print the solution
x, y = solution
print(f'Solution: x = {x}, y = {y}')


#Output:Solution: x = 0.7407407407407407, y = 1.4074074074074074
