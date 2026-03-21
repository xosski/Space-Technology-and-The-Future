import numpy as np
import matplotlib.pyplot as plt

class ReactorCorePulseGenerator:
    def __init__(self, frequency=440, amplitude=1.0):
        self.frequency = frequency
        self.amplitude = amplitude

    def emit(self, t):
        return self.amplitude * np.sin(2 * np.pi * self.frequency * t)


class NodeOscillator:
    def __init__(self, initial_freq, amplitude=0.9):
        self.frequency = initial_freq
        self.amplitude = amplitude
        self.phase_offset = 0

    def respond(self, t):
        return self.amplitude * np.sin(2 * np.pi * self.frequency * t + self.phase_offset)

    def update_frequency(self, target_freq, damping=0.01):
        self.frequency += damping * (target_freq - self.frequency)

    def calculate_efficiency(self, reactor_signal, node_signal):
        phase_diff = np.mean(np.abs(reactor_signal - node_signal))
        if phase_diff < 0.2:
            return 1.1  # in-phase
        elif phase_diff < 0.5:
            return 0.95  # slightly off
        else:
            return 0.8  # out of phase


# Simulation parameters
t_max = 0.1
sample_rate = 10000
t = np.linspace(0, t_max, int(sample_rate * t_max))

# Initialize reactor and nodes
reactor = ReactorCorePulseGenerator()
nodes = [NodeOscillator(initial_freq=400 + i * 10) for i in range(5)]

# Store energy efficiency results
efficiencies = []

for step in range(100):
    t_step = t + step * t_max
    reactor_signal = reactor.emit(t_step)
    step_efficiency = []

    for node in nodes:
        node_signal = node.respond(t_step)
        node.update_frequency(reactor.frequency)
        efficiency = node.calculate_efficiency(reactor_signal, node_signal)
        step_efficiency.append(efficiency)

    efficiencies.append(step_efficiency)

# Placeholder for visualization and report generation
print("Simulation complete. Efficiencies recorded for each node over 100 steps.")
