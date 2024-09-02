#Write a Python program to remove a newline in Python

#String = "\nBest \nDeeptech \nPython \nTraining\n" 


# Given string with newline characters
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters using split and join
cleaned_string = ''.join(string.splitlines())

# Print the result
print(cleaned_string)


#Output: Best Deeptech Python Training
