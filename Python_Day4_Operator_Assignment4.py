#Create a Python program that checks if a user-given number is positive, negative, or zero.

# Get the number from the user
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    

""" Output:
        Enter a number: 0
        The number is zero."""
