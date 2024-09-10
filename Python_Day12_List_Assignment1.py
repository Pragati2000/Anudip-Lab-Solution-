#Write a Python program to sum all the items in a list.


def sum_of_list(items):
    total = 0
    for item in items:
        total += item
    return total

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = sum_of_list(my_list)
print("The sum of the list is:", result)


#Output:The sum of the list is: 15
