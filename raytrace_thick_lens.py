from math import *
import numpy as np

# VARIABLE REVIEW:
# n = Refractive index of lens material. To calculate power, the outside material is assumed to be air, whose n is approx 1.
# R1 and R2 = Raddii of lens. To calculate a plano-convex lens, make R1 > 1e5 or R2 < -1e5.
# d = thickness of lens.

# ASSUMPTIONS:
# You are either wanting calculations for a bi-convex or plano-convex lens.
# The material surrounding the lens is air.
# You are looking at exactly one lens.
# Length is in meters.


def thickLensMatrix(n, R1, R2, t):
    if R1 > 1e5:
        P1 = 0
    else:
        P1 = (n - 1) / R1

    if R2 < -1e5:
        P2 = 0
    else:
        P2 = (n - 1) / R2

    # Setting up the system matrix for a thick lens
    a = 1 + ((t * (1 - n)) / (R1 * n))
    b = t * (1 / n)
    c = (1 / R1) * (1 - n) + (1 / R2) * ((1 - n)) + t * (1 / R1) * (1 / R2) * ((1 - n)**2 / n)
    d = 1 + (t * (1 / R2) * ((1 - n) / n))

    # System matrix for thick lens
    M_lens = np.array([[a, b], 
                    [c, d]])
    return M_lens

def homoMatrix(d):
    homoMatrix = np.array([[1, d],
                          [0, 1]])
    return homoMatrix

# Transfer matrix from source to lens
M1 = homoMatrix(10)

# Transfer matrix through LA1401 Thorlabs Lens
LA1401 = thickLensMatrix(1.5153, 0.0309, -1e10, 0.0163)

# Transfer matrix from lens to image
M3 = homoMatrix(0.060)

# System matrix
M =  M3 @ LA1401 @ M1

# Initial laser conditions
# NOTE: when r > 0, the ray is above the optical axis, so your angle should probably be negative! Vice versa, too.
r = 0.0254
theta = -5.08e-3
laserVector = np.array([[r], 
               [theta]])

# Resulting Image Location
imageVector = M @ laserVector
print(f"--------------------------------------\nTHICK APPROX ANSWER FOR LA1401 LENS WITH RAY {r} m OFFEST AND {theta} rad ANGLE.")
print(f"LASER IS POINTING {M1[0][1]} m AWAY.\nIMAGE PLANE IS {M3[0][1]} m AWAY FROM LENS.")
print(imageVector)
print("--------------------------------------")
