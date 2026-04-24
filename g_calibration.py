from decimal import Decimal, getcontext
getcontext().prec = 60

# Inputs
C = Decimal('299792458')
EARTH_M = Decimal('5.9722e24') # Using a slightly more precise Earth mass
R_45 = Decimal('6367490')      # WGS84 Radius at 45 degrees

# The "Tightened" Pure g (Observed + Corrections)
G_PURE = Decimal('9.82465') 

# Solve for Lambda: (c^2 * M) / (2 * g * R^2)
tightened_lambda = (C**2 * EARTH_M) / (2 * G_PURE * R_45**2)

# Derive the new ML: ML = lambda * c
tightened_ML = tightened_lambda * C

print(f"--- REFINED LEDGER ANCHORS ---")
print(f"Refined Lambda: {tightened_lambda}")
print(f"Refined ML:     {tightened_ML}")
print(f"------------------------------")