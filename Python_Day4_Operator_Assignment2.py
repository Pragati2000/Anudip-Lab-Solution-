#Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

# Get the age from the user
age = int(input("Enter your age: "))

# Check if the person is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

    
    
""" Output:
       Enter your age: 16
       You are not eligible to vote. """

