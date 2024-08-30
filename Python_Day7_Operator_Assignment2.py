# Python program to check if a given number is an Armstrong number

def is_armstrong_number(num):
# Convert the number to a string to easily iterate over digits
    num_str = str(num)
# Find the number of digits
    num_digits = len(num_str)
    
# Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
# Check if the sum is equal to the original number
    return sum_of_powers == num

# Input from the user
input_number = int(input("Enter a number to check if it is an Armstrong number: "))

# Check and display the result
if is_armstrong_number(input_number):
    print(f"{input_number} is an Armstrong number.")
else:
    print(f"{input_number} is not an Armstrong number.")


""" Output:
         Enter a number to check if it is an Armstrong number: 370
         370 is an Armstrong number. """
