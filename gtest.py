from decimal import Decimal, getcontext
getcontext().prec = 70

C = Decimal('299792458')
LAMBDA = Decimal('6.73295e26') # Your anchor lambda
M_EARTH = Decimal('5.9722e24')
R_EQUATOR = Decimal('6378137')

# Velocity Deficit L = M / (2 * lambda * R/c)
# Simplified: L = (M * c) / (2 * lambda * R)
L_equator = (M_EARTH * C) / (2 * LAMBDA * R_EQUATOR)

print(f"Equatorial Velocity Deficit (L_eq): {L_equator} m/s")