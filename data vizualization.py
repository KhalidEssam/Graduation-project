import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data from the CSV file
data = pd.read_csv('concatenated2.csv')
data1 = pd.read_csv('concatenated1.csv')

# Extract the X, Y, and Z coordinates
x = data['Accelerometer X (g)']
y = data['Accelerometer Y (g)']
z = data['Accelerometer Z (g)']


# Extract the X, Y, and Z coordinates
x1 = data1['Accelerometer X (g)']
y1 = data1['Accelerometer Y (g)']
z1 = data1['Accelerometer Z (g)']

# Create a 3D plot
plt.figure(figsize=(10, 6))

# Plot the X-axis data in yellow
plt.plot(x, color='red', label='X-axis')

# Plot the Y-axis data in blue
plt.plot(y, color='blue', label='Y-axis')

# Plot the Z-axis data in red
plt.plot(z, color='yellow', label='Z-axis')

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Gyroscope data')
plt.title('Gyroscope Signal')

# Add a legend
plt.legend()

# Show the plot
plt.show()





plt.plot(x1, color='red', label='X-axis')

# Plot the Y-axis data in blue
plt.plot(y1, color='blue', label='Y-axis')

# Plot the Z-axis data in red
plt.plot(z1, color='yellow', label='Z-axis')

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Gyroscope data')
plt.title('Gyroscope Signal')

# Add a legend
plt.legend()

# Show the plot
plt.show()