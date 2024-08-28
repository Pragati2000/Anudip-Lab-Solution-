#Declare a div() function with two parameters. Then call the function and pass two numbers and display their division

def div(a, b):
# Check if the divisor is not zero to avoid ZeroDivisionError
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return
    
# Perform the division and print the result
    result = a / b
    print(f"The division of {a} by {b} is: {result}")

# Call the function with two numbers
div(10, 2)



# Output: The division of 10 by 2 is: 5.0
