import matplotlib.pyplot as plt
import numpy as np

# Distance range in light-years
distances = np.linspace(1, 100, 200)

# Speed profiles
speed_conventional_2 = 0.2  # Conventional slow (0.2c)
speed_conventional_1 = 0.5  # Conventional fast (0.5c)
speed_spectral_drift = 0.85  # Spectral Drift (0.85c)
speed_revenant_ftg = 5.0     # Revenant-class (appears as 5.0c equivalent)

# Calculate travel times
time_conventional_2 = distances / speed_conventional_2
time_conventional_1 = distances / speed_conventional_1
time_spectral_drift = distances / speed_spectral_drift
time_revenant_ftg = distances / speed_revenant_ftg

# Plot
plt.figure(figsize=(12, 7))
plt.plot(distances, time_conventional_2, '--', label='Conventional (0.2c)', alpha=0.6)
plt.plot(distances, time_conventional_1, '--', label='Conventional (0.5c)', alpha=0.7)
plt.plot(distances, time_spectral_drift, label='Spectral Drift (0.85c)', linewidth=2)
plt.plot(distances, time_revenant_ftg, label='Revenant-Class (5.0c equivalent)', linewidth=2.5)

plt.title('Projected Interstellar Travel Times by Propulsion Method')
plt.xlabel('Distance (light-years)')
plt.ylabel('Travel Time (years)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()