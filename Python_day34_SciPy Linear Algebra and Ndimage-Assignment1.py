# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
import imageio  # Library to read and write image files

# Load an example image
image = imageio.imread('dog.jpg')  # Replace with your image file path

# Apply the Sobel filter on the image
sobel_filtered_image = ndimage.sobel(image)

# Create a figure with two subplots
plt.figure(figsize=(6, 12))  # Adjust the figure size for better visibility

# Plot the original image
plt.subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Plot the Sobel filtered image
plt.subplot(2, 1, 2)  # 2 rows, 1 column, 2nd subplot
plt.imshow(sobel_filtered_image, cmap='gray')
plt.title('Sobel Filtered Image')
plt.axis('off')

# Show the combined figure
plt.show()
