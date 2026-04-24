import streamlit as st
import math

# 1. The Constants
G = 6.67430e-11
C = 299792458
LAMBDA = (C**2) / (2 * G) 

# 2. The UI Header
st.title(r"Triadic Gravitational Tool")
st.write(r"This tool identifies the linear deficit from $c$ imposed by linear density ($\lambda$) based on mass and radius.")

# 3. Interactive Inputs (The Sliders!)
name = st.text_input("Body Name", "Jupiter")
mass = st.number_input("Mass (kg)", value=1.898e27, format="%.2e")
radius = st.number_input("Radius (m)", value=69911000)

# 4. The Logic
rs = mass / LAMBDA 
gravity = (G * mass) / (radius**2)
c_eff = math.sqrt(1 - (rs / radius)) * 100

# 5. The Browser Output
st.divider()
st.header(f"Results for {name}")
st.metric("Local c Efficiency", f"{c_eff:.8f} %")
col1, col2 = st.columns(2)
col1.metric("Exhaustion Coordinate ($R_s$)", f"{rs:.2f} m")
col2.metric("Surface Gravity ($g$)", f"{gravity:.4f} m/s²")

# The Realist's Reflection
st.subheader("The Linear Ledger Audit")
st.write(rf"""
At a radius of **{radius/1000:,.1f} km**, the velocity of length/time ($c$) is partially 'choked' 
by the linear density, manifesting as the gravitational potential $g$. 

However, the radius of **{rs:.2f} meters** represents the Schwarzschild radius: where the linear density $\lambda$ would be fully realised. At this linear density, 
$c$ is extinguished entirely, marking a total spatial exclusion where the 
volumetric manifold (Length/Time) can no longer be expressed.
""")