from math import *
import numpy as np
import matplotlib.pyplot as plt

# Magnification Power of Beam Expander
mp = 2

# Input Beam Diameter (m)
d_0 = 0.68 / 1000

# Input Beam Divergence (radians) (half-angle)
theta_0 = (1.2 / 2) / 1000

# Laser path distance
L = np.linspace(0, 10, 1000)

# Output Beam Diameter with Beam Expander
d_1_expander = (mp * d_0) + L * tan((2 * theta_0) / mp)

# Output Beam Divergence with Beam Expander
theta_1 = theta_0 / mp

#Output Beam Diameter without Expander
d_1_raw = d_0 + L * tan(2*theta_0)

plt.plot(L, d_1_expander * 1000, label = 'Expander Beam Diameter')
plt.plot(L, d_1_raw * 1000, label = 'Raw Beam Diameter')
plt.xlabel('Beam Path Length (m)')
plt.ylabel('Beam Diameter (mm)')
plt.title('Laser Beam Diameter Over Path Length')
plt.legend()
plt.show()