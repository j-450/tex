import streamlit as st
import math

# 1. The Constants
G = 6.67430e-11
C = 299792458
LAMBDA = (C**2) / (2 * G) 

# 2. The UI Header
st.title(r"Triadic Gravitational Tool")
st.write(r"This tool identifies the linear deficit from $c$ imposed by the local linear density ($\lambda$), based on a body's mass and radius.")

# 3. Interactive Inputs (The Sliders!)
name = st.text_input("Body Name", "Jupiter")
mass = st.number_input("Mass (kg)", value=1.898e27, format="%.2e")
radius = st.number_input("Radius (m)", value=69911000)

# 4. The Logic
rs = mass / LAMBDA 
gravity = (G * mass) / (radius**2)
c_eff = math.sqrt(1 - (rs / radius)) * 100


# The Linear Deficit (L)
# This represents the 'velocity cost' at the given radius
linear_deficit = (gravity * radius) / C

# 5. The Browser Output
st.divider()
st.header(f"Results for {name}")

col1, col2, col3 = st.columns(3) # Expanded to 3 columns
col1.metric("Exhaustion Coordinate ($R_s$)", f"{rs:.2f} m")
col2.metric("Surface Gravity ($g$)", f"{gravity:.4f} m/s²")
col3.metric("Linear Deficit ($L$)", f"{linear_deficit:.6f} m/s")

st.metric("Local c Efficiency", f"{c_eff:.8f} %")


# The Realist's Reflection
st.subheader("The Linear Ledger Audit")
st.write(rf"""
At a radius of **{radius/1000:,.1f} km**, the velocity of length/time ($c$) is partially 'choked' 
by the linear density, manifesting as the gravitational potential $g$. 

However, the radius of **{rs:.2f} meters** represents the Schwarzschild radius: where the linear density $\lambda$ would be fully realised. At this linear density, 
$c$ is extinguished entirely, marking a total spatial exclusion where the 
volumetric manifold (Length/Time) can no longer be expressed.
""")