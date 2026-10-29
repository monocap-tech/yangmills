# YM-AUX-04 — Exact normal-flux exclusion and CMP99 Dirichlet source-entry discrimination

**Date:** 2026-10-28. **Previous main:** 3f63732b6127294e56a298c0bbec792800610d48 (merged AUX-03). **Type:** self-contained exact discrete theorem, independently executed integer checks, lower-custody primary-paper OCR source-interface audit. **Canonical:** YM-R149 completed; YM-R150 **UNCONSUMED / SOURCE_DATA_HOLD**. Four-dimensional continuum Yang–Mills existence, OS and mass gap unproved.

## 0. Native question

AUX-03 gave a divergence-free four-dimensionally liftable field with all *regionally selected* CMP109 linear coarse-link constraints zero yet nonzero regional boundary-normal mean. Does this obstruct the **source-supported** Gaussian fluctuation, whose original CMP99 operators use Dirichlet regional boundary conditions? The earlier auxiliary witness is globally supported; support and topology are decisive. This pass derives a necessary flux test, not another artificial counterexample.

## 1. Exact normal flux conservation (DERIVATION / THEOREM)

On the complete periodic discrete torus T_N^d (any d>=2), let a_μ(x) take values in any finite-dimensional real vector space, with positive-axis bonds and the ordinary backward lattice divergence
`(div a)(x)=Σ_{μ=1}^d [a_μ(x)-a_μ(x-e_μ)]`.

Fix a normal coordinate μ and define the full-transverse-slice flux
`Φ_μ(s)=Σ_{x_⊥∈T_N^{d-1}}a_μ(s,x_⊥)`.

Sum div a=0 over all sites with x_μ=s. Every transverse forward/backward difference cancels by periodicity; the normal component gives
`0=Φ_μ(s)-Φ_μ(s-1)`.
Thus
`BOXED: div a=0 ⇒ Φ_μ(s) is independent of s.` (AUX04.1)

If the normal component vanishes throughout even ONE complete transverse slice, `Φ_μ(s0)=0`, then `Φ_μ(s)=0` for ALL s. Consequently the mean normal bond component on any set of complete transverse slices (not only a contiguous strip) is EXACTLY zero:
`BOXED: div a=0 AND Φ_μ(s0)=0 ⇒ mean_{B_Y}a_μ=0.` (AUX04.2)

In particular, if a has **zero-extension / Dirichlet support** in a region A that omits one entire μ-transverse lattice slice, the hypothesis Φ(s0)=0 follows. One does not need the coarse-link constraint D_Ya=0 for this specific mean conclusion. This is a finite discrete conservation/orthogonality theorem, not a coercivity estimate.

**Geometric passport:** A nontrivial supported co-closed normal flux can survive only if its support projects onto **every** normal slice. If a legitimate Dirichlet domain misses a full slice, ordinary div-free normal flux is automatically zero. This condition is sufficient, not asserted necessary in arbitrary irregular shapes. Full-torus flux may persist even in the presence of positive plaquette energy; co-closedness alone does not force it away.

## 2. Independent AUX-03 revalidation and its exclusion on a zero-flux carrier

Run the exact AUX-03 construction at L=13, N=L²=169 in d=2:
`a=h-338 Σ_{j=0}^{12}q_{(7,13j)}`,
where h_1(x)=1, h_2(x)=0, and q are oriented elementary plaquette circulations.

An independent reconstruction and execution rechecked **all 26 selected source-shaped coarse-link constraints**, **all 169²=28,561 divergence equations**, and mean_{B_Y}a_1=1. In addition, for EVERY one of the 169 transverse slices,
`BOXED: Φ_1(s)=169` (AUX04.3).
Each q has zero complete-slice flux; the constant h supplies the nonzero conserved flux. Therefore this field cannot satisfy *any* genuine zero-normal-flux side condition, and it is not supported on the one-plane strip: outside it, horizontal bonds have value 1 on ordinary slices.

This yields a precise **negative admission** of AUX-03's *specific witness* to the declared carrier `{a: div a=0, Φ_1(s0)=0}` and to any zero-extended strip missing a complete transverse slice. It **does not** refute AUX-03, whose hypotheses never included zero-flux or strip support.

For comparison, a single plaquette circulation q supported entirely on two neighboring normal slices is co-closed and has Φ_1(s)=0 everywhere. The independent script checks this control on 28,561 sites.

## 3. Exact unweighted curvature-energy passport, NOT source Hessian K

For the same AUX-03 field, the independently computed full-torus scalar positive-bond 2-norm and ordinary oriented plaquette-curl norm are
`||a||²=5,969,249=209·169²,`
`||d a||²=29,703,440=1040·169²,`
so
`BOXED: ||da||²/||a||²=1040/209≈4.9760765550.` (AUX04.4)

Explanation: the 13 disjoint q have 4 nonzero bonds apiece; h is orthogonal to each q in the complete bond ℓ² metric, giving `||a||²=N²+13·4·338²`. Each plaquette circulation has curl 4 on its central plaquette and -1 on each of its four edge-neighbors, disjoint across j, giving `||da||²=13·(16+4)·338²`. Thus the prior witness has **manifestly nonzero naive plaquette energy**; it is not even a low-Rayleigh field for that elementary quadratic proxy. This is NOT a lower bound for CMP99 source A_k or the CMP109 exponential-gauge reduced precision K; exact weight and gauge/metric must be obtained independently.

## 4. New source-native interface, and an important non-equivalence

Pinned OCR of the **original CMP99 article**, Bałaban, *Propagators for lattice gauge theories in a background field*, CMP 99(3) (1985), 389–434, at `chboishabba/dashi_agda`, `Docs/support/reference/balaban-source-extracts/cmp99-background-propagators.txt`, immutable blob `ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743`, around printed pp.427–428, heading **E. Unit Lattice Propagators** and (3.155)–(3.158), states in legible prose that unit-lattice covariances require **Dirichlet boundary conditions outside some domain A**. Immediately after (3.156), it restricts the quadratic form to a subspace with fields vanishing outside A and additional local exclusions and Q1B=0, and reconstructs constrained bonds through a nearly local C.

**Evidence label: ORIGINAL-PAPER TEXT IN THIRD-PARTY OCR ONLY.** The exact superscripts/indices in the subspace are OCR-damaged; p.428 Eq.(3.156) as scanned image has NOT been independently recovered. This is source evidence of a support/Dirichlet *type*, **not** a certified source operator formula, exact domain A, gauge-divergence identity, or a reconstruction of source K. In particular, `Q1B=0` is a block-average constraint, **not** a verified equality to ordinary `div a=0`. CMP109's B' gauge, source H_k and CMP99 historical gauge differ.

**Type-safe transfer conditions:** To apply AUX04.2 to an actual source regional fluctuation, prove all:
(A) identify an admissible original CMP99/CMP109 Ω,Λ, Dirichlet field support;
(B) its normal-direction geometry omits a full transverse slice or implies zero total normal flux;
(C) its **actual** relevant gauge-fixed field satisfies ordinary divergence on the whole torus, or supplies a valid covariant/weighted flux identity *with independently proved telescoping*;
(D) source C, Hilbert metric, and precision A^(k) genuinely match that field; and
(E) this carrier is the one used in the actual two-cutoff normalized-law comparison.

**NONTRANSFER:** The source OCR's Dirichlet phrase alone cannot supply (B) or (C), and the source block constraint Q1B=0 cannot be substituted for div a=0. Nor can exclusion of harmonic flux imply uniform coercivity K≥α; R149 requires the actual operator and alpha.

## 5. Disposition / obligation graph

- **CLOSED (self-contained):** divergence-free transverse flux conservation (AUX04.1); exact zero-flux-slice sufficiency (AUX04.2); AUX-03 necessarily nonzero flux everywhere; independent curvature/energy certificate.
- **SOURCE TEXT LOCATED (lower custody):** CMP99 p.427–428 explicitly discusses Dirichlet support for unit-lattice Gaussian; original image and exact fields still pending.
- **NEGATIVE RESULT:** AUX-03 globally supported counterexample is **inadmissible** to the explicitly typed zero-normal-flux/zero-extension strip carrier; does **not** invalidate native positivity.
- **OPEN SOURCE INTERFACE:** original CMP99 images; exact regional Dirichlet/gauge and whether the source carrier has (A)–(E); CMP109 actual K/α, interaction/FP/partition and normalized two-UV laws.
- **UNPROVED:** continuum 4D YM, OS and physical mass gap.

**Stopping point:** This is a carrier-admission discriminator, not another unrestricted numerical counterexample. The AUX-03 diagnostic should not be used again to question the native Gaussian until the source field's boundary flux and gauge are typed. **YM-R150 remains unconsumed under SOURCE_DATA_HOLD**; canonical R149 checkpoint unchanged. No YM-R151 and no generic follow-on inequality passes without original source entry.
