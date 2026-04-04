# Spacecraft Gaps Analysis (Workdir-Based)

Date: 2026-04-04  
Repository: `space-technology-and-the-future`

## Executive Summary

The workdir contains a large number of subsystem concepts (propulsion, power, shielding, comms, life-support, armaments), but the spacecraft program is currently **concept-rich and integration-poor**.  
The primary gap is not idea generation; it is **system engineering closure**: requirements, interfaces, budgets, verification, and staged test evidence.

If the goal is to produce a viable spacecraft architecture, the most important needs are:

1. A mission-driven baseline design (one reference vehicle, one mission profile).
1. Closed subsystem budgets (mass, volume, power, thermal, data-rate, reliability).
1. A verification pipeline that progressively proves claims from simulation to hardware testing.

## What Exists Today (Strong Coverage)

The repository already has broad concept coverage for major spacecraft-adjacent domains:

1. **Propulsion Concepts**: multiple drive families and vessel narratives (Lazarus, FTG/Revenant, plasma/induction variants).
1. **Energy Concepts**: reactor, battery, cooling, and thermal-routing ideas.
1. **Protection Concepts**: shielding and EM/spectral defense documentation.
1. **Comms/Detection Concepts**: relay, scanner, and long-range sensing documents.
1. **Crew/Survival Concepts**: biosuit and life-support oriented documents.

This means ideation is not the bottleneck.

## Critical Gaps (What Is Needed)

## P0: Mission And System Definition Gaps

1. **No single mission baseline**: no fixed target mission (LEO transfer, cislunar cargo, deep-space probe, etc.) to constrain engineering.
1. **No top-level spacecraft requirements**: missing measurable requirements (delta-v, payload mass, endurance, crew/uncrewed mode, comms latency, fault tolerance).
1. **No system architecture baseline**: no authoritative Block Definition Diagram / internal architecture that all subsystems map to.

Needed output: a single `Spacecraft System Requirements (SSR)` and `System Architecture Baseline (SAB)` document.

## P0: Integration And Interface Gaps

1. **No interface control documents (ICDs)** between power, propulsion, thermal, avionics, comms, and structures.
1. **No command/data model** defining onboard buses, telemetry schema, timing, and fault flags.
1. **No integration ownership map** showing subsystem boundaries, assumptions, and dependencies.

Needed output: ICD package with electrical/mechanical/thermal/data interfaces for each subsystem pair.

## P0: Engineering Budget Closure Gaps

1. **No mass budget** by subsystem and growth margin.
1. **No power budget** for nominal, peak, contingency, and safe mode.
1. **No thermal budget** with source/sink accounting and off-nominal scenarios.
1. **No propellant/consumables budget** with mission phase breakdown.

Needed output: a versioned `Master Budget Table` (mass-power-thermal-data-propellant) with uncertainty bounds.

## P0: Verification And Evidence Gaps

1. **Concept papers dominate over validated results**.
1. **Limited reproducible simulation workflow** (inputs, assumptions, outputs, pass/fail criteria).
1. **No formal test ladder** from benchtop to integrated subsystem to environmental test.

Needed output: a `Verification & Validation Plan` with TRL gates and explicit evidence required per gate.

## P1: Flight-Critical Subsystem Gaps

1. **GNC stack definition is incomplete**: sensors, state estimation, control laws, autonomy boundaries, mode logic.
1. **Avionics and software assurance plan missing**: FDIR, watchdog architecture, redundancy, timing determinism, software lifecycle.
1. **Structures/material qualification missing**: loads, fatigue, vibration, thermal cycling, outgassing, radiation aging.
1. **TT&C architecture not closed**: antenna configs, link budgets, fallback channels, loss-of-signal recovery logic.

Needed output: subsystem design specs with acceptance criteria and qualification matrices.

## P1: Safety, Operations, And Program Gaps

1. **Hazard analysis missing**: FMEA/FMECA, fault trees, hazard controls, operational constraints.
1. **ConOps not formalized**: launch, orbit insertion, cruise, anomaly handling, deorbit/disposal.
1. **Ground segment definition missing**: mission operations center, command authority, telemetry pipelines, procedure packs.
1. **Configuration management process weak**: no clear baseline/release discipline for design artifacts and test evidence.

Needed output: Safety case + ConOps + mission operations handbook + change-control workflow.

## P2: Cross-Cutting Research Gaps

1. **Physics claim stratification needed**: separate conventional/near-term physics from speculative tracks.
1. **Traceability gap**: many claims are not linked to equations, references, or reproducible models.
1. **Duplicate concept drift** across directories without canonical source-of-truth documents.

Needed output: a three-lane R&D framework (`Conventional`, `Advanced`, `Speculative`) with evidence standards per lane.

## Minimum Viable Spacecraft Package (What To Build Next)

To move from repository concepts to a buildable spacecraft program, create these 10 artifacts first:

1. `Mission Definition Document (MDD)`
1. `Spacecraft System Requirements (SSR)`
1. `System Architecture Baseline (SAB)`
1. `Interface Control Document Set (ICD)`
1. `Master Budget Table (MBT)`
1. `Guidance, Navigation, and Control Spec (GNC-S)`
1. `Avionics & Software Assurance Plan (ASAP)`
1. `Verification & Validation Plan (VVP)`
1. `Safety and Hazard Analysis Package (SHA)`
1. `Concept of Operations + Ground Segment Plan (ConOps/GSP)`

Without these, subsystem documents cannot be credibly integrated into a flight program.

## Suggested 12-Week Execution Sequence

1. **Weeks 1-2**: Lock mission baseline and produce SSR v1.
1. **Weeks 3-4**: Freeze architecture and interfaces (SAB + ICD v1).
1. **Weeks 5-6**: Close first-order budgets (mass/power/thermal/data/propellant).
1. **Weeks 7-8**: Define GNC and avionics safety modes; establish software and telemetry standards.
1. **Weeks 9-10**: Build V&V matrix and test ladder; define TRL entry/exit criteria.
1. **Weeks 11-12**: Consolidate safety case, ConOps, and go/no-go review package.

## Practical Recommendation

Pick exactly **one reference spacecraft** (for example: uncrewed deep-space demonstrator) and force all existing subsystem concepts to either:

1. Map to it with measurable parameters, or
1. Move to a separate speculative research lane.

This single decision will remove most ambiguity and expose the true engineering gaps quickly.
