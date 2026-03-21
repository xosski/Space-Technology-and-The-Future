
# molten_lead_loop_model.py
# Simulates molten lead loop for cooling, EMP pulse generation, and MHD microthrust

class MoltenLeadLoop:
    def __init__(self, flow_rate_kg_s, loop_temp_K):
        self.flow_rate = flow_rate_kg_s
        self.temp = loop_temp_K
        self.specific_heat = 128  # J/kg·K for molten lead
        self.density = 10600  # kg/m^3
        self.current_amp = 0
        self.coil_turns = 0

    def compute_heat_transfer(self, delta_temp):
        # Calculate heat carried by molten lead per second
        return self.flow_rate * self.specific_heat * delta_temp

    def set_emp_parameters(self, coil_turns, current_amp):
        self.coil_turns = coil_turns
        self.current_amp = current_amp

    def emp_pulse_energy(self):
        # Calculate energy stored in the magnetic field for pulse discharge
        mu_0 = 4 * 3.1415e-7  # Magnetic constant
        area = 0.1  # m^2 (loop cross-section)
        length = 1.0  # m (coil length)
        inductance = mu_0 * (self.coil_turns**2) * area / length
        energy = 0.5 * inductance * (self.current_amp**2)
        return energy

    def jet_assist_thrust(self, velocity_exit_m_s):
        # Calculate MHD-style thrust from conductive jet ejection
        return self.flow_rate * velocity_exit_m_s  # Momentum = m * v

    def energy_recoil_thrust(self, pulse_energy_kJ):
        # Simulate recoil-style thrust from burst radiation (EMP)
        c = 3e8  # Speed of light
        return (pulse_energy_kJ * 1000) / c  # F = E/c

    def full_status(self):
        return {
            "Heat Transfer (kW)": round(self.compute_heat_transfer(100) / 1000, 2),
            "EMP Pulse Energy (J)": round(self.emp_pulse_energy(), 2),
            "Jet Thrust (N)": round(self.jet_assist_thrust(50), 2),
            "Recoil Thrust (N)": round(self.energy_recoil_thrust(self.emp_pulse_energy() / 1000), 6)
        }
