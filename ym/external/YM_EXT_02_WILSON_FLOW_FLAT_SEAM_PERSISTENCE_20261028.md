# YM-EXT-02 — Flat-holonomy persistence under Wilson gradient flow

**Date:** 2026-10-28. **Research classification:** exact finite SU(2) lattice derivation/counterexample + external manuscript applicability audit. **Predecessors:** YM-R125/R126 winding geometry and normalized law gate, YM-R149 precision checkpoint, YM-R150 source-data stop. **Canonical native cursor:** YM-R150 **UNCONSUMED**. **Claim status:** UNPROVED_RESEARCH_PROGRAM. No continuum 4D Yang–Mills, OS construction or spectral mass gap.

## 0. Question and external provenance boundary

A newly posted 2026-10-26 **three-dimensional**, periodic-torus SU(2) manuscript introduces positive-time Wilson-flow Wilson-loop observables: Patrick Lopatto and P. M. Aronow, *The continuum limit of three-dimensional SU(2) lattice Yang–Mills theory on a torus III: Regional renormalization and large-field control*, version 1, https://hexagonmath.org/2610.00510v1 . Its **public abstract** describes lattice Wilson action gradient flow, positive-time Wilson-loop observables, a refinement-class convergence claim and a program of Bałaban-type regional RG combined with large-field and reflection-positivity tools. The page identifies the manuscript as **primarily AI-generated** with **no parts human-understood**, and its provenance statement mentions model-generated discovery/verification and limited Lean formalization.

**Evidence boundary:** only the external landing-page abstract/provenance was used here. This is NOT independent mathematical verification of any 3D construction; it is not a 4D existence/mass-gap theorem and not an input to CMP109 native K or normalized two-cutoff law. The manuscript's actual proof files and PDF were not audited for this note. Its method is relevant as an **observable-carrier proposal**, not theorem transfer.

**Refute-first question:** Could flowing Wilson loops for positive time remove R126's obstruction that identical local curvature/fields away from a seam fail to determine a global winding Wilson loop?

## 1. Exact flat-seam Wilson-flow persistence lemma (SELF-CONTAINED DERIVATION)

Work on a periodic cubic lattice T_N^d=(Z/NZ)^d, d=3 or 4, N≥3, with SU(2) positive oriented links. Let

  V = [[3/5,4/5],[-4/5,3/5]] ∈ SU(2)

(viewed as a real unitary matrix: V*V=I, det V=1). Define the seam configuration U^V by

  U_1(x)=V if x_1=N-1, and U_1(x)=I otherwise;
  U_j(x)=I for each j=2,...,d.

Define U^I by every link I. The seam is the periodic boundary crossing in the e1 direction. For every oriented elementary plaquette p, U^V(∂p)=I: plaquettes not containing e1 are trivial, and e1-ej plaquettes contain the same seam factor and its inverse on parallel e1 bonds, because the seam field is independent of transverse coordinates. Consequently the standard Wilson action

  S_W(U)=Σ_p [1-(1/2) Re Tr U(∂p)]

satisfies S_W(U^V)=S_W(U^I)=0. Since S_W is smooth and globally nonnegative on the finite compact product of SU(2) links, both configurations are critical points. Under its finite-lattice negative-gradient Wilson flow, which is uniquely defined by an ODE, **both configurations remain stationary for all t≥0**.

For the noncontractible e1-loop ℓ winding once around the torus, the ordered holonomy of U^V is V whereas U^I has I, so

  W_ℓ(U^V(t))=(1/2)Tr V=3/5 ≠ 1=(1/2)Tr I=W_ℓ(U^I(t))

for **all t≥0**. The difference is exact and gauge invariant.

On any link-observation region Ω not containing seam-crossing e1 bonds, the complete *local link restrictions* of U^V(t) and U^I(t) agree for every t≥0. They also have identical plaquette/curvature data globally. Therefore **no function solely of the flow-time local Ω field history or local curvature data can identify the global winding Wilson trace** on the full class of finite flat periodic connections.

This is a *stronger flow-stable instance* of R126's topological seam negative control. It does not say that the external 3D manuscript discards global holonomies; the abstract expressly uses Wilson loops. It rules out an **unjustified attempted transfer** that treats positive flow time as equivalent to capturing missing global topology.

## 2. Exact arithmetic custody and independent check

[Reproducible standard-library rational witness](../computations/YM_EXT_02_RATIONAL_WILSON_FLOW_SEAM_20261028.py) constructs the 3D N=3,4 torus link fields with Fraction arithmetic, checks VᵀV=I, det V=1, every plaquette U_p=I, the winding holonomy V, and all links in the seam-excluded slab x1<N-1 equal I. The d=4 extension follows identically, with the fourth-direction links set to I. Stationarity follows analytically from nonnegative smooth Wilson action at zero, **not** from approximate time integration or the script.

A separate identity configuration has all local observations identical and winding 1. The plaquette-statistic η=0 in both. No synthetic Gaussian A_test, invented source K, partition Z, relative UV history or continuum spectral statement is used.

## 3. Carrier consequence and actual limit of applicability

The admissible observable carrier for a **global winding** output must encode the winding class/holonomy, or an observable genuinely sufficient to determine it. A local Ω patch plus bounded curvature cannot be declared sufficient merely by evolving it through Wilson flow, even for infinite observation time, because these flat connections are stationary.

An observable family confined to contractible local Wilson loops can be treated separately, but replacing a global loop with such a local object changes the target theorem. Positive-time flow may improve regularity of gauge fields or short-scale observables; that fact, if proved externally, does not itself provide cross-UV normalized measure comparison or OS reflection positivity in four dimensions.

**Native applicability gate:** The present flat U^V/U^I witness is on a declared periodic model. Admission by *actual* Bałaban CMP109 source Ω/Λ, χ small-field chart, coupled backgrounds, and nested Dirichlet region is NOT established. If the true source Ω reaches every relevant winding cycle, the local-observation nonidentifiability premise need not hold; no source-native counterexample is claimed.

## 4. Determination, stopping point and jurisdiction

- **DERIVED / verified finite:** flat seam gives distinct global winding with identical plaquettes, and Wilson gradient flow leaves the pair stationary for all t≥0; seam-excluded local observations remain indistinguishable.
- **NEGATIVE RESULT:** positive-time flow alone cannot repair R126's missing topological observability if only seam-excluded Ω information is transported.
- **EXTERNAL CLAIM:** 2026 3D AI-heavy torus manuscript proposes a flowed-loop convergence strategy; NOT independently checked, NOT transplanted to 4D, NOT a source coercivity result.
- **OPEN:** admissibility of the model within actual CMP109 regions and cutoffs; original CMP99 (3.155)–(3.158) images; native finite K; complete weights/normalizers; two-UV laws; volume/UV summability; OS and positive physical gap.

**Cursor:** Native YM-R150 remains UNCONSUMED on SOURCE_DATA_HOLD, exactly as established at R149 and the two previous R150 source requests. No replacement checkpoint or invented YM-R151. This separate external/topology observation is now custodied and bounded. **Next action** for the main native frontier remains acquire primary CMP99 equation image or a complete legal CMP109 precision/region; for observable selection, preserve loop homology and explicitly state whether Ω contains the loop, rather than adding another generic Gaussian comparison.
