"""Write a Python program to Return a set of elements present in Set A or B, but not both. Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} Output: {20, 70, 10, 60}"""


# Define the two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Get elements that are in either set1 or set2, but not in both
symmetric_difference = set1.symmetric_difference(set2)

# Output the result
print(symmetric_difference)


#Output:{20, 70, 10, 60}
