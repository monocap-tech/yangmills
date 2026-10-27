# YM-R105 — Actual cutoff-pair carrier admissibility and measure-law separation

**Date:** 2026-10-26. **Native previous head:** [YM-R104](../checkpoints/YM_HEAD_R104_20261026.json). **Status:** COMPLETE AS REFUTE-FIRST *SOURCE-APPLICABILITY* AUDIT; actual two-cutoff pairing, normalized Gaussian transport, and full RG-law coherence **OPEN**. **Next cursor:** YM-R106, unconsumed. **Claim status:** UNPROVED_RESEARCH_PROGRAM; no continuum Yang–Mills existence or positive mass-gap claim.

## 0. Recovery and exact jurisdiction

After YM-EXT-01's [direct YM4 crosswalk](../external/YM_EXT_01_EXTERNAL_YM4_NATIVE_CROSSWALK_20261026.md) and [RH-style typed-carrier supplement](../external/YM_EXT01_TYPED_CARRIER_CROSSWALK_20261026.md), the highest-value native question is no longer whether there exists *some* background perturbation theorem. R104 located CMP99(3) Theorem 3.4 / (3.65) / (3.86) in its own admissible chart. The question is whether the *actual two cutoff histories* of the proposed constructive theory are legal inputs for the conditional paired-variational and covariance/root comparison theorem in the external YM4 account.

This pass **does not** claim an independent proof of that external theorem. It checks its declared input type, gives an exact logical nonimplication concerning the older native physical-scale alignment, and isolates a further *law-versus-carrier* gap. The literature witness for CMP102b is bibliographic/abstract-level only, not direct publisher-image equations. Therefore no missing theorem is asserted to be absent from all Bałaban sources.

## 1. Primary and external provenance boundary

- Native [R75](YM_R75_BETA_INDEX_SEMANTICS_PHYSICAL_SCALE_STATIONARITY_20260922.md) and earlier R70 use \(\eta_N=L^{-N}\), \(\eta_{N,j}=L^j\eta_N\); exact *spacing* equality \(\eta_{N+1,j+1}=\eta_{N,j}\) is algebraic. R75 expressly does **not** certify equality of actual one-step polarization objects. R75's \(\beta_j\) semantics are traced partly through a **secondary source**.
- T. Bałaban, *The variational problem and background fields in renormalization group method for lattice gauge theories*, CMP **102**(2), 277–309 (1985), DOI [10.1007/BF01229381](https://doi.org/10.1007/BF01229381), is the correct **background variational** source. Do not confuse it with CMP102(2), 255–275 (3D ultraviolet stability), DOI 10.1007/BF01229380. The publisher metadata/abstract attests a minimum with fixed averages, unique modulo gauge transformations **under its hypotheses**; its full formula-level details were NOT inspected as publisher images in this pass.
- The external [Sussman–Alpöge YM4 draft](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/af96f9c5ec6d05a5c8f251256d87970d73b7f25a) raw Part III blob **6012ff578fb1c67c29651f1f4192ab59a4c862a3**, directly fetched again on 2026-10-26. Selected verified *text location* lines III:34655–34745, 35626–35659, 36675–36715, 36756–36807, 37398–37443, 37533–37560 and 111209–111275. This is an **unrefereed AI-assisted candidate construction**, not an accepted theorem. See [source receipt](../source_receipts/YM_R105_PAIRED_CARRIER_SOURCE_RECEIPT_20261026.md). Its Part III Chapter 13 openly inventories proof-outsanding inputs, including constrained minimizers and two-run comparisons.

## 2. Exactly what the *external* paired input requires

Part III §9.3, definition around lines 34655–34735, introduces an **admissible pair of variational problems**, not arbitrary RG runs:

- At coarse spacing \(\eta=L^{-k}\) and finer \(\eta'=\eta/L\), admissible **decreasing** domain sequences \(\boldsymbol\Omega=(\Omega_0,\dots,\Omega_k)\), \(\boldsymbol\Omega'=(\Omega'_0,\dots,\Omega'_{k+1})\). Domains have \(M_1L^j\eta\) block structure and a source distance/floor requirement (lines 34660–34668, 34729–34734).
- Determining layers \(\Lambda_j=(\Omega_j\setminus\Omega_{j+1})^{(j)}\), determining set \(\mathfrak B=\bigcup_j\Lambda_j\), with prescribed *configuration* data \(V\) satisfying plaquette small-curvature \(|(\partial V)(p')-1|<\varepsilon\) (lines 34669–34687).
- **Exact pairing constraint:** \(\Omega'_{j+1}=\Omega_j\), \(\Lambda'_{j+1}=\Lambda_j\), \(V'=V\) on these shared layers for every \(j\), plus \(\Omega'_0,V'|_{\Lambda'_0}\) chosen *subject to admissibility*. The finer minimizer is \(U_{\mathfrak B'}(V')\), and \(W:=M(U_{\mathfrak B'}(V'))\) is the one-step average (lines 34713–34726).
- Level-weighted relative norm \(\|A\|_\theta=\max(|A|_{(-1-\theta)},|\nabla_U A|_{(-2-\theta)})\) and geometric floor \(\delta_0RM_1\ge16\log L\) (lines 34698–34710 and 34729–34734).

The source's theorem around III:35626–35641 *claims*, for exactly such a pair, a gauge transformation \(\mathsf u\) and \(A\) with
\[
W^{\mathsf u}=\exp(i\eta A)U_{\mathfrak B}(V),\quad
\|A\|_\theta\le C_A\varepsilon\eta^\theta,
\]
plus gauge and averaging constraints. The subsequent covariance theorem III:36675–36697 explicitly works with common **unit-lattice** data and a whole torus or interior bonds separated from the small-field boundary; III:36766–36782 claims constrained-covariance/root comparison after the precise sandwiched precision \(T=C(V)^*\Delta C(V)\) has been defined.

**Source-text facts:** these are the text of the draft's hypotheses and candidate theorems. **Not source fact:** that our actual independent \(N\) versus \(N+1\) Wilson/RG histories satisfy them.

## 3. Verified elementary nonimplication: physical scale does not define the pair

For \(L>1\),
\[
\eta_{N+1,j+1}=L^{j+1}L^{-(N+1)}
=L^{j}L^{-N}=\eta_{N,j}.
\]
This proves equality of spacings **only**. It imposes no constraints relating the domain sequences or the values of the prescribed coarse data on shared layers.

In particular, conditions of the form \(|(\partial V)(p')-1|<\varepsilon\) and \(|(\partial V')(p')-1|<\varepsilon\) for two *separately admissible* near-identity configurations do **not** imply \(V'=V\). A counterexample is obtained by taking \(V\) flat/identity and \(V'\) sufficiently close to identity but with a small nontrivial plaquette holonomy in a compact Lie group with a nontrivial one-parameter subgroup. Their curvatures can both obey any prescribed positive smallness ceiling, but their gauge-invariant plaquette holonomies differ. A lattice with suitable shared layers and a nontrivial plaquette can realize this local diagnostic. The example is an **abstract counterexample to the inference**, not a construction of two valid complete Bałaban RG histories, and not a disproof that a coupling can arrange a pair.

Hence
\[
\boxed{\text{physical-scale alignment + separate regularity}
\ \not\Rightarrow\ \text{paired determining data/domain history}.}
\]

The **first native transfer gate** is a *pair admissibility / selection / coupling theorem*: explicitly show that the actual cutoff comparison is restricted to, decomposes into, or can be coupled with pairs having \(\Omega'_{j+1}=\Omega_j,\ V'|_{\Lambda'_{j+1}}=V|_{\Lambda_j}\) (or furnish a theorem controlling deviations). The prior R70/R75 scale equation does not establish this.

**Important qualification:** one is free to *define* or condition two variational problems with shared \(V\). This gives eligible deterministic inputs, but does not show that arbitrary histories produced by independently cutoff-dependent measures are such inputs, nor that the restricted comparison covers the full physical observable law.

## 4. New mandatory distinction: deterministic carrier versus law of the RG theory

Let \(\mathcal X_N\) denote the finite-cutoff configuration space, \(P_N:\mathcal X_{N+1}\to\mathcal X_N\) a gauge-compatible coarse-graining map if defined, and \(\mu_N,\mu_{N+1}\) the relevant *normalized* finite-cutoff probability laws. Even if paired configurations exist for every value of the shared data and the minimizers enjoy the proposed stationarity, no conclusion of the form
\[
(P_N)_*\mu_{N+1}=\mu_N
\]
follows without a **separate measure/renormalized-density identity** (and the equality is generally *not* expected for two independently chosen bare actions; a controlled defect would suffice).

For example, on the same carrier \(\mathbb R\), take \(P(x)=x\), \(\mu_N=\mathcal N(0,1)\) and \(\mu_{N+1}=\mathcal N(0,2)\). The carrier map is the identity and every point is trivially paired with itself, but the pushforward laws differ. This refutes automatic promotion of **deterministic geometric pairing** to **equality of probability laws**. This is *not* a claim about the Yang–Mills distribution.

A plausible physical-observable comparison needs a well-typed estimate, for a named gauge-invariant local observable \(F\) and an admissible bounded test class \(\mathscr F\),
\[
\left|
\int_{\mathcal X_{N+1}} F\!\circ P_N\,d\mu_{N+1}
-\int_{\mathcal X_N}F\,d\mu_N
\right|\le\varepsilon_N(F),
\]
with suitable uniformity/summability, and **explicit normalization**. If \(P_N\) cannot be defined globally because geometry or gauge slices differ, an admissible observable-level cospan or joint coupling can replace it, provided the marginals and common observables are named. A projective equality \((P_N)_*\mu_{N+1}=\mu_N\) is *not required* when a summable defect estimate yields Cauchy observables.

Two **different** transport gates therefore remain:
1. **Geometric/fiber gate:** match \(G,\Lambda,\boldsymbol\Omega,\Lambda_j,V,V',U_{\mathfrak B},U_{\mathfrak B'},M\), gauge charts, and covariance operators on prescribed comparable fibers.
2. **Probability/RG law gate:** compare the actual integrated, normalized measures and their observable evaluations across small- and large-field sectors, inherited terms, Jacobians/determinants and source normalizations.

The conditional draft's covariance/root theorem on the unit lattice is an important lead for the first gate; it is **not** the second gate.

## 5. Exact additional upstream dependency

The external draft's covariance theorem III:36675–36807 assumes the minimizer theorem and analytic jet/kernel calculus on **common** source domains. It works on the entire torus, or on bonds strictly inside \(\Lambda_k\) beyond a distance \(RM\) from its complement. It is not a global bound on every large-field collar and shell.

The draft itself admits:
- III:35621–35623 quotes a Bałaban derivative claim with the author's remark **"We do not perform these calculations here"**. That source derivative should not be described as independently verified.
- III:37398–37427 explicitly leaves the *fine-lattice unsandwiched propagator stationarity* proof outstanding; the manuscript explains why sandwiched minimizer jets do **not** automatically provide random-walk fine junction estimates.
- III:37533–37560 explicitly leaves the transfer of the two-cutoff response to the **exact paired shells** of its uniqueness argument unproved; common analytic radius and point identification are missing.
- Chapter 13 III:111209–111222 and III:111258–111275 lists constrained minimizer locality, a kernel-difference estimate, a history modulus majorant, exact shells, and **differences of nested Gaussian integrals across moving large-field regions** as proof outstanding.

Thus even if the deterministic paired input type were met, the proposed broad existence proof's full two-run law comparison would not be automatically established. This *strengthens* the RH-style evidence-boundary criterion.

## 6. Refute-first gate table

| Claim or transport | Determination | Reason |
|---|---|---|
| \(\eta_{N,j}=\eta_{N+1,j+1}\) | **EXACT ALGEBRA** | R70/R75 lattice-scale identity |
| Independently admissible data imply \(V'=V\), \(\Omega'_{j+1}=\Omega_j\) | **REFUTED AS A GENERAL INFERENCE** | Curvature regularity and spacing do not link independent data |
| Existence of *chosen* paired variational problems | **DEFINITIONAL / SOURCE DRAFT INPUT** | External III:34655–34735 specifies them conditionally |
| Native actual full RG histories instantiate chosen pairs | **OPEN** | No native selection/coupling law, admissible collar/shear, or data equality proved |
| Paired background minimizer relative chart | **CANDIDATE EXTERNAL THEOREM, UNVERIFIED** | External III:35626–35641, upstream source claims not independently checked |
| Sandwiched covariance/root response | **CANDIDATE EXTERNAL THEOREM, UNVERIFIED** | External III:36675–36807; common unit-lattice, interior/whole torus and coercivity assumptions |
| Full Gaussian measure/observable-law comparison | **OPEN** | Pointwise pairing does not imply pushforward-law comparison; large-field/inherited normalization remain |
| Fine unsandwiched random-walk junctions and exact paired shells | **EXTERNAL PROOF OUTSTANDING** | III:37398–37427 and III:37533–37560 |
| Beta full extraction, Eq. (0.29) positive-alpha, continuum/OS/mass gap | **OPEN** | Local covariance source claims insufficient |

## 7. Result and next unconsumed cursor

**YM-R105 completed its refute-first *source-applicability* task by identifying a precise missing input theorem and a valid logical counterexample**: the exact paired determining-set conditions are not consequences of the already-proved native scale alignment plus separate regularity. It additionally establishes by elementary counterexample that even a deterministic carrier pairing is insufficient to compare normalized RG laws.

This is **not** a proof that a suitable pair/coupling cannot be constructed. It is not a claim of complete direct original CMP102b image verification. No covariance/root estimate, Gaussian history theorem, OS limit or mass-gap statement is reclassified as proved.

**YM-R106 — native pair realization / probability-law interface.** At one aligned physical-scale block, explicitly define the admissible coarse-graining \(P_N\) or observable-level cospan with actual Bałaban \(M^j,\Omega_j,V_j\), and test a real small-field conditioned fiber pair *including* the shared-layer equality. Require either an actual joint law with correct marginals, or a normalized observable discrepancy bound; specify how large-field/complement events are charged. After that, verify the upstream assumptions of the external minimizer/covariance/root theorem (including original CMP102b image and CMP109 conventions). Do **not** turn a conditional pairing into an arbitrary-history statement.

**Highest historical numbered Bałaban reference remains [92].** Existing external citations are pinned by SHA, not inserted as an invented new numbered primary reference.
