"""
This file is the main function of this project
Name: Shangkun LI
Student ID: 20307130215
"""

import Ising_2d_wolff
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Fundamental parameetrs
size = [10, 12, 14, 16]
overall_steps = 500
interval = 10
Jfactor = 1
length = 30
a = 0.125  # scaling factors
b = 1
Tc = 2.27
T = np.linspace(1.0, 3.0, length)

# Figure of U-T Settings
fig1, ax1 = plt.subplots()

# Figure of scaling function
fig2, ax2 = plt.subplots()

# Simulation
for i in range(len(size)):
    U = []
    MLa = []
    tLb = []
    print("Simulation ", "n = ", size[i], "begins.")
    # Generate grid
    g = Ising_2d_wolff.Grid(size[i], Jfactor)
    for j in range(length):
        M_sum = 0
        M_2_sum = 0
        M_4_sum = 0
        avr_M = 0
        avr_M_2 = 0
        avr_M_4 = 0
        g.randomize()
        for step in range(overall_steps):
            ClusterSize = g.ClusterFlip(T[j])
        if T[j] < 1.7:
            steps = 20
        else:
            steps = 2000
        for step in range(steps):
            ClusterSize = g.ClusterFlip(T[j])
            M_sum += abs(sum(sum(g.canvas))) / (g.size * g.size)
            M_2_sum += (sum(sum(g.canvas))) ** 2
            M_4_sum += (sum(sum(g.canvas))) ** 4
        avr_M = M_sum / steps
        avr_M_2 = M_2_sum / steps
        avr_M_4 = M_4_sum / steps
        U.append((1 - avr_M_4 / (3 * (avr_M_2**2))) * 1.5)
        MLa.append(avr_M * (size[i] ** a))
        tLb.append((T[j] / Tc - 1) * (size[i] ** b))
    ax1.plot(T, U, label="n={}".format(size[i]))
    ax1.set_xlabel('T')
    ax1.set_ylabel('U')
    ax1.legend()
    ax2.plot(MLa,tLb,label="n={}".format(size[i]))
    ax2.set_xlabel('tL^b')
    ax2.set_ylabel('ML^a')
    ax2.legend()
    print("Simulation ", "n = ", size[i], "ends.")

plt.show()
