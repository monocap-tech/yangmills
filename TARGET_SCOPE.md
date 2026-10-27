# Target scope and native proof obligation (reviewer specification)

**Prepared:** 2026-10-27. **Status:** Specification and research design, **not a theorem or a certified RG construction**. Native checkpoint: [YM-R126](ym/checkpoints/YM_HEAD_R126_20261027.json); next native pass: YM-R127. Historical R103 scope obligations remain relevant.

## 1. Full problem versus this investigation

The Clay Yang–Mills existence and mass-gap problem asks for a mathematically rigorous, nontrivial quantum Yang–Mills theory on four-dimensional Euclidean space for **each compact simple gauge group** with a **positive mass gap**. The exact axioms/requirements are those in the [Clay problem statement](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf), not an abbreviated statement invented here.

This repository investigates **necessary or sufficient ingredients within a proposed Bałaban-style constructive route**, not the whole problem as a single theorem. It has **not fixed and audited a complete target specification** (group-by-group construction, gauge-invariant observable algebra, precise finite-volume lattice measures, topology of convergence, order of volume/UV limits, renormalization conditions, reconstruction map, or spectral estimates). That omission is itself an open *specification* obligation. Describing the investigation as applying to all gauge groups would currently overstate it.

No reader should treat the following schematic notation as an already instantiated object in the native source papers.

## 2. Typed comparison question at the current frontier

Let \(N\) and \(N+1\) represent two ultraviolet cutoff depths. For an eventual native proof, specify:

- A compact simple group \(G\) (or a uniform family of such groups) and a finite lattice/volume model with spacing \(a_N\), field variables, gauge fixing, and finite-cutoff action/measure.
- Two actual RG histories, each with its own domain sequence \(\Omega^{(N)}_j\), admissible background \(U^{(N)}_j\), source \(E^{(N)}_j\), weakening/localization apparatus, marginal coefficients, and constraints.
- The physical-scale alignment map between levels \(j\) and \(j+1\) (R70–R75 discuss a candidate \(a_{N,j}=L^j L^{-N}\) alignment); this is **not** a proof that the underlying random variables or operators are the same.
- Explicit comparison maps between the two *gauge, Gaussian, source, and operator carriers*. These maps must have the domains, norms, Jacobians, and normalization factors required by the actual construction.
- A source-native norm on local/weighted observables and a precise treatment of any roots, derivatives, and volume/counting factors.

The *desired* two-cutoff comparison gate is a bound on properly transported physical-scale observables (or on a sufficiently strong family of RG outputs) of the schematic form

\[
\big\|\mathcal T_{N+1\to N}\mathcal O^{(N+1)}_{j+1}
       -\mathcal O^{(N)}_j\big\|_{\mathcal B}
\leq \varepsilon_{N,j},
\]

with enough uniformity and summability to support the intended Cauchy/coherence argument. Here \(\mathcal T\), \(\mathcal O\), \(\mathcal B\), the indices, and the required sum are **placeholders awaiting source-native definition**; no numerical exponent or summable family is certified. Even a proof of such a gate would **not** alone yield continuum existence, OS reconstruction, nontriviality, or a mass gap.

YM-R104 recovered a **same-domain** analytic relative-background response from CMP99(3). YM-R105 has shown that exact physical spacing and independent source regularity do **not** entail the external proposed pair input — nested domain sequences and identical prescribed gauge data on shared layers. Its further type distinction is deterministic minimizer/covariance fibers versus the **actual normalized RG probability laws**. YM-R106 now constructs a single gauge-invariant finite-Wilson observable cospan and exact normalized coupling/complement accounting; **YM-R107** recovers the source CMP109 averaging alternatives and restricted-kernel normalization distinction; **YM-R108** now separates source orbit identity and cutoff/kernel mass; **YM-R109** has now printed-image-verified the local FP normalization; **YM-R110** types the true post-linearization Gaussian cutoff as a pullback, conditional normalized fluctuation law and explicit finite-step error gates; **YM-R111** eliminates the nonlinear cutoff displacement by exact monitored projection P h=0; **YM-R112** must evaluate the actual covariance/chart and paired-law defect. Neither the original Bałaban source-pair conditions nor a quantitative full-history comparison follows from single-apparatus CMP99(3) analyticity.

## 3. Exact algebra versus admissible source comparison

Suppose every object below exists as an operator on the **same specified vector space** and all compositions, boundary conditions, and norms are compatible. Then the identity

\[
K(\Omega_1,U_1)-K(\Omega_0,U_0)
=[K(\Omega_1,U_1)-K(\Omega_0,U_1)]
+[K(\Omega_0,U_1)-K(\Omega_0,U_0)]
\]

is an algebraic telescoping identity.

**Required additional applicability conditions:**

1. \(K(\Omega_0,U_1)\), the intermediate operator, must actually be defined: \(U_1\) must be admissible on \(\Omega_0\) in the required source chart, not only on \(\Omega_1\).
2. The two-domain theorem must apply to \((\Omega_0,\Omega_1)\) **at the same background \(U_1\)**, with all hypotheses on domain sequences, local coefficients, operator families, and constants satisfied.
3. The second difference must have a **separately proved** estimate under \(U_0\to U_1\) at fixed \(\Omega_0\).
4. Cutoff-dependent gauge and Gaussian carriers must be explicitly transported **before** subtracting operators. Transport may produce additional defects and normalization terms not displayed in the two-bracket algebra.
5. Source-supported *spatial* distance-to-changed-domain estimates cannot be substituted for decay in *age of inherited coupling/history* without a separate theorem.

If any condition fails, the identity as written is not a usable source theorem. R103 contains negative-control examples showing why domain locality by itself is insufficient.

## 4. What is already internally checked

The abstract fixed-point comparison bound is standard: if \(F_0,F_1\) act on one complete invariant metric/normed space and both have Lipschitz constant \(\le q<1\), with fixed points \(d_0,d_1\), then

\[
\|d_1-d_0\|\le \frac{\|F_1(d_0)-F_0(d_0)\|}{1-q}.
\]

This statement is a *self-contained elementary derivation*. Its proof needs only one-line telescoping plus the contraction inequality. It does **not** certify the common \(q\), common chart, marked spatial norm, or uniform RG-scale bounds needed for the Yang–Mills construction.

## 5. Minimum new source-level evidence

YM-R106 supplied an exact SU(2) finite-Wilson observable cospan and a full-Wilson small-field-only obstruction, *not* a native Bałaban pairing. YM-R127 must either (a) instantiate an actual cutoff-pair carrier selection/coupling with the draft's exact paired-Ω/V requirements **and** correct normalized measure marginals, or (b) isolate a source-specific reason the proposed pairing/observable route is inapplicable. The external candidate's minimizer/covariance/root estimates are not verified native theorems. **A new conditional lemma or an analogy to another field theory is not gate closure.**

Separate future obligations remain: one-step polarization extraction and Bałaban CMP109 Eq. (0.29), the large-field construction, limits in UV and volume, OS reconstruction, and the positive spectral gap. See [RESEARCH_STATUS.md](RESEARCH_STATUS.md) for the open-gate ledger.

**Evidence boundary:** This is a draft target specification for review; all uninstantiated quantities are intentionally left marked rather than guessed.