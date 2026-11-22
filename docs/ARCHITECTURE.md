<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
CIRCUIT-MIXED-SIGNAL — repository foundation
-->

# Repository architecture

## Current executable tooling

**What it contains:** the repository's metadata, source-provenance, workflow, dependency-alignment, documentation, inventory and preflight controls.

**What each control does:** it inspects its fixed, declared local scope.

**What received metadata cannot do:** select another acceptance policy or grant domain authority.

Foundation qualification is in progress.

## Intended domain boundaries

| Record | Responsibility | Required evidence |
| --- | --- | --- |
| Coupled operation | Co-simulation specification binding digital, analogue, electro-optic and chiplet boundary views, multi-rail `dv/dt` supply ramp schedules, PLL lock-detect rules and reset release ordering | Explicit assume-guarantee seam contracts and multi-corner SPICE macromodel calibration digests |
| Coupled result | Cross-domain timing, voltage, quantisation/threshold and sequencing waveforms, macromodel error-propagation bounds and seam-obligation verdicts | Bounded approximation error propagated into margin checks across all supply-ramp and reset corners |

## Licence isolation

- **Separate-process copyleft engines.** Permissive co-simulation glue runs in-process, while any copyleft simulator engine invoked through the mixed-signal tool profile runs strictly in a separate process.

## Planned record schemas

- `circuit_mixed_signal.coupled_operation.v1`
- `circuit_mixed_signal.coupled_result.v1`

These are planned identifiers. None of them is registered or qualified here.

Read [validation tooling](validation-tooling.md) for the executable repository interfaces.
