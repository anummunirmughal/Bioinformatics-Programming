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