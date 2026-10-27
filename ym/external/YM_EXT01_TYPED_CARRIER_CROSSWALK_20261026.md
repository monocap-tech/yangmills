# YM-EXT-01 — Typed carrier specification / external YM4 transfer audit

**Date:** 2026-10-26 (PDT). **Track:** external reconciliation, separate from native Yang–Mills passes.  
**Native invariant:** YM-R104 completed; **YM-R105 unconsumed**. Native checkpoint: [YM_HEAD_R104](../ym/checkpoints/YM_HEAD_R104_20261026.json).  
**Verdict:** **A TYPE/SPECIFICATION GAP IS CONFIRMED IN OUR PRESENT TWO-CUTOFF PROOF INTERFACE.** The existence or impossibility of a legitimate interface in Bałaban's construction remains undecided. This does **not** assert an error in Bałaban, prove Yang–Mills existence, or validate any external draft.

## 0. Import the RH/Weil method, not an RH theorem

The transferable RH/Weil discipline is **typed source→target transfer custody**: name the actual source object and native metric, separately state target object and its admissibility, specify the proposed transport/realization morphism, require a commutation/preservation proof for the consuming operation, and record the residual and refusal if any condition is unproved. An abstract positive or analytic statement is not transported merely because its symbols look similar. Distinguish an *intrinsic* target comparison from a coordinate-level auxiliary comparison.

This document imports that **proof-management method**, not RH zero arguments, positivity conclusions, or numerical certificates into Yang–Mills.

## 1. The object missing from our current interface

R103–R104 use conditional expressions such as

\[
K(\Omega_1,U_1)-K(\Omega_0,U_0)
=[K(\Omega_1,U_1)-K(\Omega_0,U_1)]
+[K(\Omega_0,U_1)-K(\Omega_0,U_0)]
\]

**only on a common typed carrier with the middle operator defined**. Native R104 establishes source-text *fixed-domain* relative-background analyticity of a particular family in the CMP99(3) (3.37) chart; it does not instantiate a common carrier for canonical \((N,j)\) and \((N+1,j+1)\).

A prospective **carrier passport** (all slots must refer to actual source objects, not just schematic symbols) is:

\[
\mathfrak C_{N,j}
=(G,\Lambda_{N,j},\Omega_{N,j},
 \mathcal U_{N,j}^{\rm adm},\mathcal G_{N,j},
 \mathcal H_{N,j},Q_{N,j},C_{N,j},
 \Delta_{N,j},\gamma_{N,j},
 \sigma_{N,j},\mathcal E_{N,j},\mathcal O_{N,j},
 \|\cdot\|_{N,j},\nu_{N,j}).
\]

Typed slot meanings and evidence required:

| Slot | Required native declaration | Current YM-R104 state |
|---|---|---|
| \(G,\Lambda,\Omega\) | Group, finite lattice/volume, blocking scale, source admissible domain sequence, physical lattice units | Group-family / exact paired indexing not fully instantiated |
| \(\mathcal U^{adm},\mathcal G\) | Background regularity (CMP99(3) (3.35)–(3.38)), gauge actions and a **joint** relative complex chart | Single-history source corridor known; paired admissibility **OPEN** |
| \(\mathcal H,Q,C\) | Actual fluctuation space, block averaging, gauge constraints, parametrization \(B=C\bar B\), adjoints and boundary conditions | Each source construction exists in a paper; **two-history map OPEN** |
| \(\Delta,\gamma\) | Positive precision on free variables and **normalized** Gaussian measure, covariance with its support; determinant/Jacobian conventions | One-trajectory source coercivity/decay; **cross-history Gaussian match OPEN** |
| \(\sigma,\mathcal E,\mathcal O\) | Weakening domains, nonlinear maps, inherited source \(E\), localized activities, marginal versus irrelevant output | CMP116 one-apparatus bounds; moving comparison **OPEN** |
| \(\|\cdot\|,\nu\) | Shared weighted norm, root/volume factors, coupling and physical-unit normalization, UV/history-age clock | **OPEN** |

The parenthetical expression \(\Sigma=C(C^*\Delta C)^{-1}C^*\) is meaningful **only when the exact constrained parametrization, adjoint, positivity, domain and inverse are defined**. It is not a proven pair comparison; CMP99(3) source formulas (3.156)–(3.158) are a single-construction witness.

## 2. Transport contract

Define two actual carrier passports, then provide transport/coupling data, **not a bare assertion of equality**:

\[
\mathfrak T_{N,j}
=(T^{\Lambda},T^{U},T^{B},T^{\gamma},T^{E},T^{O}),
\]

where each component has specified domain/codomain, chart requirements, norm bound, compatibility with gauge-invariant observables, and any Jacobian or normalization correction. \(T^{\gamma}\) could be an explicitly justified **pushforward or coupling of measures**, not necessarily an invertible linear isomorphism between different-dimensional fluctuation spaces. A single map need not exist; a cospan through a common physical observable carrier may be the correct architecture.

**Required commuting-interface test:** Compare RG-evolve-then-transport with transport-then-RG-evolve on a named class of observables, defining a defect only after both composites exist:

\[
D_{N,j}(F)=
\big(\mathcal T_{j+1}\circ\mathcal R_{N+1,j}\big)(F)
-
\big(\mathcal R_{N,j}\circ\mathcal T_j\big)(F).
\]

The indicated arrow directions and index conventions are a **template**. They must be specialized with actual domain/codomain types; without that, \(D_{N,j}(F)\) itself is **untyped**. If observable pullbacks reverse arrows, rewrite the square contravariantly. The physical task is to prove the two paths agree exactly or differ in a norm with summable cutoff/volume error. Gauge covariance (CMP99(3) (3.33)–(3.34)) alone concerns *one lattice's gauge changes*, not this cutoff square.

For a fixed-domain resolvent comparison, separately certify all of:
1. An admissible intermediate \(K(\Omega_0,U_1)\), with two domain sequences accepted at the **same** \(U_1\).
2. Actual relative \(U_1=\exp(i\eta A)U_0\) in the same chart with the correct scale-dependent \((3.37)\) norms.
3. Positive/invertible propagator operators and \(V(A)\) in a shared norm permitting \(G_1-G_0=G_0V(A)G_1\).
4. Control of the cutoff-dependent gauge and **Gaussian** carrier and normalization defects.
5. A summable *history-age* or cutoff response; the source relative amplitude \(\alpha_1\) is **not** itself such a factor.
6. Transfer through CMP116's weakened minimizers, connected logarithmic/Mayer sums, and beta/rest extraction **only after** 1–5.

This is a dependency order; it is not an assertion that a single pairwise background chart is unavoidable for *every* constructive route. A different theory might **bypass** that comparison while establishing physical-observable consistency by another theorem.

## 3. Minimal negative controls

**Ill-typed subtraction:** Let \(\mathcal H_0=\mathbb R\), \(\mathcal H_1=\mathbb R^2\). Each can carry an identity inverse and a normalized Gaussian with nondegenerate covariance. The expression \(G_1-G_0\) has **no canonical meaning** before declaring a transporter or comparison observable. Picking \(T_1(x,y)=x\) or \(T_2(x,y)=x+y\) pushes standard independent Gaussians to variances 1 and 2, respectively. Both are legitimate linear maps, but they give different *claimed* covariance comparisons. A comparison is therefore **transport-dependent** unless source geometry fixes the map.

**Common-space analytic inequality without history control:** Suppose the fixed-domain source resolvent gives \(\|G_1-G_0\|\lesssim \alpha_1\) for an admissible \(\alpha_1>0\) independent of \(N\). This does not imply \(\sum_N\|G_1-G_0\|<\infty\). The missing summable cutoff response is a separate theorem.

**Gaussian support:** A coordinate-level injection of a lower-dimensional Gaussian into a larger space produces a measure supported on a lower-dimensional subspace. An arbitrary density-ratio/log-partition comparison with a full-dimensional Gaussian is unavailable without a common reference measure or an appropriate coupling/integration/disintegration. Never infer such a ratio from positivity of separate precision matrices.

These are abstract diagnostic counterexamples, **not** assertions that Bałaban's canonical construction exhibits the pathology.

## 4. External YM4 / Armstrong crosswalk — evidence levels

### External source versions actually examined

- [Sussman–Alpöge YM4 experiment repository](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/af96f9c5ec6d05a5c8f251256d87970d73b7f25a), snapshot commit \`af96f9c5ec6d05a5c8f251256d87970d73b7f25a\`: **README read directly**. It says draft mathematical output remains tentative and largely LLM-authored, and that its YM4 existence account is very long and difficult to understand. It makes no independent theorem verification claim.
- [Armstrong \`YMACCOUNT.md\`](https://github.com/scottnarmstrong/balaban-lean/blob/493e9eb97292ebf6070c1c217a09bcf1adc23857/notes/phase1/YMACCOUNT.md), text blob \`50f1bc6522679a950a39af7b184cb0b8f856010a\`, **read directly**. This is a **secondary comparison of an O(N) formalization with a YM4 draft**, based on Sussman–Alpöge commit \`e392ef4\`. It is not the direct YM4 theorem proof.
- Direct range reads of huge \`theorem_0_complete_account_raw_{I,II,III}.tex\` in the Sussman–Alpöge repository were attempted through the GitHub connector but returned empty content for requested high line ranges. **Those manuscript passages have NOT been directly audited here**. Their line references remain *locators provided by Armstrong*, not independently confirmed quotations.
- Native papers: [R104 source receipt](../ym/source_receipts/YM_R104_CMP99_BACKGROUND_RESPONSE_RECEIPT_20261026.md), third-party primary-paper text witnesses, not original image verification.

### Refute-first interface ledger

| Candidate external interface | Reported evidence | Native YM-R104/R105 verdict | Why |
|---|---|---|---|
| Free complex **current** throughout, no current switching | Armstrong YMACCOUNT blocker 2, YM4 candidate I:45237–45330 | **POSSIBLE BYPASS / UNVERIFIED** | Avoiding a switching operation may remove one source of mismatched current coordinates, **but does not certify common UV backgrounds, gauge Gaussian carriers, or OS observable limits**. Current \(J\) is not automatically background \(U\) or fluctuation \(B\). |
| Larger current-radius domain not contained in earlier analytic domain | Armstrong blocker 2, candidate I:135200–135235 and I:135723–135800 | **SAME TYPE OF DOMAIN-ADMISSIBILITY ISSUE / NOT DISCHARGED** | Two statements on nonnested complex domains do not grant a common analytic transfer. This is not proof that the native \((3.37)\) chart fails, merely a directly relevant failure mode. |
| Collar alignment for background tests | Armstrong blocker 2, CMP99b (3.35), (3.37), CMP109 p.277, YM4 item C13 | **OPEN SOURCE HYPOTHESIS / HIGH PRIORITY** | The test family must cover the complete read set of the propagator/background; Armstrong reports the collar-alignment point unproved and says the large-field sources are silent on never-averaged collar bonds. Direct page verification outstanding. |
| Inherited boundary terms crossing retained holes | Armstrong blocker 3, candidate I:61143–61178, I:61325, CMP119/CMP122b | **POSSIBLE DISTINCT HISTORY-LOCALITY OBSTRUCTION / UNVERIFIED** | Creation-time decay does not supply inherited-history relative decay. An advertised retained-pocket/label mechanism is marked proof outstanding by Armstrong. Must not be transferred to our \(E\)-root norm without proving the precise object relation. |
| Cluster gas built on *cores* excluding retained holes | Armstrong blocker 4, candidate I:20632–20925, CMP122b | **POTENTIAL ALTERNATIVE ARCHITECTURE / NOT THE SAME GATE** | Core-incidence changes what geometric object the cluster combinatorics charges. Requires native model and preserved observable/measure identity before import. Not a fixed-domain relative background bound. |
| Footprint-localized terms independent of torus when nonwrapping | Armstrong blocker 7, candidate Theorem 4.38/I:58187 ff. | **POTENTIAL OBSERVABLE-LEVEL COMMON CARRIER / UNVERIFIED** | A genuinely intrinsic, footprint-defined local observable could bypass global gauge-carrier identification for some comparisons, **if** it respects the actual extraction and has required scalar/counterterm control. Armstrong says torus-extracted scalars are only approximately matched and that a proposed estimate remains unproved. |
| Reflection-positivity route to rotation invariance | Sussman–Alpöge README / RP subproject | **DIFFERENT JURISDICTION** | A later reconstruction/symmetry mechanism cannot retroactively define the uninstantiated two-cutoff RG carrier, nor prove history control. |

**Specific audit conclusion:** Among the examined sources, no directly audited external theorem establishes the missing \((N,j)\leftrightarrow(N+1,j+1)\) carrier, common CMP99(3) \((3.37)\) chart, constrained covariance/root transport, or summable cutoff history response. This is a statement **about the materials examined**, not a claim that the long YM4 account contains no such proof. In particular, YMACCOUNT's term "SAME GAP" applies in the first instance to its **O(N) blockers**, not automatically to our YM-R104 native obligation.

## 5. RH-style legality protocol for the next transfer

For any future candidate proposition, fill the following fields *before* a PASS decision:

\`\`\`
CLAIM-ID:
SOURCE: repository + immutable commit + exact equation/theorem/page
SOURCE-TYPE: spaces, gauge group, measures, norm, quantifiers, analytic chart
SOURCE-STATUS: theorem / draft claim / conditional / OCR witness / unproved
TARGET-TYPE: named YM-R104/R105 native object and definition
TRANSPORT: explicit map/coupling/pushforward and its admissibility proof
PRESERVATION: commuting diagram, gauge invariance, normalization, covariance
DEFECT: exact residual with a source-native bound or explicit "undefined"
UNIFORMITY: in UV depth, step, volume, fields, polynomial/cluster root counts
NEGATIVE CONTROL: counterexample to the nearest invalid shortcut
VERDICT: DISCHARGES / WEAKENS / BYPASSES / INAPPLICABLE / UNKNOWN
REMAINING GATES:
\`\`\`

Automatic refusal rules: a one-trajectory bound is not a cross-history bound; a fixed-lattice gauge covariance is not a cross-cutoff transport; a spatial mark is not history age; analytic source membership is not an intrinsic common chart; operator positivity is not Gaussian measure equivalence; a massive draft is not a verified theorem. A source can **bypass** an entire interface if the target physical observable construction is proved by another route; it is not legitimate to label the original gate "proved" in that event.

## 6. Decision / next exact work

1. **Native YM-R105 stays UNCONSUMED.** Its first task must now be **carrier passport instantiation** at one aligned physical-scale block, then proof or obstruction of admissible transport. Only after that demand the relative \(A_{N,j}\) response bound. Preserve the native R104 source receipt.
2. **YM-EXT-02 (proposed):** examine the external *primary YM4* passages around Armstrong's blockers 2, 3, and 7, with actual content access and commit-pinned citations. The discriminant is whether the source supplies a **legally typed alternative observable-level carrier** or simply shifts the missing operation to a free-current or collar-domain inclusion claim.
3. Resolve the original CMP99(3) and CMP109 publisher-image holds before promoting constants. No external lemma is adopted and no native status changes here.

This is a **completed first-pass negative/conditional crosswalk** with an explicit carrier specification protocol. It is not a complete verification of the Sussman–Alpöge draft or of Armstrong's findings, and it does not assert YM4 existence or mass gap.