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