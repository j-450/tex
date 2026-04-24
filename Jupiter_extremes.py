from decimal import Decimal, getcontext

getcontext().prec = 60

C = Decimal('299792458')
LAMBDA = Decimal('6.73294893229e26') 

def calculate_g(mass, radius):
    Rs = mass / LAMBDA
    return (C**2 * Rs) / (2 * radius**2)

def calculate_L(mass, radius):
    return (mass / (2 * LAMBDA * radius)) * C

# Base Stats
m_mean = Decimal('1.89813e27')
r_mean = Decimal('69911000')

r_eq = Decimal('71492000')
r_pol = Decimal('66854000')

# AXIAL MASS SCALING
# We adjust the mass by the ratio of the radius to the mean
m_eq = m_mean * (r_eq / r_mean)
m_pol = m_mean * (r_pol / r_mean)

# CALCULATIONS
g_eq_adjusted = calculate_g(m_eq, r_eq)
L_eq_adjusted = calculate_L(m_eq, r_eq)

g_pol_adjusted = calculate_g(m_pol, r_pol)
L_pol_adjusted = calculate_L(m_pol, r_pol)

print(f"--- Jupiter Non-Spherical Ledger ---")
print(f"Mean Mass Ref: {m_mean} kg")
print(f"\n--- EQUATORIAL (Radial Expansion) ---")
print(f"Adjusted Mass: {m_eq} kg")
print(f"Derived g: {g_eq_adjusted} m/s²")
print(f"Deficit (L): {L_eq_adjusted} m/s")

print(f"\n--- POLAR (Radial Contraction) ---")
print(f"Adjusted Mass: {m_pol} kg")
print(f"Derived g: {g_pol_adjusted} m/s²")
print(f"Deficit (L): {L_pol_adjusted} m/s")