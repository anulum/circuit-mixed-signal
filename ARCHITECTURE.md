<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
CIRCUIT-MIXED-SIGNAL — repository foundation
-->

# Architecture

## Current executable surface

The checkout contains:
- repository validation tooling;
- dedicated tests;
- workflow definitions;
- native documentation.

No domain component of Circuit Mixed-Signal is implemented yet. The metadata keeps domain capabilities, claims and qualified record formats empty.

## Intended data flow

1. **Macromodel calibration check** verifies that any event-driven real-number model matches post-extraction SPICE references across supply and temperature corners within declared error bounds.
2. **Coupled co-simulation** dispatches coordinated digital, analogue and electro-optic runs through Circuit Flow across multi-rail ramp-up, brown-out, PLL lock and synchronous reset-release sequences.
3. **Seam closure** checks every cross-domain assume-guarantee obligation against the top-level system budget.

## Ownership

**This project owns** the planned Circuit Mixed-Signal records and boundary rules.

**Owned elsewhere:**

| Responsibility | Owner |
|---|---|
| RTL and digital formal/synthesis | Circuit Digital |
| transistor-level SPICE and jitter | Circuit Analog |
| optical waveguide simulation | Circuit Photonics |
| workflow dispatch | Circuit Flow |
| sign-off verdicts | Circuit Acceptance |

## Interpretation

- **Macromodels.** A behavioural pass holds only within its calibrated SPICE corner and slew envelope.

Read [the documentation architecture](docs/ARCHITECTURE.md) for the planned records, domain rules and schema identifiers.
