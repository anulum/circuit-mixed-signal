<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
CIRCUIT-MIXED-SIGNAL — repository foundation
-->

# Circuit Mixed-Signal

Circuit Mixed-Signal is being built to coordinate coupled digital, analogue and electro-optic co-simulation through Circuit Flow — verifying compositional assume-guarantee boundary contracts, calibrated behavioural macromodel error bounds, multi-rail power ramp sequencing, phase-locked-loop lock qualification and synchronous reset release ordering — completely deterministically without AI. This checkout contains repository validation tooling and documentation only. Full foundation qualification is in progress. There is no installed mixed-signal co-simulation runner, macromodel calibrator, sequencing checker or qualified record schema.

**What does not exist yet:**
- a coupled co-simulation coordinator or macromodel calibration checker;
- a registered runtime record schema;
- a qualified mixed-signal interface model.

## Boundary

**What this project owns:**

| Record | Scope |
|---|---|
| Coupled operation | Co-simulation specification binding digital, analogue, electro-optic and chiplet boundary views, multi-rail `dv/dt` supply ramp schedules, PLL lock-detect rules and reset release ordering |
| Coupled result | Cross-domain timing, voltage, quantisation/threshold and sequencing waveforms, macromodel error-propagation bounds and seam-obligation verdicts |

**Static imports:** Circuit Core, Circuit Technology and Circuit Flow.

**Records read without importing domain code:**

| Source | Records consumed |
|---|---|
| Circuit Core, Circuit Technology and Circuit Flow | entity references, design views, operation profiles, system budgets, technology profiles and run plans |
| Circuit Digital | digital operations and formal/synthesis results |
| Circuit Analog | analogue studies and post-extraction results |
| Circuit Photonics | electro-optic photonic results |
| Circuit Assembly | chiplet and 3D stack interface specifications |

**Capability registration and handoffs:** Registers the mixed-signal tool-profile manifest with Circuit Core and delivers coupled results to Circuit Physical, Circuit Acceptance, Circuit Lab and Spike Encoder Characteriser.

**Explicit non-claims and operating boundaries:**
- It imports Circuit Core, Circuit Technology and Circuit Flow only — never importing Circuit Digital, Circuit Analog or Circuit Photonics code directly.
- Every coupled verification run works deterministically without machine learning.
- Uncalibrated real-number behavioural models cannot stand for transistor-level physics at sign-off.

## Current tooling

Repository controls inspect:
- metadata and source attribution;
- workflows and dependency alignment;
- native documentation and repository inventory;
- preflight orchestration.

Metadata declares architecture-only maturity with empty implemented domain capability and claim inventories.

- Use the exact environment in [Contributing](CONTRIBUTING.md).
- Full CI and preflight belong in CI or in an explicitly admitted pre-push environment.
- See [Validation](VALIDATION.md) for the maintained validation scope.

## Intended evidence

Every future domain artefact will carry the platform's common provenance envelope, its source and environment digests, its confidentiality compartment and its explicit verification boundary. None of the planned record schemas is registered or qualified by this foundation.

## Documentation and support

Read [Architecture](ARCHITECTURE.md), [support](SUPPORT.md), [security reporting](SECURITY.md) and [citation metadata](CITATION.cff).

**Not claimed:**
- a hosted service, released package or DOI;
- a public CI status;
- a performed simulation, hardware measurement or sign-off verdict.

## Licence

Source is licensed under [AGPL-3.0-or-later](LICENSE). A commercial licence is available through the contact in [NOTICE](NOTICE.md).

![ANULUM](docs/assets/anulum_logo_company.jpg)

![Fortis Studio](docs/assets/fortis_studio_logo.jpg)

## Text and data mining reservation
The rightsholder, Miroslav Šotek (ANULUM), expressly reserves the use of the
works in this repository for text and data mining, including the collection of
this content for, and its use in, training, fine-tuning or evaluating machine
learning and artificial intelligence models, in accordance with Article 4(3) of
Directive (EU) 2019/790 and the national provisions transposing it.

No permission for such use has been granted beyond what the licence in
`LICENSE` grants. This reservation does not change that licence: uses the
licence permits remain permitted on its terms, including its attribution and
share-alike conditions.

Reservation made on 2026-11-22. Requests for permission: contact the
rightsholder through the contact listed in this repository.
