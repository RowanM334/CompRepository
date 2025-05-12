# -*- coding: utf-8 -*-
"""

@author: rowan
"""
#1
import numpy as np

def rotate_vector(vector, theta_deg):
    """
    Rotate a 2D vector by theta degrees counterclockwise.
    
    Parameters:
        vector (array-like): A 2D vector [x, y].
        theta_deg (float): Angle in degrees.
    
    Returns:
        np.ndarray: Rotated vector [x', y'] as a NumPy array.
    """
    theta_rad = np.deg2rad(theta_deg) 
    rotation_matrix = np.array([
        [np.cos(theta_rad), -np.sin(theta_rad)],
        [np.sin(theta_rad),  np.cos(theta_rad)]
    ])
    return np.dot(rotation_matrix, vector)

#2


rng = np.random.default_rng()
samples = rng.random(100)

flips = samples < 0.5

num_heads = np.sum(flips)

print(f"Total number of heads in 100 flips: {num_heads}")

#3


import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=42)         

x_step = rng.random(500) < 0.5
y_step = rng.random(500) < 0.5

x_step = np.where(x_step, 1, -1)
y_step = np.where(y_step, 1, -1)

x_pos = np.cumsum(x_step)
y_pos = np.cumsum(y_step)

plt.figure(figsize=(8, 6))
plt.plot(x_pos, y_pos, marker='o', markersize=2, linewidth=1)
plt.title('2D Random Walk (500 Steps)')
plt.xlabel('x position')
plt.ylabel('y position')
plt.axis('equal')
plt.grid(True)
plt.show()
