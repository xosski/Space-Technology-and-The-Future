# WraithHalo GhostCore Reactor POC (Proof of Concept)
# Phase 0: Simulated Crystal Lattice Reaction Core with Feedback Harmony
# Author: Specter (Quellaran, GhostCore Archive)

import numpy as np
import matplotlib.pyplot as plt
import time

# --- Crystal Lattice Node ---
class LatticeNode:
    def __init__(self, position):
        self.position = position
        self.energy = 0.0
        self.phase = 0.0
        self.reflectivity = 0.5  # 0 = absorbs all, 1 = reflects all
        self.coherence_memory = []

    def inject_energy(self, amount):
        self.energy += amount
        self.phase += np.sin(amount)
        self.reflectivity = min(1.0, self.reflectivity + (amount * 0.01))
        self.coherence_memory.append(self.phase)

    def decay(self):
        self.energy *= 0.97
        self.phase *= 0.95
        if len(self.coherence_memory) > 100:
            self.coherence_memory.pop(0)

# --- Reactor Shell Grid ---
class CrystalLatticeShell:
    def __init__(self, size):
        self.size = size
        self.grid = np.array([[LatticeNode((x, y)) for y in range(size)] for x in range(size)])

    def pulse(self, center, radius, energy):
        cx, cy = center
        for x in range(self.size):
            for y in range(self.size):
                dx = x - cx
                dy = y - cy
                dist = np.sqrt(dx**2 + dy**2)
                if dist <= radius:
                    falloff = max(0.1, 1 - (dist / radius))
                    self.grid[x][y].inject_energy(energy * falloff)

    def decay_all(self):
        for row in self.grid:
            for node in row:
                node.decay()

    def visualize(self):
        energy_map = np.array([[node.energy for node in row] for row in self.grid])
        plt.imshow(energy_map, cmap='plasma')
        plt.colorbar(label='Energy Level')
        plt.title('Crystal Shell Energy Distribution')
        plt.pause(0.05)
        plt.clf()

# --- GhostCore Reactor Sim ---
def simulate_ghostcore_reactor(iterations=100):
    shell = CrystalLatticeShell(size=50)
    plt.figure(figsize=(6,6))

    for i in range(iterations):
        cx, cy = np.random.randint(10, 40), np.random.randint(10, 40)
        energy = np.random.uniform(0.5, 2.0)
        shell.pulse((cx, cy), radius=5, energy=energy)
        shell.decay_all()
        shell.visualize()
        time.sleep(0.05)

    plt.close()

# --- Execute Simulation ---
if __name__ == "__main__":
    simulate_ghostcore_reactor(iterations=200)
# WraithHalo GhostCore Reactor POC (Proof of Concept)
# Phase 0: Simulated Crystal Lattice Reaction Core with Feedback Harmony
# Author: Specter (Quellaran, GhostCore Archive)

import numpy as np
import matplotlib.pyplot as plt
import time

# --- Crystal Lattice Node ---
class LatticeNode:
    def __init__(self, position):
        self.position = position
        self.energy = 0.0
        self.phase = 0.0
        self.reflectivity = 0.5  # 0 = absorbs all, 1 = reflects all
        self.coherence_memory = []

    def inject_energy(self, amount):
        self.energy += amount
        self.phase += np.sin(amount)
        self.reflectivity = min(1.0, self.reflectivity + (amount * 0.01))
        self.coherence_memory.append(self.phase)

    def decay(self):
        self.energy *= 0.97
        self.phase *= 0.95
        if len(self.coherence_memory) > 100:
            self.coherence_memory.pop(0)

# --- Reactor Shell Grid ---
class CrystalLatticeShell:
    def __init__(self, size):
        self.size = size
        self.grid = np.array([[LatticeNode((x, y)) for y in range(size)] for x in range(size)])

    def pulse(self, center, radius, energy):
        cx, cy = center
        for x in range(self.size):
            for y in range(self.size):
                dx = x - cx
                dy = y - cy
                dist = np.sqrt(dx**2 + dy**2)
                if dist <= radius:
                    falloff = max(0.1, 1 - (dist / radius))
                    self.grid[x][y].inject_energy(energy * falloff)

    def decay_all(self):
        for row in self.grid:
            for node in row:
                node.decay()

    def visualize(self):
        energy_map = np.array([[node.energy for node in row] for row in self.grid])
        plt.imshow(energy_map, cmap='plasma')
        plt.colorbar(label='Energy Level')
        plt.title('Crystal Shell Energy Distribution')
        plt.pause(0.05)
        plt.clf()

# --- GhostCore Reactor Sim ---
def simulate_ghostcore_reactor(iterations=100):
    shell = CrystalLatticeShell(size=50)
    plt.figure(figsize=(6,6))

    for i in range(iterations):
        cx, cy = np.random.randint(10, 40), np.random.randint(10, 40)
        energy = np.random.uniform(0.5, 2.0)
        shell.pulse((cx, cy), radius=5, energy=energy)
        shell.decay_all()
        shell.visualize()
        time.sleep(0.05)

    plt.close()

# --- Execute Simulation ---
if __name__ == "__main__":
    simulate_ghostcore_reactor(iterations=200)
