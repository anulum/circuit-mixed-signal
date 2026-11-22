<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
CIRCUIT-MIXED-SIGNAL — repository foundation
-->

# Decision: coordinate mixed-signal seams via Circuit Flow without coupling sibling solver repositories

## Context

Mixed-signal chips fail at the seams between digital control, analogue bias/clocking and electro-optic links, yet importing digital, analogue and photonic packages into one monolith would tangle their toolchains.

## Decision

**What Circuit Mixed-Signal owns:**
- coupled operation;
- coupled result;

**What it imports:** Circuit Core, Circuit Technology and Circuit Flow.

**Owned elsewhere:**

| Responsibility | Owner |
|---|---|
| RTL and digital formal/synthesis | Circuit Digital |
| transistor-level SPICE and jitter | Circuit Analog |
| optical waveguide simulation | Circuit Photonics |
| workflow dispatch | Circuit Flow |
| sign-off verdicts | Circuit Acceptance |

## Consequences

**What can be qualified now:** repository governance and validation tooling, before domain code exists.

**What it cannot qualify:** unimplemented schemas, solvers, hardware or sign-off verdicts.

**Architectural consequences:**
- Circuit Mixed-Signal imports only Circuit Core, Circuit Technology and Circuit Flow, consuming sibling results as digest-pinned records;
- power sequencing, PLL lock qualification, reset ordering and calibrated macromodel error bounds have one dedicated owner.
