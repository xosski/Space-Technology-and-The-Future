"""Configurable present-day comparison points.

These are representative engineering reference values, not records or procurement
specifications. Mission and vendor data should replace them in serious trade studies.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Benchmark:
    value: float
    unit: str
    label: str
    source: str
    note: str


BASELINES = {
    "space_li_ion_specific_energy": Benchmark(
        250.0,
        "Wh/kg",
        "representative rechargeable Li-ion cell",
        "https://www.nasa.gov/smallsat-institute/sst-soa/power-subsystems/",
        "Cell-level illustrative value; qualified pack performance is usually lower.",
    ),
    "space_solar_specific_power": Benchmark(
        100.0,
        "W/kg",
        "representative deployed small-spacecraft solar array",
        "https://www.nasa.gov/smallsat-institute/sst-soa/power-subsystems/",
        "Illustrative system-level value; orbit, pointing, degradation, and packaging matter.",
    ),
    "chemical_rocket_isp": Benchmark(
        450.0,
        "s",
        "upper-end chemical rocket specific impulse",
        "https://ntrs.nasa.gov/citations/20220006853",
        "NASA describes chemical propulsion as below roughly 450 s.",
    ),
    "electric_thruster_isp": Benchmark(
        3000.0,
        "s",
        "representative flight electric-propulsion specific impulse",
        "https://ntrs.nasa.gov/citations/20220006853",
        "Representative ion-thruster value; electric systems span a wide range.",
    ),
    "electric_thrust_per_power": Benchmark(
        0.075,
        "N/kW",
        "small-spacecraft electric-propulsion thrust-to-power reference",
        "https://www.nasa.gov/wp-content/uploads/2021/10/4.soa_in-space_propulsion_2021.pdf",
        "NASA reports electric propulsion generally below 75 mN/kW.",
    ),
    "crew_oxygen": Benchmark(
        0.89,
        "kg/person-day",
        "reference astronaut oxygen demand",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC8398003/",
        "Conservative daily respiration estimate including exercise.",
    ),
    "crew_co2": Benchmark(
        1.0,
        "kg/person-day",
        "illustrative crew carbon-dioxide load",
        "https://ntrs.nasa.gov/citations/20210024855",
        "Use mission metabolic schedules from NASA BVAD for detailed sizing.",
    ),
    "iss_water_recovery": Benchmark(
        0.90,
        "fraction",
        "ISS water recovery reference",
        "https://www.nasa.gov/reference/environmental-control-and-life-support-systems-eclss",
        "NASA states that the ISS currently recovers about 90 percent of water.",
    ),
}


SOURCES = tuple(sorted({benchmark.source for benchmark in BASELINES.values()}))
