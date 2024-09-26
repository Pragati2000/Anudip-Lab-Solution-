"""Visualize the daily temperature changes over time in a city and give your conclusion

 Input: days = list(range(1, 32)) 

# Daily temperature data (replace with your own data) 

temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]"""


# Importing necessary library
import matplotlib.pyplot as plt

# Input data
days = list(range(1, 32))  # Days of the month
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]
# Daily temperatures

# Create a line chart to represent daily temperature changes
plt.plot(days, temperature, marker='o', linestyle='-', color='orange', label='Temperature')

# Adding titles and labels
plt.title('Daily Temperature Changes Over Time')
plt.xlabel('Days of the Month')
plt.ylabel('Temperature (°F)')
plt.grid(True)

# Show the plot
plt.show()
