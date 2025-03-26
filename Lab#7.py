# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 19:36:22 2025

@author: rowan
"""
#example 1
import numpy as np
import matplotlib.pyplot as plt

masses = np.array([2, 5, 10, 15, 20])

velocity = 3  # Example constant velocity

kinetic_energy = 0.5 * masses * velocity**2

plt.bar(masses, kinetic_energy, color='skyblue', edgecolor='black')

plt.xlabel('Mass (kg)')
plt.ylabel('Kinetic Energy (Joules)')
plt.title('Kinetic Energy of Objects with different masses')

plt.show()




#example 2
temperatures = np.linspace(100, 500, 100)
thermal_energy = 1.5 * temperatures 

plt.hist(thermal_energy, bins=20, color='orange', edgecolor='black')

plt.xlabel('Energy (J)')
plt.ylabel('Frequency')
plt.title('Thermal Energy in a something')


plt.show()

#example 3
elements = ['Hydrogen', 'Helium', 'Oxygen', 'Carbon', 'Neon', 'Iron']
abundances = [74, 24, 1, 0.5, 0.3, 0.2] 

plt.figure(figsize=(8, 8))
plt.pie(abundances, labels=elements, autopct='%1.1f%%', colors=['blue', 'orange', 'green', 'red', 'purple', 'brown'])

plt.title('Relative abundances of elements')

plt.legend(elements, loc='upper right')

plt.show()