
# TPV_simulator.py
# Simulates thermophotovoltaic cell efficiency for Ghost Core radiation harvesting

class TPVSimulator:
    def __init__(self, core_temp_K, bandgap_eV):
        self.core_temp = core_temp_K
        self.bandgap = bandgap_eV
        self.stefan_boltzmann = 5.67e-8

    def spectral_efficiency(self):
        if self.bandgap < 0.4 or self.bandgap > 1.0:
            return 0.15
        return 0.35

    def power_output_per_area(self):
        emitted_power = self.stefan_boltzmann * self.core_temp**4
        return emitted_power * self.spectral_efficiency()
