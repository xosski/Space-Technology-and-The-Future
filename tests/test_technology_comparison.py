import math

from technology_comparison.catalog import discover_technologies
from technology_comparison.models import calculate, propulsion, thermal_control


def test_every_archive_family_has_a_runnable_model():
    technologies = discover_technologies(".")
    assert len(technologies) == 160
    assert len({technology.path for technology in technologies}) == 160
    for technology in technologies:
        result = calculate(technology.model)
        assert result["illustrative_only"] is True
        assert result["outputs"]


def test_propulsion_uses_rocket_equation_and_power_closure():
    result = propulsion(
        {
            "thrust_n": 1.0,
            "mass_flow_kg_s": 0.0001,
            "wet_mass_kg": 1000,
            "dry_mass_kg": 500,
            "input_power_kw": 10,
        }
    )
    assert math.isclose(result["specific_impulse_s"], 10_000 / 9.80665)
    assert math.isclose(result["delta_v_m_s"], 10_000 * math.log(2))
    assert math.isclose(result["ideal_jet_power_kw"], 5.0)
    assert math.isclose(result["minimum_power_closure"], 0.5)


def test_radiator_area_rejects_requested_heat():
    result = thermal_control(
        {"heat_load_kw": 10, "radiator_temperature_k": 350, "emissivity": 0.85}
    )
    assert result["radiated_flux_w_m2"] > 0
    assert math.isclose(
        result["required_radiator_area_m2"] * result["radiated_flux_w_m2"],
        10_000,
    )


def test_unphysical_inputs_are_rejected():
    try:
        calculate("power_generation", {"efficiency": 1.1})
    except ValueError as error:
        assert "efficiency" in str(error)
    else:
        raise AssertionError("efficiency above one must fail")
