from decimal import Decimal, getcontext

# Set high precision for the Ledger Identity check
getcontext().prec = 70

# 1. OUR REFINED ANCHORS
ML = Decimal('201982073100046422270893781345058360.8258064')
C = Decimal('299792458')

# 2. DERIVING THE TRIAD COMPONENTS
# Alpha (Metric Scaling Ratio) is the inverse of the Ledger Mass
alpha_bar = Decimal(1) / ML

# Lambda (Linear Density) is the mass per unit of light-speed
ledger_lambda = ML / C

# 3. THE IDENTITY CHECK: alpha * c * lambda
# This should mathematically resolve to (1/ML) * c * (ML/c) = 1
identity_result = alpha_bar * C * ledger_lambda

print(f"--- THE LEDGER SYMMETRY AUDIT ---")
print(f"Alpha (1/ML):  {alpha_bar}")
print(f"Lambda (ML/c): {ledger_lambda}")
print(f"---------------------------------")
print(f"Alpha * C * Lambda = {identity_result}")