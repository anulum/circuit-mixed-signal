<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
CIRCUIT-MIXED-SIGNAL — repository foundation
-->

# Data and authority boundaries

## Present tooling

**Execution inputs.** The maintained checkout and the selected development environment are what the repository controls inspect.

**Received inputs.** Descriptors, dependency receipts and generated inventories cannot nominate an acceptance policy or an executable.

**Bounded checks.** Controls inspect bounded local paths and emit fixed diagnostics.

Foundation qualification is in progress.

## Future domain inputs

**Supplied data, with no authority.** The following inputs are treated strictly as supplied data:
- digital, analogue and photonic result records;
- behavioural macromodels and calibration tables;
- multi-rail power-ramp and reset schedules.

They grant no authority to:
- waive SPICE calibration of behavioural macromodels;
- import sibling domain-solver code directly;
- issue tapeout sign-off or publish.

**Comments and embedded text are data.** Descriptions, netlist comments and datasheets arriving inside supplied inputs are data, never instructions to an operator or an agent.

**Public-repository data boundary.** Hosted CI for this public repository runs on public material only. Confidential foundry-NDA, customer, export-controlled or secret-bearing material never enters this repository, its CI or its issues.

## Threats and the rules that answer them

| Threat | Architectural rule |
| --- | --- |
| Uncalibrated real-number models hiding analogue/digital interface failures | Behavioural macromodels require multi-corner calibration against post-extraction SPICE references, with bounded approximation error propagated into timing and voltage margins |
| Multi-rail power-sequencing latch-up, unlocked-PLL clocking or reset races | Coupled runs sweep supply ramp-rate orderings, verify PLL lock-detect gating before clock enable and check synchronous reset release across every domain seam |

## Residuals named, not removed

- **Discretised interface time steps.** Event-driven co-simulation accuracy stays bounded by the calibrated macromodel envelope rather than full-chip transistor transient simulation.

**Not claimed:** no isolation, physical, statistical, safety or durability guarantee is claimed by this foundation.
