import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df.to_csv('/usr/src/app/output/my_data.csv')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Generate data for the spiral
theta = np.linspace(0, 12 * np.pi, 1000)
z = np.linspace(-2, 2, 1000)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

# Create a 3D figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the spiral
ax.plot(x, y, z, color='purple', linewidth=2)

# Customize the plot
ax.set_title('3D Parametric Spiral', fontsize=16)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.grid(True)

# Define the output directory and ensure it exists
output_dir = '/usr/src/app/output'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '3d_spiral_plot.png')

# Save the plot to the specified directory
plt.savefig(output_path)

# Optional: If you also want to display the plot in addition to saving it
# plt.show()

print(f"Plot saved at: {output_path}")

