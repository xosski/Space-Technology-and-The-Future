"""Physics and engineering screening calculations.

All default inputs are illustrative scenarios. Results are not predictions of an
archive concept unless measured or design-controlled parameters replace the defaults.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Mapping

from .baselines import BASELINES

G0 = 9.80665
SIGMA = 5.670374419e-8
C = 299_792_458.0
PROTON_MASS = 1.67262192369e-27
ELEMENTARY_CHARGE = 1.602176634e-19


def _positive(values: Mapping[str, float], *names: str) -> None:
    for name in names:
        if float(values[name]) <= 0:
            raise ValueError(f"{name} must be positive")


def power_generation(p: Mapping[str, float]) -> dict[str, float]:
    _positive(p, "input_power_kw", "system_mass_kg")
    efficiency = float(p["efficiency"])
    if not 0 < efficiency <= 1:
        raise ValueError("efficiency must be in (0, 1]")
    output = float(p["input_power_kw"]) * efficiency
    specific = output * 1000 / float(p["system_mass_kg"])
    return {
        "electric_output_kw": output,
        "waste_heat_kw": float(p["input_power_kw"]) - output,
        "specific_power_w_kg": specific,
        "specific_power_vs_solar": specific / BASELINES["space_solar_specific_power"].value,
    }


def energy_storage(p: Mapping[str, float]) -> dict[str, float]:
    _positive(p, "system_mass_kg", "specific_energy_wh_kg", "load_kw")
    energy = float(p["system_mass_kg"]) * float(p["specific_energy_wh_kg"]) / 1000
    baseline_energy = float(p["system_mass_kg"]) * BASELINES["space_li_ion_specific_energy"].value / 1000
    return {
        "stored_energy_kwh": energy,
        "runtime_hours": energy / float(p["load_kw"]),
        "same_mass_li_ion_kwh": baseline_energy,
        "specific_energy_vs_li_ion": float(p["specific_energy_wh_kg"])
        / BASELINES["space_li_ion_specific_energy"].value,
    }


def solar_power(p: Mapping[str, float]) -> dict[str, float]:
    _positive(p, "area_m2", "solar_flux_w_m2", "array_mass_kg")
    efficiency = float(p["efficiency"])
    if not 0 < efficiency <= 1:
        raise ValueError("efficiency must be in (0, 1]")
    power = float(p["area_m2"]) * float(p["solar_flux_w_m2"]) * efficiency
    specific = power / float(p["array_mass_kg"])
    return {
        "beginning_of_life_power_kw": power / 1000,
        "specific_power_w_kg": specific,
        "specific_power_vs_reference": specific / BASELINES["space_solar_specific_power"].value,
    }


def thermal_control(p: Mapping[str, float]) -> dict[str, float]:
    _positive(p, "heat_load_kw", "radiator_temperature_k")
    emissivity = float(p["emissivity"])
    if not 0 < emissivity <= 1:
        raise ValueError("emissivity must be in (0, 1]")
    background = float(p.get("background_temperature_k", 3.0))
    if not 0 <= background < float(p["radiator_temperature_k"]):
        raise ValueError("background_temperature_k must be nonnegative and below radiator temperature")
    flux = emissivity * SIGMA * (float(p["radiator_temperature_k"]) ** 4 - background**4)
    return {"radiated_flux_w_m2": flux, "required_radiator_area_m2": float(p["heat_load_kw"]) * 1000 / flux}


def propulsion(p: Mapping[str, float]) -> dict[str, float]:
    _positive(p, "thrust_n", "mass_flow_kg_s", "wet_mass_kg", "dry_mass_kg", "input_power_kw")
    wet, dry = float(p["wet_mass_kg"]), float(p["dry_mass_kg"])
    if wet <= dry:
        raise ValueError("wet_mass_kg must exceed dry_mass_kg")
    exhaust_velocity = float(p["thrust_n"]) / float(p["mass_flow_kg_s"])
    isp = exhaust_velocity / G0
    jet_power_kw = 0.5 * float(p["mass_flow_kg_s"]) * exhaust_velocity**2 / 1000
    return {
        "specific_impulse_s": isp,
        "delta_v_m_s": exhaust_velocity * math.log(wet / dry),
        "acceleration_m_s2": float(p["thrust_n"]) / wet,
        "ideal_jet_power_kw": jet_power_kw,
        "minimum_power_closure": jet_power_kw / float(p["input_power_kw"]),
        "isp_vs_chemical": isp / BASELINES["chemical_rocket_isp"].value,
        "isp_vs_electric": isp / BASELINES["electric_thruster_isp"].value,
        "thrust_per_power_n_kw": float(p["thrust_n"]) / float(p["input_power_kw"]),
    }


def communications(p: Mapping[str, float]) -> dict[str, float]:
    _positive(
        p,
        "frequency_hz",
        "distance_m",
        "transmit_power_w",
        "transmit_gain_linear",
        "receive_gain_linear",
        "bandwidth_hz",
        "system_temperature_k",
    )
    wavelength = C / float(p["frequency_hz"])
    path_loss = (4 * math.pi * float(p["distance_m"]) / wavelength) ** 2
    received = (
        float(p["transmit_power_w"])
        * float(p["transmit_gain_linear"])
        * float(p["receive_gain_linear"])
        / path_loss
    )
    noise = 1.380649e-23 * float(p["system_temperature_k"]) * float(p["bandwidth_hz"])
    snr = received / noise
    return {
        "free_space_path_loss_db": 10 * math.log10(path_loss),
        "received_power_dbw": 10 * math.log10(received),
        "snr_db": 10 * math.log10(snr),
        "shannon_capacity_bps": float(p["bandwidth_hz"]) * math.log2(1 + snr),
    }


def shielding(p: Mapping[str, float]) -> dict[str, float]:
    _positive(p, "areal_density_kg_m2", "mass_attenuation_m2_kg", "particle_energy_mev", "magnetic_field_t")
    optical_depth = float(p["areal_density_kg_m2"]) * float(p["mass_attenuation_m2_kg"])
    kinetic_j = float(p["particle_energy_mev"]) * 1e6 * ELEMENTARY_CHARGE
    momentum = math.sqrt(kinetic_j**2 / C**2 + 2 * kinetic_j * PROTON_MASS)
    radius = momentum / (ELEMENTARY_CHARGE * float(p["magnetic_field_t"]))
    return {
        "passive_transmission_fraction": math.exp(-optical_depth),
        "passive_attenuation_percent": 100 * (1 - math.exp(-optical_depth)),
        "proton_gyroradius_m": radius,
        "shield_mass_for_area_kg": float(p["areal_density_kg_m2"]) * float(p.get("protected_area_m2", 1.0)),
    }


def life_support(p: Mapping[str, float]) -> dict[str, float]:
    _positive(
        p,
        "crew",
        "mission_days",
        "oxygen_capacity_kg_day",
        "co2_capacity_kg_day",
        "water_use_kg_person_day",
    )
    crew, days = float(p["crew"]), float(p["mission_days"])
    oxygen = crew * days * BASELINES["crew_oxygen"].value
    co2 = crew * days * BASELINES["crew_co2"].value
    water_demand = crew * days * float(p["water_use_kg_person_day"])
    recovery = float(p["water_recovery_fraction"])
    if not 0 <= recovery <= 1:
        raise ValueError("water_recovery_fraction must be in [0, 1]")
    return {
        "oxygen_required_kg": oxygen,
        "co2_generated_kg": co2,
        "oxygen_daily_margin_kg": float(p["oxygen_capacity_kg_day"]) - crew * BASELINES["crew_oxygen"].value,
        "co2_daily_margin_kg": float(p["co2_capacity_kg_day"]) - crew * BASELINES["crew_co2"].value,
        "water_makeup_required_kg": water_demand * (1 - recovery),
        "water_makeup_vs_iss_reference": (1 - recovery) / (1 - BASELINES["iss_water_recovery"].value),
    }


def waste_processing(p: Mapping[str, float]) -> dict[str, float]:
    _positive(p, "throughput_kg_day", "specific_energy_kwh_kg", "operating_hours_day")
    daily = float(p["throughput_kg_day"]) * float(p["specific_energy_kwh_kg"])
    return {"daily_energy_kwh": daily, "average_operating_power_kw": daily / float(p["operating_hours_day"]), "annual_throughput_tonnes": float(p["throughput_kg_day"]) * 365 / 1000}


def relativistic_bound(p: Mapping[str, float]) -> dict[str, float]:
    _positive(p, "vehicle_mass_kg", "acceleration_time_s")
    fraction = float(p["speed_fraction_c"])
    if not 0 < fraction < 1:
        raise ValueError("speed_fraction_c must be in (0, 1)")
    gamma = 1 / math.sqrt(1 - fraction**2)
    energy = (gamma - 1) * float(p["vehicle_mass_kg"]) * C**2
    return {"lorentz_factor": gamma, "kinetic_energy_j": energy, "minimum_average_power_w": energy / float(p["acceleration_time_s"]), "mass_energy_fraction": gamma - 1}


def power_limited_payload(p: Mapping[str, float]) -> dict[str, float]:
    _positive(p, "energy_per_operation_kwh", "operations_per_hour", "system_efficiency", "radiator_temperature_k")
    if float(p["system_efficiency"]) > 1:
        raise ValueError("system_efficiency must not exceed 1")
    input_energy = float(p["energy_per_operation_kwh"]) / float(p["system_efficiency"])
    average_power = input_energy * float(p["operations_per_hour"])
    rejected = average_power * (1 - float(p["system_efficiency"]))
    radiator = thermal_control({"heat_load_kw": max(rejected, 1e-12), "radiator_temperature_k": p["radiator_temperature_k"], "emissivity": p.get("emissivity", 0.85)})
    return {"input_energy_per_operation_kwh": input_energy, "average_input_power_kw": average_power, "li_ion_mass_per_operation_kg": input_energy * 1000 / BASELINES["space_li_ion_specific_energy"].value, "waste_heat_kw": rejected, "radiator_area_m2": radiator["required_radiator_area_m2"]}


def readiness(p: Mapping[str, float]) -> dict[str, float]:
    fields = ("physics", "requirements", "model", "test_data", "safety", "integration")
    values = [float(p.get(field, 0)) for field in fields]
    if any(not 0 <= value <= 1 for value in values):
        raise ValueError("readiness inputs must be fractions in [0, 1]")
    return {"evidence_completeness_percent": 100 * sum(values) / len(values), "completed_evidence_gates": float(sum(value >= 1 for value in values)), "total_evidence_gates": float(len(fields))}


def integrated_module(p: Mapping[str, float]) -> dict[str, float]:
    power = power_generation(p)
    thermal = thermal_control({"heat_load_kw": power["waste_heat_kw"], "radiator_temperature_k": p["radiator_temperature_k"], "emissivity": p["emissivity"]})
    crew = life_support(p)
    return {**power, **thermal, **crew}


DEFAULT_SCENARIOS: dict[str, dict[str, float]] = {
    "power_generation": {"input_power_kw": 1000, "efficiency": 0.30, "system_mass_kg": 5000},
    "energy_storage": {"system_mass_kg": 100, "specific_energy_wh_kg": 500, "load_kw": 10},
    "solar_power": {"area_m2": 10, "solar_flux_w_m2": 1361, "efficiency": 0.30, "array_mass_kg": 30},
    "thermal_control": {"heat_load_kw": 100, "radiator_temperature_k": 350, "emissivity": 0.85},
    "propulsion": {"thrust_n": 1, "mass_flow_kg_s": 0.000034, "wet_mass_kg": 1000, "dry_mass_kg": 700, "input_power_kw": 20},
    "communications": {"frequency_hz": 8.4e9, "distance_m": 384.4e6, "transmit_power_w": 20, "transmit_gain_linear": 1000, "receive_gain_linear": 1e6, "bandwidth_hz": 1e6, "system_temperature_k": 150},
    "shielding": {"areal_density_kg_m2": 10, "mass_attenuation_m2_kg": 0.01, "particle_energy_mev": 100, "magnetic_field_t": 1, "protected_area_m2": 100},
    "life_support": {"crew": 4, "mission_days": 365, "oxygen_capacity_kg_day": 4, "co2_capacity_kg_day": 5, "water_use_kg_person_day": 3.5, "water_recovery_fraction": 0.90},
    "waste_processing": {"throughput_kg_day": 100, "specific_energy_kwh_kg": 2, "operating_hours_day": 8},
    "relativistic_bound": {"vehicle_mass_kg": 1000, "speed_fraction_c": 0.01, "acceleration_time_s": 31_557_600},
    "power_limited_payload": {"energy_per_operation_kwh": 1, "operations_per_hour": 10, "system_efficiency": 0.25, "radiator_temperature_k": 350, "emissivity": 0.85},
    "program_readiness": {"physics": 0, "requirements": 0, "model": 0, "test_data": 0, "safety": 0, "integration": 0},
    "biomedical_readiness": {"physics": 0, "requirements": 0, "model": 0, "test_data": 0, "safety": 0, "integration": 0},
    "integrated_module": {"input_power_kw": 100, "efficiency": 0.30, "system_mass_kg": 1000, "radiator_temperature_k": 350, "emissivity": 0.85, "crew": 4, "mission_days": 30, "oxygen_capacity_kg_day": 4, "co2_capacity_kg_day": 5, "water_use_kg_person_day": 3.5, "water_recovery_fraction": 0.90},
}

MODELS: dict[str, Callable[[Mapping[str, float]], dict[str, float]]] = {
    "power_generation": power_generation, "energy_storage": energy_storage, "solar_power": solar_power,
    "thermal_control": thermal_control, "propulsion": propulsion, "communications": communications,
    "shielding": shielding, "life_support": life_support, "waste_processing": waste_processing,
    "relativistic_bound": relativistic_bound, "power_limited_payload": power_limited_payload,
    "program_readiness": readiness, "biomedical_readiness": readiness, "integrated_module": integrated_module,
}


def calculate(model: str, parameters: Mapping[str, float] | None = None) -> dict[str, object]:
    if model not in MODELS:
        raise KeyError(f"unknown model: {model}")
    inputs = dict(DEFAULT_SCENARIOS[model])
    if parameters:
        inputs.update(parameters)
    return {"model": model, "illustrative_only": True, "inputs": inputs, "outputs": MODELS[model](inputs)}


def headline(result: Mapping[str, object]) -> str:
    outputs = result["outputs"]
    assert isinstance(outputs, dict)
    preferred = {
        "power_generation": "specific_power_w_kg", "energy_storage": "runtime_hours",
        "solar_power": "specific_power_w_kg", "thermal_control": "required_radiator_area_m2",
        "propulsion": "specific_impulse_s", "communications": "shannon_capacity_bps",
        "shielding": "passive_attenuation_percent", "life_support": "oxygen_daily_margin_kg",
        "waste_processing": "average_operating_power_kw", "relativistic_bound": "kinetic_energy_j",
        "power_limited_payload": "average_input_power_kw", "program_readiness": "evidence_completeness_percent",
        "biomedical_readiness": "evidence_completeness_percent", "integrated_module": "specific_power_w_kg",
    }
    key = preferred[str(result["model"])]
    return f"{key}={outputs[key]:.4g}"
