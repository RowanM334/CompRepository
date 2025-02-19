# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
# Get user input for vector components
x = float(input("Enter the x value of the vector: "))
y = float(input("Enter the y value of the vector: "))

#Store as tuple
vector = (x,y)

#Calculate the magnitude of the vectors
vector_mag = np.sqrt(x**2 + y**2)

# Print the components and magnitude
print(f"Vector value: {vector}")
print(f"Magnitude of the vector: {vector_mag:.2f}")



prime_numbers = [2, 3, 5, 7, 11]


prime_numbers.extend([13, 17, 19, 23])


first_prime = prime_numbers[0]
last_prime = prime_numbers[-1]
print(f"First prime number: {first_prime}")
print(f"Last prime number: {last_prime}")


first_three_primes = prime_numbers[:3]
print(f"First three prime numbers: {first_three_primes}")


more_primes = [29, 31, 37, 41]
combined_primes = prime_numbers + more_primes
print(f"Combined prime list: {combined_primes}")


reversed_primes = combined_primes[::-1]
print(f"Reversed prime list: {reversed_primes}")

    
planet_gravity = {
    "Mercury": 3.7,
    "Venus": 8.87,
    "Earth": 9.81,
    "Mars": 3.71,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uranus": 8.69,
    "Neptune": 11.15
}

# Get user input for mass and planet
mass = float(input("Enter your mass in kg: "))
planet = input("Enter the planet name: ").capitalize()

# Calculate and display weight on the chosen planet
if planet in planet_gravity:
    weight = mass * planet_gravity[planet]
    print(f"Your weight on {planet} would be {weight:.2f} N. Damn bruh lay off dem snacks.")