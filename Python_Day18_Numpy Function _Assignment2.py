"""Suppose you have a dataset containing monthly sales data for a company, and you want to split this data into quarterly reports for analysis and reporting purposes. 

Input: monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])"""


import numpy as np

# Monthly sales data
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

# Split data into quarters
quarter1 = monthly_sales[0:3]
quarter2 = monthly_sales[3:6]
quarter3 = monthly_sales[6:9]
quarter4 = monthly_sales[9:12]

# Output the results in the desired format
print("Quarter 1 Sales (in thousands of dollars):")
print(quarter1)

print("\nQuarter 2 Sales (in thousands of dollars):")
print(quarter2)

print("\nQuarter 3 Sales (in thousands of dollars):")
print(quarter3)

print("\nQuarter 4 Sales (in thousands of dollars):")
print(quarter4)


"""Output:
        Quarter 1 Sales (in thousands of dollars):
        [120 135 148]

        Quarter 2 Sales (in thousands of dollars):
        [165 180 155]

        Quarter 3 Sales (in thousands of dollars):
        [168 190 205]

        Quarter 4 Sales (in thousands of dollars):
        [198 210 225]
