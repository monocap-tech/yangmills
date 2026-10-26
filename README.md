# Yang–Mills — constructive renormalization-group research notes

**An independent, AI-assisted mathematical research notebook on four-dimensional pure Yang–Mills theory, focused on Bałaban's constructive renormalization-group program.**

> **Research status: OPEN / UNPROVED.** This repository does **not** claim a rigorous construction of the four-dimensional continuum Yang–Mills theory, satisfaction of the Osterwalder–Schrader axioms, or a strictly positive physical mass gap. Its many numbered passes contain source audits, mathematical reductions, conditional interfaces, and explicitly unresolved proof obligations. They have not been independently peer-reviewed.

| Canonical state | Value |
| --- | --- |
| Last completed native pass | **[YM-R103](ym/passes/YM_R103_CMP99_DOMAIN_MARK_NONLINEAR_MINIMIZER_AUDIT_20261014.md)** — 2026-10-14 |
| Next native cursor | **YM-R104** — not yet consumed |
| Official research checkpoint | **[YM_HEAD_R103](ym/checkpoints/YM_HEAD_R103_20261014.json)** |
| Public status snapshot | **2026-10-26** (documentation update, not a new proof pass) |

## Start here

| Document | Purpose |
| --- | --- |
| **[Research status and evidence ledger](RESEARCH_STATUS.md)** | What was actually established, under what hypotheses, and which native gates remain open |
| **[YM-R103 investigation](ym/passes/YM_R103_CMP99_DOMAIN_MARK_NONLINEAR_MINIMIZER_AUDIT_20261014.md)** | Latest source-text result, two-history operator decomposition, fixed-point stability interface, and counterexamples |
| **[R103 source receipt](ym/source_receipts/YM_R103_CMP99_3_MARKED_DOMAIN_RECEIPT_20261014.md)** | Primary-paper locations, third-party text provenance, and the original-image verification boundary |
| **[Terminology registry](ym/terminology/YM_R103_TERMINOLOGY_REGISTRY_20261014.md)** | Definitions and distinctions specific to the current frontier |
| **[External research interfaces](EXTERNAL_RECONCILIATION.md)** | Proposed comparison with new constructive Yang–Mills research; no external claim adopted as proved |
| **[YM-R75 investigation](ym/passes/YM_R75_BETA_INDEX_SEMANTICS_PHYSICAL_SCALE_STATIONARITY_20260922.md)** | Earlier marginal-beta / vacuum-polarization source question and its conditional reduction |

The historical research record remains in `ym/passes/`, `ym/checkpoints/`, `ym/references/`, `ym/source_receipts/`, and `ym/terminology/`. These documents are not intended to be read as a single, completed proof.

## Technical synopsis

The current focus is the gap between **local one-step RG estimates** and a sufficiently uniform **two-cutoff continuum comparison**. In earlier passes, alignment of physical lattice spacing reduced the marginal-beta coherence question to an appropriate covariance or decay estimate for the freshly extracted one-step vacuum-polarization tensor. It did *not* prove that estimate.

R102–R103 separate two effects that would otherwise be conflated:

- **Spatial-domain motion:** for certain source operators, a third-party text transcription of Bałaban's CMP 99(3), Theorem 3.14, supports an extra distance-to-domain-change factor from random-walk cancellation, subject to its stated hypotheses.
- **Background, coupling-history, and carrier motion:** comparing genuinely different ultraviolet-cutoff histories also changes operator coefficients, nonlinear minimizers, source charts, gauge constraints, and possibly Gaussian carriers. A spatial domain mark does **not** automatically control those changes.

The basic conditional decomposition is

```text
K(Ω₁,U₁) − K(Ω₀,U₀)
  = [K(Ω₁,U₁) − K(Ω₀,U₁)]
  + [K(Ω₀,U₁) − K(Ω₀,U₀)],
```

**only after identifying a common operator carrier**. The first bracket is domain motion; the second is background/coefficient motion. R103 also proves an abstract fixed-point difference inequality when two maps share a uniform contraction factor, but no suitable common weighted contraction margin has yet been certified for the actual two-cutoff Yang–Mills data.

The native frontier therefore remains: **background-sensitive propagator and nonlinear-minimizer response, actual gauge/carrier identification, rooted historical decay, and the marginal/remainder source estimates**. Large-field closure, continuum/OS construction, and the spectral mass gap remain separate unresolved requirements. See the [complete gate ledger](RESEARCH_STATUS.md).

## Evidence discipline

We distinguish:

- **Source-text witness** from **original publisher-image verification**; OCR can corrupt mathematical symbols and hypotheses.
- **Abstract mathematical deductions** from a **proof that their hypotheses hold** for the lattice-gauge construction.
- **A result about one RG trajectory** from **a uniform estimate comparing two trajectories**.
- **Domain-distance decay** from **decay in inherited coupling-history age**.
- **External announcements or draft manuscripts** from **independently verifiable theorems**.

The project retains failed transfers and counterexamples rather than silently promoting conditional reasoning to closure. The [status ledger](RESEARCH_STATUS.md) gives the operational evidence categories and gate-closure criteria.

## Relationship to newer work

On 2026-10-26, OpenAI [announced](https://openai.com/index/building-scientific-understanding-with-academic-communities/) an AI-generated Yang–Mills **existence** result built on Bałaban's approach; its physics proof artifacts were not publicly released in that announcement, and it did not claim a positive mass gap. The [Sussman–Alpöge research repository](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment) and [Armstrong's O(N) formalization](https://github.com/scottnarmstrong/balaban-lean) offer separate public lines of investigation. They are **leads for precise comparison**, not results incorporated into this project's theorem ledger.

See [External research interfaces](EXTERNAL_RECONCILIATION.md) for the proposed comparison protocol. **YM-EXT-01 is proposed work, not a completed native pass.**

## Scope and contributions

This is a reproducible **research/evidence trail**, not a priority assertion or proof announcement. Contributions are most useful when they cite an exact pass, theorem, page, norm, assumption, and counterexample-sensitive transfer step. In particular, source-image corrections, independent checks of the two-cutoff interface, and sharply stated obstructions are welcome research inputs.

**Last public-status review:** 2026-10-26. **Research frontier as recorded:** 2026-10-14, YM-R103.
