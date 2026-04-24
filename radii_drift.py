# --- THE IDENTITY OF 1: AXIAL MASS DRIFT AUDIT ---

# 1. User Inputs (Replace 0 with planetary data)
mean_mass_35 = 0          # Total Mass (at the 35.26° Isotropic Mean) in kg
mean_radius_35 = 0        # Radius at 35.26° latitude in meters
polar_radius = 0          # Radius at the Pole in meters
equatorial_radius = 0     # Radius at the Equator in meters

# 2. Scaling Logic
# The Toy Universe assumes constant linear density (lambda).
# Mass must scale proportionally with the radial extension.

def calculate_drift():
    if 0 in [mean_mass_35, mean_radius_35, polar_radius, equatorial_radius]:
        print("Audit Halted: Please provide non-zero values for all parameters.")
        return

    # Calculate Scaling Ratios
    p_ratio = polar_radius / mean_radius_35
    e_ratio = equatorial_radius / mean_radius_35

    # Determine Adapted Masses
    mass_polar = mean_mass_35 * p_ratio
    mass_equatorial = mean_mass_35 * e_ratio

    # 3. Output the Audit Results
    print(f"{'--- AXIAL MASS DRIFT REPORT ---':^40}")
    print(f"Mean Anchor: {mean_mass_35:e} kg @ {mean_radius_35:,} m")
    print("-" * 40)
    print(f"POLAR EXTREMITY:")
    print(f"  Radius Ratio: {p_ratio:.4f}")
    print(f"  Adapted Mass: {mass_polar:e} kg")
    print("-" * 40)
    print(f"EQUATORIAL EXTREMITY:")
    print(f"  Radius Ratio: {e_ratio:.4f}")
    print(f"  Adapted Mass: {mass_equatorial:e} kg")
    print("-" * 40)
    print(f"Status: Linear Density (lambda) Preserved.")

# Run Audit
calculate_drift()