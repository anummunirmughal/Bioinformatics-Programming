import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Simulation time (in ns)
time = np.linspace(0, 100, num=100)

# RMSD data (example values)
rmsd_esr1 = {
    'Ellagic Acid': np.random.uniform(1.5, 2.3, size=100),
    'Gallic Acid': np.random.uniform(1.5, 2.3, size=100),
    'Punicalagin': np.random.uniform(1.5, 2.3, size=100)
}

rmsd_lyst = {
    'Punicalagin': np.random.uniform(1.0, 2.0, size=100),
}

# Create RMSD plot for p.Q19T-ESR1 complex
plt.figure(figsize=(14, 6))

# Plot RMSD for ESR1 complex
plt.subplot(1, 2, 1)
for compound, rmsd_values in rmsd_esr1.items():
    plt.plot(time, rmsd_values, label=compound)
plt.title('RMSD of Compounds in p.Q19T-ESR1 Complex')
plt.xlabel('Time (ns)')
plt.ylabel('RMSD (Å)')
plt.axhline(y=2.3, color='r', linestyle='--', label='Max RMSD')
plt.axhline(y=1.5, color='g', linestyle='--', label='Min RMSD')
plt.legend()
plt.grid()

# Plot RMSD for LYST complex
plt.subplot(1, 2, 2)
for compound, rmsd_values in rmsd_lyst.items():
    plt.plot(time, rmsd_values, label=compound, color='orange')
plt.title('RMSD of Compounds in p.L2438Q-LYST Complex')
plt.xlabel('Time (ns)')
plt.ylabel('RMSD (Å)')
plt.axhline(y=2.0, color='r', linestyle='--', label='Max RMSD')
plt.axhline(y=1.0, color='g', linestyle='--', label='Min RMSD')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
