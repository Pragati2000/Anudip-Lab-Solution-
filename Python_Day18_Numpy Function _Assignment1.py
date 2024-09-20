""" Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

Input:

temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,4,25,12,-4,-12])"""


import numpy as np

# Temperature data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4, 25, 12, -4, -12])

# Identify hot and cold days
hot_days = np.where(temperatures > 35)[0]  # Days with temperature > 35°C
cold_days = np.where(temperatures < 5)[0]  # Days with temperature < 5°C

# Output the results in the desired format
print("Hot Days:")
print("Day\tTemperature (°C)")
for day in hot_days:
    print(f"{day+1}\t{temperatures[day]}")

print("\nCold Days:")
print("Day\tTemperature (°C)")
for day in cold_days:
    print(f"{day+1}\t{temperatures[day]}")


"""Output: Hot Days:
           Day	Temperature (°C)
            3	36.8
            6	38.7
            10	37.2

          Cold Days:
          Day	Temperature (°C)
           11	4.0
           14	-4.0
           15	-12.0
