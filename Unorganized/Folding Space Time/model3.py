
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Tunnel curve - spiral outward pathway
t = np.linspace(0, 4 * np.pi, 1000)
x = np.sin(t) * t
y = np.cos(t) * t

# Plot the tunnel path
ax.plot(x, y, color='blue', linewidth=2, label='Temporal-Energy Outflow')

# Mark central singularity
ax.plot(0, 0, 'ro', label='Singularity Core')
ax.text(0.5, 0.5, 'Singularity\n(Decoherence Point)', color='red', fontsize=10)

# Add labels for universe domains
ax.text(-13, -1, 'Universe A\n(Forward Time - U⁺)', color='green', fontsize=12, ha='right')
ax.text(13, 1, 'Universe B\n(Inverse Time - U⁻)', color='purple', fontsize=12, ha='left')

# Decorate plot
ax.set_title('G-Field Temporal Inversion: Entropic Outflow Model', fontsize=14)
ax.set_xlabel('Dimensional Divergence')
ax.set_ylabel('Temporal Phase Drift')
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.show()