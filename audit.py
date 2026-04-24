import streamlit as st
import math

# 1. The Constants
G = 6.67430e-11
C = 299792458
LAMBDA = (C**2) / (2 * G) 

# 2. The Planetary Ledger (Presets)
bodies = {
    "Jupiter": {"mass": 1.898e27, "radius": 69911000.0},
    "Earth": {"mass": 5.972e24, "radius": 6371000.0},
    "Sun": {"mass": 1.989e30, "radius": 696340000.0},
    "Moon": {"mass": 7.347e22, "radius": 1737100.0},
    "Custom": {"mass": 1.0e24, "radius": 1.0e7}
}

# 3. UI Sidebar Configuration
st.sidebar.header("Audit Configuration")
selection = st.sidebar.selectbox("Select a Celestial Body", list(bodies.keys()))

if selection == "Custom":
    name = st.sidebar.text_input("Body Name", "My Planet")
    mass = st.sidebar.number_input("Mass (kg)", value=bodies["Custom"]["mass"], format="%.2e")
    radius = st.sidebar.number_input("Radius (m)", value=bodies["Custom"]["radius"])
else:
    name = selection
    mass = bodies[selection]["mass"]
    radius = bodies[selection]["radius"]
    st.sidebar.info(f"Using preset data for {name}")

# 4. The Logic
rs = mass / LAMBDA 
gravity = (G * mass) / (radius**2)
c_eff = math.sqrt(1 - (rs / radius)) * 100
linear_deficit = (gravity * radius) / C

# 5. Main Browser Output
st.title(r"Triadic Gravitational Tool")
st.write(r"This tool identifies the deficit from $c$ imposed by the local linear density ($\lambda$), based on a body's mass and radius.")

st.divider()
st.header(f"Results for {name}")

# Metrics Row 1
col1, col2, col3 = st.columns(3)
col1.metric("Exhaustion Coordinate ($R_s$)", f"{rs:.2f} m")
col2.metric("Surface Gravity ($g$)", f"{gravity:.4f} m/s²")
col3.metric("Linear Deficit ($L$)", f"{linear_deficit:.6f} m/s")

# Metrics Row 2
st.metric("Local c Efficiency", f"{c_eff:.8f} %")

# 6. The Realist's Reflection
st.subheader("The Linear Ledger Audit")
st.write(rf"""
At a radius of **{radius/1000:,.1f} km**, the velocity of length/time ($c$) is partially 'choked' 
by the linear density, manifesting as the gravitational potential $g$. 

The radius of **{rs:.2f} meters** represents the Schwarzschild radius: where the linear density $\lambda$ would become fully realised if the body's radius was reduced to this compression. At that linear density, 
$c$ would be extinguished entirely, marking a total spatial exclusion where the 
volumetric manifold (Length/Time) can no longer be fulfilled.
""")

# Safety Warning for the "Custom" explorers
if radius <= rs:
    st.error("CRITICAL: The current radius is within the coordinate of exhaustion. Spatial context is mathematically excluded.")