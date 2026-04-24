CODATA_G = Decimal('6.67430e-11')
# Solve for ML: ML = c^3 / 2G
ideal_ML = (C**3) / (2 * CODATA_G)

# Now check the Earth Deficit with this "Ideal" ML
ideal_lambda = ideal_ML / C
# Deficit = c * (M_earth / (lambda * 2 * R_45))
v_deficit = C * (EARTH_M / (ideal_lambda * 2 * R_45))

print(f"Ideal ML from G: {ideal_ML}")
print(f"Predicted Deficit: {v_deficit} m/s")