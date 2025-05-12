# -*- coding: utf-8 -*-
"""

@author: rowan
"""

import numpy as np

def rotate_vector(vector, angle_deg):
    """
    Rotates a 2D vector by a given angle (in degrees).
    
    Parameters:
        vector (tuple or list or np.array): 2D vector as (x, y)
        angle_deg (float): Angle in degrees to rotate counterclockwise
    
    Returns:
        np.ndarray: Rotated vector as [x', y']
    """
    angle_rad = np.deg2rad(angle_deg)
    rotation_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad),  np.cos(angle_rad)]
    ])
    return np.dot(rotation_matrix, vector)


rng = np.random.default_rng()
samples = rng.random(100)

flips = samples < 0.5

num_heads = np.sum(flips)

print(f"Total number of heads: {num_heads}")


import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=123)

x_step = rng.random(500) < 0.5  
y_step = rng.random(500) < 0.5

x_step = np.where(x_step, 1, -1)
y_step = np.where(y_step, 1, -1)

x_pos = np.cumsum(x_step)
y_pos = np.cumsum(y_step)

plt.figure(figsize=(8, 6))
plt.plot(x_pos, y_pos, linestyle='-', marker='o', markersize=2)
plt.title('2D Random Walk: 500 Steps')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.grid(True)
plt.axis('equal')
plt.show()


rng = np.random.default_rng(seed=123)

x_step = rng.random(500) < 0.5
y_step = rng.random(500) < 0.5
z_step = rng.random(500) < 0.5

x_step = np.where(x_step, 1, -1)
y_step = np.where(y_step, 1, -1)
z_step = np.where(z_step, 1, -1)

x_pos = np.cumsum(x_step)
y_pos = np.cumsum(y_step)
z_pos = np.cumsum(z_step)

fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot(111, projection='3d')

ax1.plot(x_pos, y_pos, z_pos, marker='o', markersize=2, linewidth=1)

ax1.set_title("3D Random Walk: 500 Steps")
ax1.set_xlabel("X Position")
ax1.set_ylabel("Y Position")
ax1.set_zlabel("Z Position")

plt.tight_layout()
plt.show()