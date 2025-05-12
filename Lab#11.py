# -*- coding: utf-8 -*-
"""
Created on Sun May 11 23:24:40 2025

@author: rowan
"""

import numpy as np
import matplotlib.pyplot as plt

num_steps = 1000
num_walks = 1000

def generate_random_walk(num_steps):
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)
    steps = np.random.choice([-1, 1], size=(num_steps, 2))  # diagonal steps
    x[1:] = np.cumsum(steps[:, 0])
    y[1:] = np.cumsum(steps[:, 1])
    return x, y

x, y = generate_random_walk(num_steps)
plt.figure()
plt.plot(x, y)
plt.axis('equal')
plt.title('Single Random Walk')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

plt.figure(figsize=(10, 10))
for i in range(1, 5):
    x, y = generate_random_walk(num_steps)
    plt.subplot(2, 2, i)
    plt.plot(x, y)
    plt.title(f'Walk {i}')
    plt.axis('equal')
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
plt.tight_layout()
plt.show()

x_final = np.zeros(num_walks)
y_final = np.zeros(num_walks)
displacement = np.zeros(num_walks)

for i in range(num_walks):
    x, y = generate_random_walk(num_steps)
    x_final[i] = x[-1]
    y_final[i] = y[-1]
    displacement[i] = np.sqrt(x[-1]**2 + y[-1]**2)

plt.figure()
plt.scatter(x_final, y_final, alpha=0.5)
plt.title('Final Positions of 1000 Random Walks')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid()
plt.show()

plt.figure()
plt.hist(displacement, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Displacements')
plt.xlabel('Displacement')
plt.ylabel('Frequency')
plt.grid()
plt.show()

disp_squared = displacement ** 2
plt.figure()
plt.hist(disp_squared, bins=30, color='lightcoral', edgecolor='black')
plt.title('Histogram of Displacement Squared')
plt.xlabel('Displacement²')
plt.ylabel('Frequency')
plt.grid()
plt.show()

plt.figure()
plt.semilogy(sorted(disp_squared), label='semilog')
plt.title('Semilog Plot of Displacement Squared')
plt.grid()
plt.show()

plt.figure()
plt.loglog(sorted(disp_squared), label='log-log')
plt.title('Log-Log Plot of Displacement Squared')
plt.grid()
plt.show()

msd_1000 = np.mean(disp_squared)
print(f"Mean-square displacement (1000 steps): {msd_1000:.2f}")

num_steps_4000 = 4000
displacement_4000 = np.zeros(num_walks)
for i in range(num_walks):
    x, y = generate_random_walk(num_steps_4000)
    displacement_4000[i] = x[-1]**2 + y[-1]**2
msd_4000 = np.mean(displacement_4000)
print(f"Mean-square displacement (4000 steps): {msd_4000:.2f}")


# Part 2

from scipy.special import factorial

lambda_ = 8
k = np.arange(0, 30, dtype=float)
P_k = (lambda_**k * np.exp(-lambda_)) / factorial(k)

plt.figure()
plt.stem(k, P_k, use_line_collection=True)
plt.title('Poisson Distribution: λ = 8')
plt.xlabel('k (Number of Heads)')
plt.ylabel('Probability')
plt.grid()
plt.show()

N = 1000
p_heads = 0.08
num_flips = 100
trials = np.random.binomial(n=num_flips, p=p_heads, size=N)

plt.figure()
plt.hist(trials, bins=np.arange(0, max(trials)+2)-0.5, edgecolor='black', color='orchid')
plt.title('Histogram of Heads in 1000 Coin Flip Trials (8% chance)')
plt.xlabel('Number of Heads in 100 Flips')
plt.ylabel('Frequency')
plt.grid()
plt.show()