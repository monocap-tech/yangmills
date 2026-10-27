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

## 4. External YM4 / Armstrong crosswalk — direct candidate and type check

### Read the **existing direct primary-source audit** before the secondary locator

A preceding repository workstream **already conducted an equation/line-level direct TeX source inspection**, by fetching the enormous YM4 account as GitHub blobs after high-line range reads returned empty. That work is preserved in:
- [YM-EXT-01 direct YM4-to-native crosswalk](YM_EXT_01_EXTERNAL_YM4_NATIVE_CROSSWALK_20261026.md) and
- [its pinned primary-source receipt](YM_EXT_01_SOURCE_RECEIPT_20261026.md).

The direct audit used Sussman–Alpöge repository commit \`af96f9c5ec6d05a5c8f251256d87970d73b7f25a\`; the three raw TeX blobs are recorded there: Part I \`31898fb205c2990b59b7574915e82b22e08450b4\`, Part II \`f1e0aa132d23ed7f6d44f504a78ad57bd4ce38b8\`, and Part III \`6012ff578fb1c67c29651f1f4192ab59a4c862a3\`. It reviewed *selected* passages directly—not 424,000 lines end to end—and explicitly identified candidate results and acknowledged proof holes. This carrier-specification addendum is **not** a competing attempt to redo its mathematical status determinations.

[Armstrong's \`YMACCOUNT.md\`](https://github.com/scottnarmstrong/balaban-lean/blob/493e9eb97292ebf6070c1c217a09bcf1adc23857/notes/phase1/YMACCOUNT.md), text blob \`50f1bc6522679a950a39af7b184cb0b8f856010a\`, was also directly read. **Armstrong's content is secondary** and compares an O(N) formalization with an earlier YM4 snapshot (\`e392ef4\`). It is useful for finding *adjacent type failures*, but does not override the newer direct source audit.

### Critical finding: a candidate **carrier construction** exists in the external draft

The raw YM4 Part III does **not** merely invoke a small perturbation of arbitrary cutoff histories. According to the existing direct source receipt:

1. **III:34660–34734:** specifies **paired determining-set variational problems** with aligned domains \(\Omega'_{j+1}=\Omega_j\), shared-layer data \(V'=V\), a finer lattice \(\eta'=\eta/L\), a curvature bound and geometric floors. This is a proposed **source carrier pair**, conditional on actual histories satisfying that pairing.
2. **III:35626–35641:** its **candidate minimizer index-stationarity theorem** claims a gauge transformation \(\mathsf u\) and relative field \(A\) with
   \[
   W^{\mathsf u}=e^{i\eta A}U_{\mathfrak B},\qquad
   \|A\|_\theta\le C_A\varepsilon\eta^\theta.
   \]
   This is precisely the *kind* of source-to-target transporter missing in native R104. Its proof and dependencies have **not been independently certified**.
3. **III:36675–36807:** its proposed **stationarity of fluctuation covariance** bounds differences of \(C^{(k)},(C^{(k)})^{1/2},\Delta^{(k)},\Gamma_k\) at rate \(CL^{-\theta k/8}\) under the paired hypotheses, via the sandwiched precision \(T_k=C(V^{(k)})^*\Delta^{(k)}C(V^{(k)})\) and inverse/square-root resolvent calculus. This is **much stronger in intended scope** than native R104's fixed-background propagator analytic bound. It remains an external **conditional candidate**, not an adopted theorem.
4. **III:36809–36935:** the proposed one-loop coefficient comparison \(|\beta^0_{l+1}-\beta^0_l|\le CL^{-\theta l/8}\) includes log-determinant/Jacobian terms, but \(\beta_l^0\) is **not** automatically our entire beta history or the CMP109 Eq. (0.29) residual.
5. **III:37365–37482 and 37533–37633:** the same draft **explicitly leaves unsandwiched fine-propagator stationarity and exact paired-shell transfer unproved**; a proposed sandwiched-logdet localization **bypass** is not a completed proof.
6. **III:32417ff, 34033ff and Chapter 13:** history-wise modulus majorants, full forgetting, nested Gaussian integration across moving large-field regions and other prerequisites include explicit open dependencies.

These are source-located manuscript statements, **not independently verified theorems**. Crucially, the *actual* \((N,j)\) and \((N+1,j+1)\) histories of our project have **not yet been shown** to instantiate the draft's precisely paired variational input class. That is the native **untyped-carrier specification gap** in sharper form: **candidate source type located; target-membership and transport legality not established**.

### Refute-first transfer ledger

| Candidate interface | Exact source and evidence | RH-type verdict for native R105 |
|---|---|---|
| Native cutoff pair \(\to\) paired variational problems | Raw Part III:34660–34734 (direct-audit receipt) | **OPEN SOURCE→TARGET ADMISSIBILITY**; must match actual domains, gauge, shared-layer \(V\), curvature and norms |
| Paired minimizer \(\to\) relative \((3.37)\) background \(A\) | Raw Part III:35626–35641, CMP99(3) source R104 | **CONDITIONAL TRANSPORT**; prove native gauge/chart compatibility and independently audit minimizer dependencies |
| Relative \(A\) and shared \(C,\Delta\) \(\to\) normalized Gaussian covariance/root | Raw Part III:36675–36807 | **CANDIDATE CONDITIONAL**; require same free-variable carrier or valid pushforward, positivity, source norm, Jacobian and root semantics |
| Covariance/root \(\to\) one-loop beta | Raw Part III:36809–36935 | **CANDIDATE ONLY FOR ONE-LOOP**; check logdet/measure derivative and identify native one-step extraction separately from full marginal history |
| Covariance root \(\to\) unsandwiched fine random-walk junctions | Raw Part III:37365–37482 | **EXPLICIT GAP**; proposed alternative sandwiched-localization path remains unverified |
| Exact paired shells and source radii for two-cutoff response | Raw Part III:37533–37633 | **EXPLICIT GAP**; transport must commute with shell selection/rebasing and correctly handle shrinking radii |
| Inherited \(E\), large-field collars and nested integrations | Raw I:61295–61350, III:32417ff, III:111269–111275; Armstrong blockers 2/3 | **OPEN / PROOF OUTSTANDING**; no unconditional history-age response |
| Free complex current \(J\) avoids switching currents | Armstrong YMACCOUNT blocker 2 / raw I:45236–45314 | **POSSIBLE BYPASS OF CURRENT SWITCHING ONLY**; \(J\) is not background \(U\) or fluctuation \(B\); the same account notes a radius-inclusion gap |
| Intrinsic nonwrapping observable/torus terms | Raw I:58187–58340 and II:89995–90034 | **CONDITIONAL ALTERNATIVE OBSERVABLE CARRIER**; proof inputs and scalar/termwise-covariance transfer remain open |
| RP/rotation-invariance route | Sussman–Alpöge project README / RP subproject | **DIFFERENT JURISDICTION**; does not instantiate the UV transport |

**Verdict:** The old statement “no candidate common carrier has been found anywhere” is now **incorrect**: the external draft supplies a specific proposed paired carrier, relative gauge chart and sandwiched covariance/root response. The correct negative conclusion is that **no verified morphism from our actual native cutoff pair into that external source type has been established**, nor has the proposed complete native history/normalization transfer been independently proved. The earlier direct [YM-EXT-01 audit](YM_EXT_01_EXTERNAL_YM4_NATIVE_CROSSWALK_20261026.md) already records the candidate; this addendum **retypes** the proof interface without promoting theorem status.

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

1. **Native YM-R105 stays UNCONSUMED.** Its first task is **carrier passport instantiation**: compare the actual R104/R105 Bałaban cutoff histories with external Part III:34660–34734 determining-set input type, including \(G,\Lambda,\Omega\), gauge-fixed \(V,V'\), curvature, source averaging, chart and Gaussian normalized free variables.
2. If the actual histories satisfy the pairing, independently test the claimed relative-minimizer stationarity III:35626–35641, then the root/covariance estimate III:36675–36807 with its *entire upstream dependency chain*. If the pair does not fit, record the precise type mismatch instead of inventing a map.
3. **YM-EXT-02 (proposed independent validation):** specialize the existing direct external crosswalk to a proof-obligation-by-proof-obligation check of the paired-minimizer and covariance-root statements, explicitly addressing the manuscript's named unproved hypotheses, original Bałaban source-image gaps, and any legitimate sandwiched-localization bypass.
4. Preserve the separate inherited \(E\), full \(\beta\), positive-\(\alpha\) Eq. (0.29), large-field Gaussian integration, OS existence and physical mass-gap obligations.
5. No external theorem is adopted. No native cursor or status changes. Highest numbered Bałaban reference remains [92]; external repositories are version-pinned in the existing [source receipt](YM_EXT_01_SOURCE_RECEIPT_20261026.md).

**New outcome:** The transfer problem is no longer “find an arbitrary background stability lemma.” It is **“prove our actual cutoff histories inhabit the proposed paired variational/Gaussian carrier type, or exhibit why they do not.”** The RH legality protocol makes that gap auditable, and the external draft provides a sharply defined candidate rather than a substitute proof.

