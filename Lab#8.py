# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 14:30:23 2025

@author: rowan
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define parameters for HIV model
A = 1e5  # Initial viral load
B = 0
alpha = 0.5  # Infection rate
beta = 0.1   # Removal rate

time = np.linspace(0, 10, 101)  # Time from 0 to 10 seconds
viral_load = A * np.exp(alpha * time) + B * np.exp(-beta * time)

# Plot HIV model
plt.figure(figsize=(8, 5))
plt.plot(time, viral_load, label=f"HIV Model: A={A}, α={alpha}, β={beta}")
plt.xlabel("Time (days)")
plt.ylabel("Viral Load")
plt.title("HIV Viral Load Model")
plt.legend()
plt.grid()
plt.show()

# Load HIV experimental data
hiv_data = pd.read_csv("HIVSeries.csv")
time_data = hiv_data.iloc[:, 0]
viral_data = hiv_data.iloc[:, 1]

# Plot experimental data
plt.figure(figsize=(8, 5))
plt.scatter(time_data, viral_data, label="Experimental Data", color='red', marker='o')
plt.plot(time, viral_load, label="Model Prediction", linestyle='--', color='blue')
plt.xlabel("Time (days)")
plt.ylabel("Viral Load")
plt.title("HIV Viral Load vs. Model")
plt.legend()
plt.grid()
plt.show()

# Define Bacteria Growth Model
A = 1
tau = 1
t = np.linspace(0, 2, 100)
W_t = A * (np.exp(-t/tau) - 1 + t/tau)

# Plot Bacteria Growth Model
plt.figure(figsize=(8, 5))
plt.plot(t, W_t, label=f"W(t) with A={A}, τ={tau}")
plt.xlabel("Time (hours)")
plt.ylabel("W(t)")
plt.title("Bacteria Growth Model")
plt.legend()
plt.grid()
plt.show()

# Load Bacteria experimental data
data_b = pd.read_csv("g149novickB.csv")
time_b = data_b.iloc[:, 0]
growth_b = data_b.iloc[:, 1]

# Slice data for time < 10 hours
mask = time_b < 10
time_b_filtered = time_b[mask]
growth_b_filtered = growth_b[mask]

# Fit and plot bacteria growth data
plt.figure(figsize=(8, 5))
plt.scatter(time_b_filtered, growth_b_filtered, label="Experimental Data", color='red', marker='+')
plt.plot(t, W_t, label="Model Prediction", linestyle='--', color='blue')
plt.xlabel("Time (hours)")
plt.ylabel("Growth")
plt.title("Bacteria Growth vs. Model")
plt.legend()
plt.grid()
plt.show()
