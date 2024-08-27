#Write a Python program that determines if a given year is a leap year or not.

# Get the year from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


""" Output:
        Enter a year: 2023
        2023 is not a leap year. """
