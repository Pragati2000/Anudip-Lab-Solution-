#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.


def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"The result is {result}"

# Example usage:
numerator = 10
denominator = 0

print(divide_numbers(numerator, denominator))


#output:Error: Division by zero is not allowed.
