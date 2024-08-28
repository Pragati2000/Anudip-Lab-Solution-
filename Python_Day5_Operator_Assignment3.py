# Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random

# Generate 5 random numbers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(5)]

# Find the maximum and minimum values
maximum = max(numbers)
minimum = min(numbers)

# Display the results
print(f"Generated numbers: {numbers}")
print(f"Maximum number: {maximum}")
print(f"Minimum number: {minimum}")



""" Output:
        Generated numbers: [97, 65, 50, 48, 50]
        Maximum number: 97
        Minimum number: 48 """
