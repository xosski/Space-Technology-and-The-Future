import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 400)
y = np.linspace(-4, 4, 400)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2)) / (np.sqrt(X**2 + Y**2) + 1e-6)

rupture_mask = np.exp(-((X)**2 + (Y)**2) * 3) * 10
Z_rupture = Z - rupture_mask

plt.figure(figsize=(10, 10))
plt.contourf(X, Y, Z_rupture, levels=100, cmap='inferno')
plt.colorbar(label='Waveform Potential')
plt.plot(0, 0, 'ro', markersize=12)
plt.text(0.2, 0.2, 'Rupture Node\n(G-Field Collapse)', color='white', fontsize=12)
plt.title("4D G-Field Lattice Projection with Rupture Node", fontsize=14)
plt.xlabel("Spatial Dimension X")
plt.ylabel("Spatial Dimension Y")
plt.axis('equal')
plt.grid(False)
plt.show()