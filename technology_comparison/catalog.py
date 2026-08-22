"""Discover every first-level technology family and assign a calculation model."""

from dataclasses import dataclass
from pathlib import Path


DOMAINS = (
    "Armaments",
    "Comms-and-Systems",
    "Energy-and-Power",
    "Medical",
    "Modules",
    "Programs-and-Initiatives",
    "Propulsion-and-Vehicles",
    "Shielding-and-Defense",
    "Space-Time-and-Research",
    "Waste-Management",
)


@dataclass(frozen=True)
class TechnologyFamily:
    path: str
    name: str
    domain: str
    model: str
    rationale: str


def _classify(domain: str, name: str) -> tuple[str, str]:
    text = name.casefold()
    if domain == "Energy-and-Power":
        if "solar" in text:
            return "solar_power", "solar collection and specific-power comparison"
        if any(word in text for word in ("battery", "capacitor", "flywheel", "reserve", "overdrive-cell")):
            return "energy_storage", "stored-energy, runtime, and mass comparison"
        if any(word in text for word in ("cool", "thermal", "ferroflow")):
            return "thermal_control", "heat-rejection and radiator-area calculation"
        return "power_generation", "energy conversion, waste heat, and specific power"
    if domain == "Propulsion-and-Vehicles":
        return "propulsion", "thrust, specific impulse, delta-v, and power closure"
    if domain == "Shielding-and-Defense":
        return "shielding", "passive attenuation and charged-particle deflection bounds"
    if domain == "Armaments":
        return "power_limited_payload", "non-operational energy, storage, and heat burden"
    if domain == "Comms-and-Systems":
        return "communications", "free-space link budget and ideal channel capacity"
    if domain == "Medical":
        if any(word in text for word in ("life support", "biosuit", "eden chamber", "cyrohalo")):
            return "life_support", "crew metabolic loads and process margins"
        return "biomedical_readiness", "evidence gate; no unvalidated dose-response model"
    if domain == "Space-Time-and-Research":
        return "relativistic_bound", "known-physics energy lower bound"
    if domain == "Waste-Management":
        return "waste_processing", "throughput, power, and specific-energy comparison"
    if domain == "Modules":
        return "integrated_module", "combined power, thermal, and crew-support closure"
    return "program_readiness", "requirements and verification completeness"


def discover_technologies(root: str | Path) -> list[TechnologyFamily]:
    root = Path(root)
    technologies: list[TechnologyFamily] = []
    for domain in DOMAINS:
        directory = root / domain
        if not directory.exists():
            continue
        entries = sorted(directory.iterdir(), key=lambda path: path.name.casefold())
        for entry in entries:
            if entry.name.startswith("."):
                continue
            model, rationale = _classify(domain, entry.stem if entry.is_file() else entry.name)
            technologies.append(
                TechnologyFamily(
                    path=entry.relative_to(root).as_posix(),
                    name=entry.stem if entry.is_file() else entry.name,
                    domain=domain,
                    model=model,
                    rationale=rationale,
                )
            )
    return technologies
