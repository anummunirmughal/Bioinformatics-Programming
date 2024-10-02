import matplotlib.pyplot as plt
import numpy as np

# Simulated RMSD data for wild-type and mutant MYO7A proteins (arbitrary units for illustration)
time = np.linspace(0, 200, 201)  # Time from 0 to 200 ns
rmsd_wildtype = np.sin(time / 50) * 0.05 + 0.2  # Minor deviations in wild-type
rmsd_mutant = np.sin(time / 50) * 0.1 + 0.4  # Larger deviations in the mutant after 100 ns
rmsd_mutant[100:] += np.linspace(0, 0.2, 101)  # Mutation leads to destabilization after 100 ns

# Simulated RMSF data for residue flexibility analysis
residues = np.arange(1, 1660)  # Residue positions from 1 to 1657 (for mutant, wild-type extends further)
rmsf_wildtype = np.exp(-(residues - 1100) ** 2 / (2 * 200 ** 2)) * 0.2  # Lower flexibility in key domains
rmsf_mutant = rmsf_wildtype.copy()

# Corrected line: Adjusting the length of the np.linspace array to match the truncation site
rmsf_mutant[1585:] += np.linspace(0.2, 0.5, len(rmsf_mutant[1585:]))  # Increased flexibility near truncation site

# Create the figure for RMSD plot
plt.figure(figsize=(10, 5))

# RMSD plot
plt.subplot(1, 2, 1)
plt.plot(time, rmsd_wildtype, label="Wild-type", color="blue")
plt.plot(time, rmsd_mutant, label="Mutant", color="red")
plt.title("RMSD Over Time")
plt.xlabel("Time (ns)")
plt.ylabel("RMSD (nm)")
plt.legend()
plt.grid(True)

# RMSF plot
plt.subplot(1, 2, 2)
plt.plot(residues, rmsf_wildtype, label="Wild-type", color="blue")
plt.plot(residues, rmsf_mutant, label="Mutant", color="red")
plt.title("RMSF by Residue")
plt.xlabel("Residue Number")
plt.ylabel("RMSF (nm)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
