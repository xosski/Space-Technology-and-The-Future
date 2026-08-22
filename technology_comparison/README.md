# Theoretical Technology Comparison Tool

This package discovers every first-level technology family in the archive and assigns it a transparent engineering screening model. It currently covers 159 project directories and the standalone module file.

The calculations answer questions such as:

- How much electrical output and waste heat follow from an assumed conversion efficiency?
- How does assumed storage specific energy compare with present-day Li-ion cells?
- What radiator area is required at a stated temperature and emissivity?
- Do thrust, mass flow, input power, specific impulse, and delta-v close consistently?
- What does a conventional free-space communications link budget permit?
- What passive attenuation or charged-particle gyroradius follows from stated shielding inputs?
- What oxygen, carbon-dioxide, water, and processing margins follow from crew and mission duration?
- What known-physics energy lower bound applies to a relativistic transit claim?

## Important limitation

Default scenarios are **illustrations, not predictions**. The archive generally does not contain measured parameters. The tool therefore never treats a narrative claim as a measured input. Biomedical concepts receive an evidence-readiness calculation rather than an invented dose-response model, and program initiatives receive a requirements/verification completeness model.

## Usage

Generate a Markdown comparison covering every family:

```powershell
python -m technology_comparison --root . --output technology-comparison.md
```

Generate JSON:

```powershell
python -m technology_comparison --root . --json --output technology-comparison.json
```

Override defaults for one or more technologies:

```json
{
  "Propulsion-and-Vehicles/VAPS(vapor assisted plasma system)": {
    "thrust_n": 2.0,
    "mass_flow_kg_s": 0.00005,
    "wet_mass_kg": 1200,
    "dry_mass_kg": 800,
    "input_power_kw": 50
  }
}
```

```powershell
python -m technology_comparison --root . --assumptions assumptions.json
```

Overrides should come from a test result, a controlled simulation, or a clearly labeled design assumption. The generated report includes every input so comparisons remain auditable.

## Present-day references

Representative defaults are centralized in `baselines.py` and can be updated independently of the formulas. Sources include NASA's Small Spacecraft Technology State-of-the-Art survey, NASA propulsion reports, NASA's Life Support Baseline Values and Assumptions Document, and NASA's ISS ECLSS overview. Values are screening references rather than vendor guarantees.
