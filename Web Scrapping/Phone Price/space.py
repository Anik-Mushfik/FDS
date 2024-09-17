import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create three 3D vectors
v1 = np.array([1, 2, 1])
v2 = np.array([3, 1, 2])
v3 = np.array([0, 1, 3])

# Create a figure and 3D axis for the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the three vectors
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='v1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', label='v2')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='g', label='v3')

# Set limits for the 3D plot
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# Plot the span (combinations of v1, v2, and v3)
for a in np.linspace(-1, 1, 5):
    for b in np.linspace(-1, 1, 5):
        for c in np.linspace(-1, 1, 5):
            point = a * v1 + b * v2 + c * v3
            ax.scatter(point[0], point[1], point[2], color='k', s=5)

# Add labels and a legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.title('3D Vector Space and Span of v1, v2, and v3')
plt.show()
