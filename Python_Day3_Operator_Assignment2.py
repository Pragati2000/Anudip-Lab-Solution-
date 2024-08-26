#Using input function take two number and then swap the number


# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display the numbers before swapping
print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swap the numbers
num1, num2 = num2, num1

# Display the numbers after swapping
print(f"After swapping: num1 = {num1}, num2 = {num2}")


"""output  
   Enter the first number: 45
   Enter the second number: 23
   Before swapping: num1 = 45, num2 = 23
   After swapping: num1 = 23, num2 = 45"""
    
