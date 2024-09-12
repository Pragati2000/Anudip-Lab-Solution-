"""Write a Python program and calculate the mean of the below dictionary.

 test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

Output: 6.2"""


# Given dictionary
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

# Calculate the mean
mean_value = sum(test_dict.values()) / len(test_dict)

# Print the mean value
print("The mean value is:", mean_value)


#Output:The mean value is: 6.2
