#Write a Python program to reverse words in a string 

#String = “Deeptech Python Training”


def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed list into a single string
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

# Given string
input_string = "Deeptech Python Training"

# Reverse the words in the string
reversed_string = reverse_words(input_string)

# Print the result
print(reversed_string)


#Output: Training Python Deeptech
