""" Write a python program using Interpolation to fill in missing values in the data frame. After that store the data frame into a MATLAB file using SciPy IO.Then display the contents from the MATLAB file. 

Input: df = pd.DataFrame({"Math":[12, 4, 7, None, 2], "English":[4, 3, 57, 3, None], "Hindi":[20, 16, None, 3, 8], "Science":[14, 3, None, None, 6]})"""


import pandas as pd
from scipy.io import savemat, loadmat

# Step 1: Creating the DataFrame with missing values
df = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

# Step 2: Interpolating the missing values
df_interpolated = df.interpolate()

# Step 3: Saving the interpolated DataFrame to a MATLAB file (.mat)
# The data needs to be converted into a dictionary format compatible with MATLAB
data_dict = {col: df_interpolated[col].values for col in df_interpolated.columns}
savemat("interpolated_data.mat", data_dict)

# Step 4: Loading and displaying the contents from the MATLAB file
loaded_data = loadmat("interpolated_data.mat")

# Display the loaded data
print("Data from the MATLAB file:")
for key, value in loaded_data.items():
    # Skip metadata that starts with "__"
    if not key.startswith("__"):
        print(f"{key}: {value}")


"""Output:
Data from the MATLAB file:
Math: [[12.   4.   7.   4.5  2. ]]
English: [[ 4.  3. 57.  3.  3.]]
Hindi: [[20.  16.   9.5  3.   8. ]]
Science: [[14.  3.  4.  5.  6.]]"""
