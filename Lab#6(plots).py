# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:29:08 2025

@author: rowan
"""

import numpy as np
import matplotlib.pyplot as plt

# Define variables
v0 = 20  # Initial velocity in m/s
theta = 45  # Launch angle in degrees
g = 9.81  # Acceleration due to gravity in m/s²

# Convert angle to radians
theta_rad = np.radians(theta)

# Calculate total flight time
time_total = (2 * v0 * np.sin(theta_rad)) / g

# Create time intervals
time_intervals = np.linspace(0, time_total, num=100)

# Calculate horizontal and vertical positions
x_t = v0 * np.cos(theta_rad) * time_intervals
y_t = v0 * np.sin(theta_rad) * time_intervals - 0.5 * g * time_intervals**2

# Create subplots
plt.figure(figsize=(12, 6))

# Plot x vs t
plt.subplot(1, 3, 1)
plt.plot(time_intervals, x_t, 'b-', label='x vs t')
plt.xlabel('Time (s)')
plt.ylabel('Horizontal Position (m)')
plt.title('Horizontal Position vs Time')
plt.grid(True)
plt.legend()

# Plot y vs t
plt.subplot(1, 3, 2)
plt.plot(time_intervals, y_t, 'r--', label='y vs t')
plt.xlabel('Time (s)')
plt.ylabel('Vertical Position (m)')
plt.title('Vertical Position vs Time')
plt.grid(True)
plt.legend()

# Plot x vs y
plt.subplot(1, 3, 3)
plt.plot(x_t, y_t, 'g-.', label='x vs y')
plt.xlabel('Horizontal Position (m)')
plt.ylabel('Vertical Position (m)')
plt.title('Projectile Motion')
plt.grid(True)
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
