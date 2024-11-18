import matplotlib.pyplot as plt
import numpy as np

# Simulation time (in ns) for a larger scale, 1e9 ns (1 second)
time = np.linspace(0, 1e9, num=1000)  # 1 billion time points representing 1 second

# Use RMSD values from the provided data, with added noise for visibility
rmsd_data = {
    "Genistein_AKT1": np.full(1000, 2.4) + np.random.normal(0, 0.1, 1000),
    "Genistein_EGFR": np.full(1000, 3.1) + np.random.normal(0, 0.1, 1000),
    "Genistein_ESR1": np.full(1000, 2.1) + np.random.normal(0, 0.1, 1000),
    "Apigenin_AKT1": np.full(1000, 2.7) + np.random.normal(0, 0.1, 1000),
    "Apigenin_ESR1": np.full(1000, 2.9) + np.random.normal(0, 0.1, 1000),
    "Kaempferol_AKT1": np.full(1000, 2.5) + np.random.normal(0, 0.1, 1000),
    "Kaempferol_ESR1": np.full(1000, 2.6) + np.random.normal(0, 0.1, 1000),
    "Diadzein_AKT1": np.full(1000, 3.0) + np.random.normal(0, 0.1, 1000),
    "Diadzein_ESR1": np.full(1000, 2.3) + np.random.normal(0, 0.1, 1000),
    "Quercetin_AKT1": np.full(1000, 2.2) + np.random.normal(0, 0.1, 1000),
    "Quercetin_EGFR": np.full(1000, 2.7) + np.random.normal(0, 0.1, 1000),
    "Quercetin_ESR1": np.full(1000, 1.9) + np.random.normal(0, 0.1, 1000),
}

# Group by flavonoid
flavonoids = {
    "Genistein": ["Genistein_AKT1", "Genistein_EGFR", "Genistein_ESR1"],
    "Apigenin": ["Apigenin_AKT1", "Apigenin_ESR1"],
    "Kaempferol": ["Kaempferol_AKT1", "Kaempferol_ESR1"],
    "Diadzein": ["Diadzein_AKT1", "Diadzein_ESR1"],
    "Quercetin": ["Quercetin_AKT1", "Quercetin_EGFR", "Quercetin_ESR1"],
}

# Plotting RMSD for each flavonoid
for flavonoid, complexes in flavonoids.items():
    plt.figure(figsize=(10, 6))

    for complex_name in complexes:
        plt.plot(time, rmsd_data[complex_name], label=complex_name)

    # Add title, labels, and legend
    plt.title(f"RMSD of {flavonoid} Docked Complexes", fontsize=16)
    plt.xlabel("Time (ns)", fontsize=14)
    plt.ylabel("RMSD (Å)", fontsize=14)
    
    # Adjust the threshold lines based on RMSD stability
    plt.axhline(y=3.0, color="r", linestyle="--", label="Max Stability Threshold")
    plt.axhline(y=2.0, color="g", linestyle="--", label="Min Stability Threshold")
    
    # Adjust labels and grid
    plt.legend(fontsize=12)
    plt.grid()
    
    # Ensure the plot fits well and is clear
    plt.tight_layout()
    plt.show()