import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_facecolor("#0b0c1d")  # Blueprint dark blue

# Core
core = Circle((0, 0), 1, edgecolor='cyan', fill=False, linewidth=2)
ax.add_patch(core)
ax.text(0, 0, "FUSION CORE", color='cyan', ha='center', va='center', fontsize=8, weight='bold')

# Morphing Crystal Lattice
lattice_ring = Circle((0, 0), 2, edgecolor='lightblue', fill=False, linewidth=1.5, linestyle='--')
ax.add_patch(lattice_ring)
ax.text(0, 2.3, "Crystal Lattice Zone", color='lightblue', ha='center', fontsize=7)

# Superconductive Web
superconductive_layer = Circle((0, 0), 3, edgecolor='cyan', fill=False, linewidth=1.2, linestyle='dotted')
ax.add_patch(superconductive_layer)
ax.text(0, 3.3, "Superconductive Matrix", color='cyan', ha='center', fontsize=7)

# Harmonic Pulse Shell
harmonic_shell = Circle((0, 0), 4, edgecolor='white', fill=False, linewidth=1.2)
ax.add_patch(harmonic_shell)
ax.text(0, 4.4, "Harmonic Pulse Ring", color='white', ha='center', fontsize=7)

# Supercooled Gas Jacket
gas_shell = Circle((0, 0), 5, edgecolor='skyblue', fill=False, linewidth=1.5)
ax.add_patch(gas_shell)
ax.text(0, 5.4, "Supercooled Gas Jacket", color='skyblue', ha='center', fontsize=7)

# Outer Containment Wall
containment = Circle((0, 0), 5.7, edgecolor='deepskyblue', fill=False, linewidth=2.0)
ax.add_patch(containment)
ax.text(0, 6.0, "Outer Containment Wall", color='deepskyblue', ha='center', fontsize=7)

# Final blueprint layout
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.axis('off')
ax.set_title("Blueprint Export: GhostCore Reactor (Lattice Cooling Architecture)", color='white', fontsize=11)

plt.show()
