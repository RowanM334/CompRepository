# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 08:49:40 2025

@author: rowan
"""

import numpy as np

a = float(input("Enter acceleration (m/s²): "))
t = float(input("Enter time (s): "))

u = 0

s = (0.5) * a * (t ** 2)

print(f"Final position of the object: {s:.2f} meters")


v = float(input("Enter initial velocity (m/s): "))

g = 9.8 

h = (v ** 2) / (2 * g)

print(f"Maximum height reached: {h:.2f} meters")


m = float(input("Enter mass of the box (kg): "))
uk = float(input("Enter coefficient of kinetic friction: "))

g = 9.81 

F_friction = uk * m * g

print(f"Force of friction acting on the box: {F_friction:.2f} N")