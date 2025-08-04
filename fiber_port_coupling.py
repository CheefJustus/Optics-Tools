from math import *
import numpy as np
import matplotlib.pyplot as plt

# Diameter of collimated laser beam. (mm)
D = 0.68e-3

# Mode field diameter. This is how big the core of the single mode patch cable is. (µm)
MFD = 4.1e-6

# Wavelength of incident laser beam source. (nm)
λ = 632.8e-9

# Effective focal length (EFL) of a given fiber coupler (mm)
EFL = 4.6e-3

# Mode radius of coupled laser beam with given fiber coupler. (µm)
# ω = ((4 * λ * EFL) / (pi * D))
ω = 10.4e-6
# Focal length needed for perfect fiber coupling. (mm)
f = ((pi * D * MFD) / (4 * λ)) * 1e3

# Coupling efficiency of laser beam and fiber port with given specifications. (%)
η = (4 * ω**2 * (MFD / 2)**2) / (ω**2 + (MFD / 2)**2)**2

print('---------------------------------------------------------------------')
print(f'FOCAL LENGTH NEEDED FOR PERFECT SINGLE MODE FIBER COUPLING:')
print(f'INPUTS: D = {D * 1e3} mm\n\tMFD = {MFD * 1e6} µm\n\tλ = {λ * 1e9} nm')
print(f'OUTPUT: f = {f} mm')
print('---------------------------------------------------------------------')

'''''
Equation is broken. I do not think Thorlabs put the right equation on their webinar!
print(f'COUPLING EFFICIENCY OF CURRENT FIBER PORT ARRANGEMENT:')
print(f'INPUTS: D = {D * 1e3} mm\n\tEFL = {EFL * 1e3} mm\n\tMFD = {MFD * 1e6} µm\n\tλ = {λ * 1e9} nm')
print(f'OUTPUTS: ω = {ω * 1e6:.3} µm\n\t η = {η*100:.3} %')
print(f'In other words, with the given laser and fiber port arrangement, the laser beam spot would be reduced to {ω * 1e6:.3} µm.\nThis would result in a coupling efficiency of {η*100:.3} %, using the given single mode patch cable specs.')
print(f'Note that this ignores any lateral or angular offset losses, which can be significant even with minor misalignment.')
print('---------------------------------------------------------------------')
'''''