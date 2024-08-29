#Write a python program finding the factorial of a given number using a while loop


def factorial(n):
# Initialize result as 1 (the factorial of 0 and 1 is 1)
    result = 1
    
# Use a while loop to calculate factorial
    while n > 0:
        result *= n  # Multiply result by the current value of n
        n -= 1       # Decrease n by 1
       
    return result

# Example usage
number = int(input("Enter a number to find its factorial: "))

# Ensure the number is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial(number)}.")


""" Output:
          Enter a number to find its factorial: 12
          The factorial of 12 is 479001600. """
