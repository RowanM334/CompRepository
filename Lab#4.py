# -*- coding: utf-8 -*-
"""

@author: rowan
"""

import math

x = float(input("Enter the x component of the vector: "))
y = float(input("Enter the y component of the vector: "))

vector = (x, y)

magnitude = math.sqrt(vector[0]**2 + vector[1]**2)

print(f"\nVector components: {vector}")
print(f"Magnitude of the vector: {magnitude:.2f}")


primes = [2, 3, 5, 7, 11]
print("Initial primes:", primes)

primes.extend([13, 17, 19])
print("After adding more primes:", primes)

first_prime = primes[0]
last_prime = primes[-1]
print("First prime:", first_prime)
print("Last prime:", last_prime)

first_three = primes[:3]
print("First three primes:", first_three)

more_primes = [23, 29, 31]
combined_primes = primes + more_primes
print("Combined prime list:", combined_primes)

reversed_primes = combined_primes[::-1]
print("Reversed prime list:", reversed_primes)

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

mass = float(input("Enter your mass in kilograms: "))
planet = input("Enter the planet you want to know your weight on (e.g., Earth, Mars, Jupiter): ").capitalize()

if planet in planet_gravity:
    g = planet_gravity[planet]
    weight = mass * g
    print(f"Your weight on {planet} is: {weight:.2f} N")
else:
    print("Invalid planet name entered. Please enter a valid planet name.")