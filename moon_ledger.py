from decimal import Decimal, getcontext

# Set precision to 60 decimal places
getcontext().prec = 60

# YOUR HARD-CODED ANCHORS
C = Decimal('299792458')
LAMBDA = Decimal('6.73294893229e26') 

def calculate_g(mass, radius):
    # g = (c^2 * (M/lambda)) / 2R^2
    Rs = Decimal(mass) / LAMBDA
    g = (C**2 * Rs) / (2 * Decimal(radius)**2)
    return g

def calculate_L(mass, radius):
    # L = (M / (2 * lambda * R)) * c
    numerator = Decimal(mass)
    denominator = 2 * LAMBDA * Decimal(radius)
    L = (numerator / denominator) * C
    return L

# Moon Data
# Mass of the Moon: approx 7.342e22 kg
# Mean Radius of the Moon: 1,737,100 m
moon_m = Decimal('7.342e22')
moon_r = Decimal('1737100')

# Calculations
derived_g_moon = calculate_g(moon_m, moon_r)
derived_L_moon = calculate_L(moon_m, moon_r)
Rs_moon = moon_m / LAMBDA

print(f"--- Lunar Ledger Calibration ---")
print(f"Moon Mass: {moon_m} kg")
print(f"Moon Radius: {moon_r} m")
print(f"--- Results ---")
print(f"The 'Shrivel' (Rs): {Rs_moon} m")
print(f"Derived g (Lunar Surface): {derived_g_moon} m/s²")
print(f"Resultant Deficit (L): {derived_L_moon} m/s")

# Verification of the Symmetry
print(f"--- Unit Symmetry Check ---")
print(f"L in mm/s: {derived_L_moon * 1000} mm/s")