"""Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school. Also generate a horizontal bar chart based on the result and explain the conclusion.

 Input: student_data = pd.DataFrame({ 'school_code': ['s001','s002','s003','s001','s002','s004'],

 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 

'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 

'age': [12, 12, 13, 13, 14, 12], 

'height': [173, 192, 186, 167, 151, 159], 

'weight': [35, 32, 33, 30, 31, 32], 

'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, )"""


import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group the data by 'school_code' and calculate mean, min, and max age
school_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

# Print the results
print("School Statistics:")
print(school_stats)

# Create a horizontal bar chart
school_stats.plot(kind='barh', figsize=(10, 6))
plt.xlabel("Age")
plt.ylabel("School Code")
plt.title("Age Statistics by School")
plt.show()


"""Output:
School Statistics:
             mean  min  max
school_code                
s001         12.5   12   13
s002         13.0   12   14
s003         13.0   13   13
s004         12.0   12   12"""