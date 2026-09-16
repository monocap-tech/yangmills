# Yang–Mills traversal ledger — YM-R0 through YM-R15

Date custodied: 2026-09-15
Repository: `monocap-tech/yangmills`
Status: append-only backfill from the live research thread
Claim status: UNPROVED_RESEARCH_PROGRAM
Current live pointer after this ledger: `YM-R16` (UNCONSUMED)

This ledger backfills the live traversal without rewriting the historical September 14 checkpoint. Earlier repository state remains historical evidence of the opening position; this file records the later sequence of bounded determinations.

## YM-R0 — opening statement / literature reconnaissance

**Target.** Type the Clay Yang–Mills existence-and-mass-gap problem before attempting a proof route.

**Determination.** The Clay problem is conjunctive: construct a nontrivial 4d quantum Yang–Mills theory satisfying axioms at least as strong as Wightman/Osterwalder–Schrader, and prove a positive spectral gap. The opening seam is not simply “prove exponential decay” or “remove the lattice cutoff”; it is compatibility of UV construction and IR mass generation along one continuum-producing trajectory.

**Initial candidate carrier.** A physically normalized quantity such as `m_lat(a)/a`, equivalently inverse physical correlation length, rather than a fixed dimensionless lattice gap.

## YM-R1 — scale-custody audit

**Target.** Compare what Bałaban RG, Magnen–Rivasseau–Sénéor (MRS), modern stochastic Yang–Mills, and strong-coupling lattice theory actually preserve.

**Determination.** The four programs preserve different objects: effective-action admissibility/locality (Bałaban), UV-renormalized Schwinger functions with an IR cutoff (MRS), gauge-orbit state-space/dynamics (modern stochastic programs), and long-distance decay/area-law information (strong coupling). No theorem supplies a common transport object connecting all four.

**Working hypothesis.** A useful carrier must combine continuum correlation control, reflection positivity, locality/OS compactness, correct UV behavior, and a quantitatively normalized decay/gap datum.

## YM-R2 — spectral-transport audit

**Target.** Audit the 2026 Faizal–Shabir spectral-RG claim specifically for physical normalization.

**Negative results.** The published argument, as read in the live thread, contains scale-normalization and inequality-direction defects. In particular, statements comparing transfer gaps across blocking steps can lose the factor `a_k/a_{k+1}`, and alternate clustering formulations similarly risk converting graph-distance decay into a physical Hamiltonian mass without carrying the lattice spacing.

**Determination.** Distinguish:

- contraction gap `1-lambda_2(T_a)`;
- dimensionless transfer exponent `-log lambda_2(T_a)`;
- physical Hamiltonian gap `-(1/a) log lambda_2(T_a)`.

Only the last is the Clay-relevant quantity.

## YM-R3 — two-scale / limit-commutation audit

**Target.** Separate RG blocking from regulator removal and infinite-volume removal.

**Determination.** The control problem is at least three-parameter: microscopic spacing `a`, volume/IR scale `L`, and RG depth `k`. Strong-coupling methods control the `L -> infinity` direction at fixed regulator; Bałaban gives substantial UV control in the `a -> 0` direction at finite volume. The joint uniform region needed for a continuum gap is not established.

**Useful formulation.** A target contract is a lower bound `M(a,L) >= M_* > 0` uniformly for small `a` and large `L` along the asymptotically-free trajectory.

## YM-R4 — dimensional-transmutation custody

**Target.** Test whether `M_gap / Lambda_YM` can serve as the invariant carrier.

**Determination.** Normalizing the gap to an RG-generated reference scale is physically natural, but it does not prove positivity. `Lambda_YM` fixes the permitted scale of a gap, not the existence of the gap. The numerical ratio is scheme-dependent although positivity is preserved under finite scheme changes.

**Refinement.** A finite-volume reference length `L_*`, defined by a renormalized coupling condition, may be a cleaner nonperturbative normalization. The target can be written `M_gap L_* >= c > 0`.

## YM-R5 — spectral detectability / completeness

**Target.** Determine whether a family of local correlators can certify the entire vacuum-sector spectrum.

**Determination.** After OS/Wightman reconstruction, Reeh–Schlieder-type cyclicity addresses qualitative detectability. If centered local vectors are dense in `Omega^perp` and there exists one common Euclidean-time exponent `m_* > 0` such that each centered local vector has a correlator bounded by `C_psi e^{-m_* t}`, then the spectral theorem gives `sigma(H) ∩ (0,m_*) = empty`.

**Critical quantifier.** `exists m_* > 0 for all local O`, not `for all O exists m_O > 0`.

## YM-R6 — uniform-exponent custody

**Target.** Audit constructive literature by quantifier strength.

**Determination.** Common-exponent clustering is not an exotic missing theorem: constructive Higgs and strong-coupling lattice results already exhibit this pattern. The missing uniformity is over the regulator and thermodynamic limits in physical units.

**Compressed certificate.** Instead of transporting all correlators independently, one may target `|| Q e^{-tH} Q || <= e^{-m_* t}` or its transfer-matrix analogue.

## YM-R7 — which gap?

**Target.** Separate stochastic-generator, correlation, transfer/Hamiltonian, and RG notions of “gap.”

**Determination.** These are distinct:

- Langevin/Markov gap: relaxation in stochastic time;
- correlation exponent: spatial/temporal mixing of the Euclidean measure;
- Hamiltonian gap: physical Euclidean-time spectrum after reconstruction;
- RG contraction: stability/irrelevance in theory space.

Only temporal-transfer/Hamiltonian gap is definitionally the Clay object. Langevin coercivity requires locality/mixing theorems to imply correlation decay. RG contraction has no generic implication to `Delta_H`.

## YM-R8 — transfer/RG commutation square

**Target.** Ask whether reflection-positive RG commutes with OS reconstruction strongly enough to transport spectral coercivity.

**Determination.** Weak commutation is possible: an RG can preserve reflection positivity so OS reconstruction exists at each scale. Strong spectral commutation is not automatic. Hamiltonian-renormalization literature already shows, even for free-field test cases, that path-integral-induced finite-scale Hamiltonian flows need not form a simple inductive/isometric spectral family.

**Key asymmetry.** Compression can increase the apparent gap; coarse gappedness does not imply fine gappedness. Low-energy fine states may lie in discarded sectors.

## YM-R9 — discarded-sector coercivity / Feshbach splice

**Target.** Test operator-theoretic spectral RG as a low-spectrum custody mechanism.

**Determination.** Smooth Feshbach/Schur methods can preserve the exact low-energy spectral question without assuming a global gap. They solve an information-loss problem, not the mass-generation problem. For Yang–Mills, a suitable gauge-invariant isospectral RG would still have to prove that the retained low-energy sector eventually excludes `(0,m_*)`.

**Missing object.** No established 4d pure non-Abelian constructive Feshbach RG was located that simultaneously preserves Gauss law/gauge symmetry, low-spectrum isospectrality, continuum control, and a uniform spectral exclusion estimate.

## YM-R10 — mass-generation control experiments

**Target.** Inspect rigorously controlled asymptotically free models (Gross–Neveu, 2d O(N) sigma) for the UV-to-massive-IR mechanism.

**Determination.** Rigorous UV constructions and rigorous IR mass-generation results in these models historically live in different regimes. The IR proofs often retain a UV cutoff. As the dynamically generated mass becomes exponentially small in cutoff units, one-scale cluster-expansion constants deteriorate like powers of the correlation length/volume.

**Working term.** `correlation-volume debt`: a one-shot IR expansion started at the UV cutoff must pay for an exponentially large correlation region.

**Architectural lesson.** Run weak-coupling RG shell by shell until an intermediate matching scale where the effective coupling is order one, then switch proof regime to a massive-IR theorem.

## YM-R11 — matching-scale / basin-entry audit

**Target.** Compare Bałaban effective-action classes with rigorous strong-coupling polymer/character-expansion domains.

**Determination.** No certified overlap was found. The two expansions are organized around different reference geometries:

- UV/Bałaban: near-flat/small-curvature fields plus controlled localized corrections;
- IR/strong coupling: plaquette weight close to the Haar/constant reference measure.

An order-one running coupling is not a sufficient handoff condition. The full effective action must enter an IR-admissible open set in interaction space.

## YM-R12 — massive-basin stability

**Target.** Determine whether a rigorously gapped lattice point generates an open neighborhood of gapped interactions.

**Determination.** Yes, in several rigorous topologies: polymer/Kotecký–Preiss stability, local mixing/functional-inequality stability, and Hamiltonian gap-stability theorems. For the Kogut–Susskind Hamiltonian at very strong coupling, the electric term is an explicit gapped rotor anchor and the plaquette term is a bounded local perturbation after normalization.

**Remaining defect.** These open basins are expressed in norms different from Bałaban's Euclidean RG norm.

## YM-R13 — norm-dictionary audit

**Target.** Compare Bałaban locality norms, polymer activity norms, and Hamiltonian interaction/form norms.

**Determination.** Bałaban already has an internal localized-polymer dictionary. The missing implication is from UV polymer smallness around the weak-field principal action to strong-coupling polymer smallness around the Haar reference point. A generic Euclidean-locality norm also does not automatically produce a local Hamiltonian interaction norm; reflection positivity and controlled temporal range are extra requirements.

**Simplification.** Avoid an intermediate Hamiltonian dictionary when possible: remain Euclidean, prove reflection positivity plus uniform physical-time clustering, and reconstruct the Hamiltonian only at the end.

## YM-R14 — reflection-positive RG cone

**Target.** Determine whether non-Abelian coarse-graining can preserve reflection positivity while retaining constructive UV control.

**Determination.** Reflection positivity is not intrinsically incompatible with RG. For an exact blocking map `Q`, if `Q Theta = Theta' Q` and positive-time coarse observables pull back to positive-time fine observables, then the pushforward of an RP measure remains RP. Special coarse-graining designs in Hamiltonian-RG and older lattice-gauge work support this architecture.

**Status against Bałaban.** No theorem was found establishing that every Bałaban 4d RG step preserves the OS half-space algebra. Nor was an impossibility found.

## YM-R15 — gauge fixing versus half-space locality

**Target.** Inspect the actual Bałaban machinery to locate the first operation that crosses a Euclidean-time reflection plane.

**Determination.** Block averaging and piecewise axial gauge can plausibly be arranged half-space locally when blocks and paths are aligned with the reflection plane. Background minimizers, Landau-gauge coordinates, and propagators are not strictly half-space local because they use inverses of elliptic operators with exponentially decaying but nonzero cross-plane kernels.

**Critical correction.** This analytic nonlocality does not itself destroy RP. If the *exact coarse measure* is the RP pushforward `Q_* mu`, then later background/gauge/propagator/cluster manipulations may be nonlocal proof coordinates while representing the same RP measure exactly.

**Revised carrier.** An exact RP coarse measure plus a separately controlled quasi-local analytic representation. Term-by-term manifest RP of every effective-action component is unnecessary.

## Current canonical frontier — YM-R16 (UNCONSUMED)

**Title.** Exact-pushforward custody.

**Next action.** For one actual non-Abelian Bałaban RG step, establish or falsify

`Q Theta = Theta Q`

and

`Q^* A'_+ subset A_+`.

Then classify each subsequent operation—delta constraint, axial-gauge insertion, Landau-gauge change, background expansion, small/large-field partition, localization, cluster expansion, and R-operation—as either:

1. an exact identity/reparametrization of `Q_* mu`, or
2. an approximation whose error must be tracked explicitly.

If all approximations remain inside exact remainder terms, RP belongs to the total coarse measure throughout and does not need to be manifest term by term.

## Non-promotion boundary

Nothing in YM-R0–R15 constitutes a proof of 4d Yang–Mills existence or the mass gap. The project currently has a progressively sharpened interface diagnosis. Proposed 2026 “solutions” remain audit targets, not installed theorems.

## Source linkage

Cumulative source IDs `[1]`–`[42]` are custodied separately in `ym/references/YM_REFERENCES_001_042_20260915.md`. Historical source IDs must not be renumbered in later passes.
