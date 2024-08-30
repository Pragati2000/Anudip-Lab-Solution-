#Python program to check if the given string is a palindrome

def is_palindrome(s):
# Remove spaces and convert to lowercase for consistent comparison
    s = s.replace(" ", "").lower()
    
# Initialize two pointers
    left = 0
    right = len(s) - 1
    
# Check characters from both ends towards the center
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Input from the user
input_string = input("Enter a string to check if it is a palindrome: ")

# Check and display the result
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
    


""" Output:
         Enter a string to check if it is a palindrome: 12521
         "12521" is a palindrome. """
