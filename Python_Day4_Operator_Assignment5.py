#Write a Python program that determines the largest of three numbers entered by the user.

# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the result
print(f"The largest number is: {largest}")



""" Output:
        Enter the first number: 2
        Enter the second number: 5
        Enter the third number: 9
        The largest number is: 9.0 """
