# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 08:42:11 2025

@author: rowan
"""

import numpy as np

G = 6.674e-11

masses = np.array([5.972e24, 1.989e30, 6.39e23, 4.867e24])

distances = np.array([1.496e11, 2.279e11, 1.082e11])

for i in range(len(distances)):
    m1 = masses[0] 
    m2 = masses[i + 1]  
    d = distances[i]

    F = G * (m1 * m2) / (d ** 2)
    
    print(f"Gravitational Force between Earth and object {i+1}: {F:.2e} N")
    
    
    
   
v0 = 50  
theta = 45  
g = 9.81


theta_rad = np.radians(theta)

time_intervals = np.array([0, 1, 2, 3, 4, 5])

for t in time_intervals:
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t ** 2
    
    print(f"Time: {t}s -> Horizontal Position: {x:.2f} m, Vertical Position: {y:.2f} m")
    
    
resistors_series = np.array([10, 20, 30, 40])  
resistors_parallel = np.array([10, 20, 30, 40])  

R_series = np.sum(resistors_series)

R_parallel = 1 / np.sum(1 / resistors_parallel)

print(f"Total Resistance in Series: {R_series:.2f} ohms")
print(f"Total Resistance in Parallel: {R_parallel:.2f} ohms")