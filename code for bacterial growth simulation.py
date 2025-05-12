import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def simulate_bacteria_dynamics(bacteria_name, pH, Temp, duration=48):
    # --- Model Parameters ---
    krs = 0.03             # Resting decay rate (1/hour)
    kdeath = 0.05          # Bacterial death rate (1/hour)
    kdeg = 0.02            # Bacteriocin degradation rate (1/hour)
    ke = 0.05              # Elimination rate between compartments (1/hour)
    kgrowth = 1.0          # Growth rate (1/hour)
    Bmax = 7e8             # Max bacteriocin production (AU/ml)
    K = 1.2e8              # Carrying capacity of bacteria

    # --- Environmental Effect Calculation ---
    pH_effect = np.exp(-((pH - 7.0) ** 2) / 2)
    temp_effect = np.exp(-((Temp - 37.0) ** 2) / 20)
    EFFECT = pH_effect * temp_effect

    # --- Initial Conditions ---
    Resting0 = 1e8          # Initial resting population
    Growing0 = 1e6          # Initial growing population
    CentralBac0 = 0.0       # Initial bacteriocin
    BiophaseBac0 = 0.0
    y0 = [Resting0, Growing0, CentralBac0, BiophaseBac0]
