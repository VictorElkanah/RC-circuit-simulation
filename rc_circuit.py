
import numpy as np
import matplotlib.pyplot as plt

# Given parameters
R = 1000        # Resistance in ohms
C = 1e-6        # Capacitance in farads
V = 5           # Supply voltage in volts
#   Time Constant
tau = R * C     # Time constant τ = RC
#  Step 2: Time Array 
# Time chosen to cover charging and discharging fully
t = np.linspace(0, 5 * tau, 1000)

#  Charging Equation 
# Vc(t) = V(1 - e^(-t/RC))
Vc_charge = V * (1 - np.exp(-t / tau))

#  Discharging Equation
# Vc(t) = V e^(-t/RC)
Vc_discharge = V * np.exp(-t / tau)

#  Plot Charging & Discharging 
plt.figure(figsize=(8, 5))
plt.plot(t, Vc_charge, label="Charging")
plt.plot(t, Vc_discharge, label="Discharging")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (volts)")
plt.title("RC Circuit: Charging and Discharging of a Capacitor")
plt.legend()
plt.grid(True)
plt.show()

#  Effect of Changing R and C
R_new = 2000        # New resistance
C_new = 2e-6        # New capacitance
tau_new = R_new * C_new

Vc_charge_new = V * (1 - np.exp(-t / tau_new))

#  Comparison Plot 
plt.figure(figsize=(8, 5))
plt.plot(t, Vc_charge, label="Original (R=1000Ω, C=1µF)")
plt.plot(t, Vc_charge_new, label="Modified (R=2000Ω, C=2µF)")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (volts)")
plt.title("Effect of Resistance and Capacitance on RC Circuit")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(t, Vc_charge, label="Charging")
plt.plot(t, Vc_discharge, label="Discharging")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (volts)")
plt.title("RC Circuit Response")
plt.legend()
plt.grid(True)
plt.savefig("rc_circuit_response.png")
plt.close()

print("Simulation completed successfully.")
