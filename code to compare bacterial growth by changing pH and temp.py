import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def simulate_bacteria_dynamics(bacteria_name, pH, Temp, duration=48):
    # --- Model Parameters ---
    krs_base = 0.03             # Resting decay rate
    kdeath_base = 0.05          # Death rate
    kdeg_base = 0.02            # Bacteriocin degradation
    ke = 0.05                   # Elimination rate
    kgrowth_base = 1.0          # Base growth rate
    Bmax = 7e8                  # Max bacteriocin production
    K = 1.2e8                   # Carrying capacity

    # --- Environmental Sensitivity Scaling ---
    pH_effect = np.exp(-((pH - 7.0) ** 2) / 1.5)
    temp_effect = np.exp(-((Temp - 37.0) ** 2) / 15)
    EFFECT = pH_effect * temp_effect

    # Scale parameters based on EFFECT
    kgrowth = kgrowth_base * EFFECT
    krs = krs_base / EFFECT if EFFECT > 0 else 0.1
    kdeath = kdeath_base / EFFECT if EFFECT > 0 else 0.1
    kdeg = kdeg_base * (2 - EFFECT)  # more degradation under stress

    # --- Initial Conditions ---
    Resting0 = 1e8
    Growing0 = 1e6
    CentralBac0 = 0.0
    BiophaseBac0 = 0.0
    y0 = [Resting0, Growing0, CentralBac0, BiophaseBac0]

 # --- Time Vector ---
    t = np.linspace(0, duration, 500)

     # --- ODE System ---
    def model(y, t):
        Resting, Growing, CentralBac, BiophaseBac = y
        total_bacteria = Resting + Growing

        if t <= 8:
            growth_effect = kgrowth * (1 - total_bacteria / K)
        else:
            growth_effect = kgrowth * max(1 - (t - 8) / 16, 0.05)

        if t >= 4:
            if CentralBac < Bmax:
                bac_production = EFFECT * Growing * (1 - CentralBac / Bmax)
            else:
                bac_production = 0
        else:
            bac_production = 0

        dResting_dt = -krs * Resting
        dGrowing_dt = growth_effect * Resting - kdeath * Growing
        dCentralBac_dt = bac_production - kdeg * CentralBac
        dBiophaseBac_dt = ke * CentralBac - ke * BiophaseBac

        return [dResting_dt, dGrowing_dt, dCentralBac_dt, dBiophaseBac_dt]
    
    # --- Solve ODEs ---
    result = odeint(model, y0, t)
    Resting, Growing, CentralBac, _ = result.T
# --- Plotting ---
    plt.figure(figsize=(10, 5))
    plt.plot(t, Growing, color='dodgerblue', label="Growing", linewidth=2)
    plt.plot(t, Resting, color='orangered', label="Resting", linewidth=2)
    plt.plot(t, CentralBac, color='gold', label="B", linewidth=2)

    plt.title(f"{bacteria_name} at pH={pH}, Temp={Temp}°C", fontsize=14)
    plt.xlabel("Time (Hours)")
    plt.ylabel("Population / Bacteriocin (AU/ml)")
    plt.ylim(0, Bmax * 1.1)
    plt.xlim(0, duration)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# ✅ Example comparisons — try changing values:
simulate_bacteria_dynamics("Propionibacterium acnes", pH=7.0, Temp=37.0)
simulate_bacteria_dynamics("Streptococcus mitis", pH=6.0, Temp=35.0)