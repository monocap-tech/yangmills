# YM-R108 — additive source/type registry

Date 2026-10-26. [Pass](../passes/YM_R108_CMP109_GAUGE_ORBIT_CUTOFF_NORMALIZATION_AUDIT_20261026.md). Historical registries preserved.

- **BasedGaugeOrbitNormalizer** — a nonnegative w whose Haar average over each relevant compact gauge orbit is one. This permits R108.1 gauge-invariant integral preservation. Abstract exact; native CMP109 w not recovered from original image.
- **GaugeFixingNotPhysicalTilt** — exact Faddeev–Popov insertion need not alter a physical gauge-invariant law; nonconstant w is not proof of reweighting.
- **OrbitAveragedCutoffSelector** — sigma(x)=integral_H w(hx)chi(hx)dh; gauge-invariant, in [0,1] for chi in [0,1]; physical restricted weight on invariant observables R108.2.
- **KernelVersusCutoffMass** — normalized restricted output tilts original input by kappa_t*sigma (R108.3), not automatically by w alone; original source kappa and sigma OPEN.
- **MarkovTruncationTV** — if underlying t is Markov, restricted/unrestricted output law distance is at most 1-E sigma. No native uniform or summable bound.
- **ReferenceScalarLawCancellation** — positive coarse-field-independent N_ref cancels from normalized probabilities; it still differs from a full partition function in other contexts.
- **NativeR109FPSourceGate** — acquire source images around CMP109 (0.15)–(0.17), identify exact based gauge orbit, w, chi, native M/t and compute kappa, sigma, probability normalization at an aligned actual RG block.
