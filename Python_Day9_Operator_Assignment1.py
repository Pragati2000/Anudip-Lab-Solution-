#Write a Python program to Count all letters, digits, and special symbols from the given string

#Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3  


def count_using_lists(input_string):
# Separate characters into lists
    chars_list = [char for char in input_string if char.isalpha()]
    digits_list = [char for char in input_string if char.isdigit()]
    symbols_list = [char for char in input_string if not char.isalnum()]
    
# Count the length of each list
    chars_count = len(chars_list)
    digits_count = len(digits_list)
    symbols_count = len(symbols_list)
    
    return chars_count, digits_count, symbols_count

# Input String
input_string = "P@#yn26at^&i5ve"

# Counting using the list comprehension method
chars, digits, symbols = count_using_lists(input_string)

print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")



""" Output:
         Chars = 8
         Digits = 3
         Symbols = 4 """
