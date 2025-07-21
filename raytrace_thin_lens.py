from math import *
import numpy as np

# VARIABLE REVIEW:
# n = Refractive index of lens material. To calculate power, the outside material is assumed to be air, whose n is approx 1.
# R1 and R2 = Raddii of lens. To calculate a plano-convex lens, make R1 > 1e5 or R2 < -1e5.
# d = thickness of lens.

# ASSUMPTIONS:
# You are either wanting calculations for a thin bi-convex or plano-convex lens.
# The material surrounding the lens is air.
# You are looking at exactly one lens.
# Length is in meters.


def thinLensMatrix(f):
    # System matrix for thin lens
    M_lens = np.array([[1, 0], 
                    [-1/f, 1]])
    return M_lens

def homoMatrix(d):
    homoMatrix = np.array([[1, d],
                          [0, 1]])
    return homoMatrix

# Transfer matrix from source to lens
M1 = homoMatrix(0.100)

# Transfer matrix through LA1401 Thorlabs Lens
LA1401 = thinLensMatrix(0.060)

# Transfer matrix from lens to image
M3 = homoMatrix(0.110)

# System matrix
M =  M3 @ LA1401 @ M1

# Initial laser conditions
# NOTE: when r > 0, the ray is above the optical axis, so your angle should probably be negative! Vice versa, too.
r = -0.100
theta = 0.785
laserVector = np.array([[r], 
               [theta]])

# Resulting Image Location
imageVector = M @ laserVector
print("--------------------------------------\nTHIN APPROX ANSWER")
print(imageVector)
print("--------------------------------------")
