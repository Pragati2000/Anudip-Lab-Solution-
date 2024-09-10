#Write a Python program to get the largest and smallest number from a list without builtin functions.

def find_largest_and_smallest(numbers):
    if not numbers:  # Check if the list is empty
        return None, None

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest

# Example usage:
my_list = [3, 5, 1, 8, 2, -4, 7]
largest, smallest = find_largest_and_smallest(my_list)
print("The largest number is:", largest)
print("The smallest number is:", smallest)


"""Output:
          The largest number is: 8
          The smallest number is: -4 """
