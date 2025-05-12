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