import numpy as np
import matplotlib.pyplot as plt
# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))

# Define the tunnel curve - entry, singularity, exit
t = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
x = np.sin(t) * np.exp(-0.1 * t**2)
y = t

# Plot the wormhole pathway
ax.plot(x, y, color='blue', linewidth=2, label='Wormhole Pathway')

# Add entry and exit universes
ax.text(-0.8, -7, 'Universe A (Entry)', fontsize=10, ha='right', color='green')
ax.text(0.8, 7, 'Universe B (Exit)', fontsize=10, ha='left', color='purple')

# Add singularity point
ax.plot(0, 0, 'ro', label='Singularity Core')
ax.text(0.1, 0.5, 'Singularity\n(Reformatting Node)', color='red')

# Add decorations
ax.set_title('Dimensional Tunnel Model: G-Field Reformatting Pathway', fontsize=14)
ax.set_xlabel('Spatial Warp')
ax.set_ylabel('Temporal Displacement')
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.show()