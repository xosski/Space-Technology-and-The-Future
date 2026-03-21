
# photon_drive_model.py
# Models thrust over time from a photon propulsion system using Ghost Core TPV

class PhotonDrive:
    def __init__(self, power_watts, ship_mass_kg):
        self.power = power_watts
        self.mass = ship_mass_kg
        self.c = 3e8

    def acceleration(self):
        return self.power / (self.mass * self.c)

    def velocity_after(self, time_seconds):
        return self.acceleration() * time_seconds

    def distance_traveled(self, time_seconds):
        return 0.5 * self.acceleration() * (time_seconds**2)
