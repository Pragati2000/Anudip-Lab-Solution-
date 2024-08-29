#Write a python program to check whether a number is palindrome or not?

def is_palindrome(number):
# Convert the number to a string to easily check for palindrome
    num_str = str(number)
    
# Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Example usage
number = int(input("Enter a number: "))

if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


""" Output:
         Enter a number: 12321
         12321 is a palindrome. """
