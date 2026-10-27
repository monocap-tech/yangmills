# YM-R104 — CMP99(3) analytic background response / CMP116 two-history transfer audit

Date: 2026-10-26  
Repository: monocap-tech/yangmills  
Verified prior native head: YM-R103, checkpoint ym/checkpoints/YM_HEAD_R103_20261014.json (before this pass).  
Status: COMPLETE AS SOURCE-TEXT AUDIT AND EXACT SAME-DOMAIN PERTURBATION INTERFACE; **TWO-CUTOFF NATIVE RESPONSE OPEN**.  
Next cursor: **YM-R105** (unconsumed).  
Research classification: **UNPROVED RESEARCH PROGRAM**. No four-dimensional continuum Yang–Mills existence, OS reconstruction, or positive mass-gap claim.

## 0. Exact question and custody

R103 established a domain-sequence comparison from CMP99(3) Theorem 3.14 / Eq. (3.154) and elementary stability inequalities for CMP116 nonlinear fixed-point equations. It **did not** establish a same-domain *background* difference estimate. R104 asks whether the original papers contain a real source mechanism for the second bracket in

\[
K(\Omega_1,U_1)-K(\Omega_0,U_0)
 =[K(\Omega_1,U_1)-K(\Omega_0,U_1)]
 +[K(\Omega_0,U_1)-K(\Omega_0,U_0)]
\]

and, if so, whether it genuinely controls two different cutoff histories. This identity requires a common operator carrier **and the intermediate \(K(\Omega_0,U_1)\) to be defined/admissible**; a gauge or Gaussian carrier transport may introduce separate terms. See TARGET_SCOPE.md and REVIEW_ERRATA_20261026.md.

Sources re-read:
- T. Bałaban, "Propagators for Lattice Gauge Theories in a Background Field," *Communications in Mathematical Physics* **99(3)** (1985), 389–434, DOI 10.1007/BF01240355 (CMP99(3)); source paper title/DOI verified on Springer. The working **third-party transcription**, observed blob SHA **ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743**, is at https://github.com/chboishabba/dashi_agda/blob/master/Docs/support/reference/balaban-source-extracts/cmp99-background-propagators.txt.
- T. Bałaban, "Renormalization Group Approach to Lattice Gauge Field Theories. II. Cluster Expansions," *Communications in Mathematical Physics* **116** (1988), 1–22, DOI 10.1007/BF01239022 (CMP116); working third-party transcription blob SHA **2de28469578fcdc14270f57516b190234f9c8812** at https://github.com/chboishabba/dashi_agda/blob/master/Docs/support/reference/balaban-source-extracts/cmp116-effective-actions-part-ii.txt.

**Evidence boundary:** Original paper *transcriptions* hosted by a third party, not verified publisher page images. Equation signs, exact indices, constant exponents and OCR-damaged formulas MUST be checked against original images before formal use. No new bibliography number is created; highest cumulative reference remains [92]. Source receipt: ym/source_receipts/YM_R104_CMP99_BACKGROUND_RESPONSE_RECEIPT_20261026.md.

## 1. Source-positive result: CMP99(3) has an actual analytic background field perturbation corridor

CMP99(3) §A first defines a **domain-dependent** class of regular configurations \(U\): local gauge choices and estimates (3.35), (3.36) on the appropriate scale-indexed cubes, plus no regularity conditions outside the domain \(\Omega_0\). The **relative complex perturbation** is written \(U'U\), \(U'=\exp(i\eta A)\), with scale-dependent size and covariant derivative conditions in (3.37), and a stronger derivative condition (3.38) for some applications (transcription lines 353–385; printed pp.396–397). The compact phrase "both configurations are individually regular" does **not** imply they lie in one common relative chart.

CMP99(3) §B expressly studies analytic dependence on this relative complex field. **Theorem 3.4** (OCR lines 522–545, printed p.400) says its propagator/projection operators admit analytic continuation on the \((3.37)\) domain and retain the indicated Theorems 3.1–3.3 bounds. This is a genuine **source-text witness of single-domain background analyticity**, stronger than treating every propagator as a function of an entirely unspecified background.

Notable source mechanisms:
- The covariant Laplace and averaging changes are expanded in powers of the relative \(A\); (3.53), (3.59) and (3.60) lead to an operator perturbation \(V'(A)\). Its kernel/norm bounds are given in (3.61)–(3.63).
- On the *fixed source carrier/domain*, (3.64) is a convergent Neumann expansion for \(G'(U'U)\); (3.65) gives the **exact relative-background resolvent identities**
  \[
  G'(U'U)-G'(U)=G'(U)V'(A)G'(U'U)
              =G'(U'U)V'(A)G'(U).
  \]
  The text following (3.65) states that the remainder satisfies the earlier propagator-type estimates with an additional **\(O(1)\alpha_1\)** small factor (OCR lines 662–691). This is *not* a cutoff-depth gain: \(\alpha_1\) controls admissible relative perturbation size.
- For the main gauge-field propagator, (3.82)–(3.86) similarly gives \(\Delta_a(U'U)=\Delta_a(U)-V(A)\) and
  \[
  G(U'U)=G(U)(I-V(A)G(U))^{-1}
  \]
  as an operator-norm convergent series when the perturbation is small, with the source's propagated regularity/decay bounds. By the algebraic resolvent identity, whenever these operators are defined on the same carrier,
  \[
  G(U'U)-G(U)=G(U)V(A)G(U'U).
  \]
- (3.33)–(3.34), OCR lines 340–352, record **gauge covariance of these operators under a gauge transformation of a fixed lattice configuration**. Gauge covariance does not itself construct a common physical-scale map between different UV cutoffs.

**Determination 1:** "There is no background-response mechanism in CMP99(3)" would be false. A *fixed-domain, relative-background, small-perturbation* response mechanism exists in the source text. The response is analytic and the listed resolvent remainders gain the **relative field-size** parameter, not a proved history-age parameter.

## 2. The exact strength and limits of the perturbation estimate

The perturbation bound is tied to the explicit complex neighbourhood \((3.37)\). A parameter \(\alpha_1\) there measures weighted relative \(A\) and its covariant derivatives at the relevant lattice scales. The source's \(O(\alpha_1)\) remainder in (3.65), and its smallness reasoning in (3.85)–(3.86), do **not** assert that independently produced cutoff backgrounds \(U_{N,j}\) and \(U_{N+1,j+1}\) obey such a relation.

To use this source mechanism for a canonical cutoff comparison, at minimum one must produce an actual physical-scale chart map \(\mathcal T\) and a relative field \(A_{N,j}\) such that, schematically,
\[
 \mathcal T U_{N+1,j+1}
 = \exp(i\eta_j A_{N,j})\,U_{N,j},
\]
**in the same admissible domain and gauge chart**, with the (3.37) componentwise bounds and an explicit sufficiently small \(\alpha_{1,N,j}\). This is a **conditional target**, not an asserted identity: domain geometry, link variables, gauge choices and blocking may invalidate the proposed form. For a Cauchy comparison we would further need a **summable** control on the normalized resulting difference, with all volume/root factors accounted for.

The source's guarantee that each operator admits analytic extension and has a one-trajectory bound is not, by itself, a two-input Lipschitz or a history-age response. A Cauchy argument on a common complex chart could control a difference if a uniform analytic radius, bounded corridor, and endpoint separation are already provided; no such *canonical paired-history corridor* has been recovered. Nor should the source's \(O(\alpha_1)\) be silently converted to a claimed \(O(L^{-cN})\).

**Determination 2:** fixed-domain relative response = **SOURCE-TEXT SUPPORTED**; actual two-cutoff background map, relative amplitude and summability = **OPEN NATIVE**. This is a meaningful narrowing of the R103 source question, **not closure of the background/coupling-dependent history-response gate**.

## 3. Domain versus background motion: a 3-condition source interface

Even after achieving a common operator carrier, the R103 telescope requires the following separate facts:

1. Both \(\Omega_0,\Omega_1\) must satisfy CMP99(3) Theorem 3.14 domain-sequence hypotheses **for the same \(U_1\)**, and the intermediate \(K(\Omega_0,U_1)\) must be admissible.
2. At fixed \(\Omega_0\), \(U_0,U_1\) must lie in a shared (3.35)/(3.37) regular relative chart with sufficiently small perturbation parameter. Only then is the §B analytic/resolvent machinery eligible.
3. A map matching the different cutoff-dependent gauge constraints, Gaussian carriers, and normalization data must be furnished. The equality of scale \(a_{N,j}=a_{N+1,j+1}\) from R70–R75 does **not** establish this map.

**If (1) fails**, a spatial-domain response theorem may be inapplicable. **If (2) fails**, the perturbation expansion at one reference \(U\) may be inapplicable. **If (3) fails**, the two compared operators need not act on the same space, even when both separately satisfy the paper's one-trajectory estimates.

These are *independently typed* obligations. Merely concatenating Thm. 3.14 and Thm. 3.4 does not prove a two-history theorem.

## 4. The constrained covariance is not automatically covered

CMP99(3) §3 around (3.156)–(3.158) introduces a linear parametrization \(B=C\bar B\) of constrained variables. The paper reports a positive lower bound for \(C^*\Delta_k C\) under source regularity and obtains an inverse covariance through this parametrization (third-party OCR lines 1905–1947). Theorem 3.15 around (3.185)–(3.187) supplies a one-trajectory random-walk expansion and exponential decay for the constrained covariance.

There is **no explicit, source-verified comparison** of two cutoff-dependent maps \(C_0,C_1\) or two normalized Gaussian measures in this material. The \(\alpha_1\)-dependent resolvent response for \(G\) **cannot be presumed unchanged** for covariance roots, constraints, determinants, or the full two-history Gaussian integral.

For a fixed identical \(C\) and two compatible positive precision operators, the inverse-resolvent algebra may be useful; this **conditional abstraction** is not a theorem that the actual constraint matrices coincide. The covariance-square-root step likewise remains typed but open.

**Determination 3:** fixed-domain source propagator analyticity **does not discharge** native constrained covariance/root/normalization carrier movement.

## 5. CMP116: analyticity and nonlinear minimizer control remain single-apparatus results

CMP116 (1.2)–(1.5) (OCR lines 75–105, printed pp.2–3) expresses the fast field through propagators \(H,H_0,G\) and nonlinear fixed points \(D,A_0\). The source says these fixed-point solutions can be considered functionals of operators obeying its regularity and bound assumptions.

CMP116's weakened operators \(H(s),G(s),H_0(s)\) are analytic in weakening parameters; under small-field conditions its fixed points are analytic in the declared variables and satisfy estimates (1.11)–(1.18) (OCR 205–290, printed pp.5–6). The source explicitly states that the considered functions/operators are analytic in \(U,J\) on domains satisfying conditions I.(i)–(iii), with uniform one-apparatus bounds (OCR 287–290). The localization sums require a **common analytic domain** when combined (OCR 318–349). Lemma 1 (1.33)–(1.36) gives localized terms analytic in the stated data and a **single-trajectory** activity bound (OCR 430–445).

**Positive transfer lead:** the source's use of common analytic domains and uniform fixed-point bounds makes a *conditional* endpoint-difference estimate plausible when both endpoint histories are mapped to one shared analytic polydisc with a uniform contraction margin and difference estimates for \(H,H_0,G\).

**What the source does NOT say in the checked passages:** a two-history source operator Lipschitz estimate with an RG-history-age factor; an explicit comparison between the endpoint source charts and \(D,A_0\) maps; a derivative bound in a common rooted *moving-apparatus* norm after weakening parameters, localization sums, Mayer steps, and marginal extraction.

R103's elementary fixed-point comparison with a common \(q<1\) is a **consumer of** such hypotheses, not their source. CMP116 analytic continuation must not be promoted to the required two-history estimate merely because its fixed points exist at each endpoint.

**Determination 4:** CMP116 has native analytic structure suitable for a future interface, but **does not by these source statements discharge** its moving-minimizer/history response obligation.

## 6. Negative-control checks

- **α1 is not history age.** Hold a nonzero relative perturbation inside a fixed admissible chart independent of UV depth \(N\): the corresponding analytic propagator difference need not decay as \(N\to\infty\). No \(L^{-cN}\) follows from the source's \(O(\alpha_1)\) alone.
- **Individual regularity is not a common chart.** Two histories may separately satisfy local gauge regularity in different charts. Their relative logarithm need not satisfy the same (3.37) domain; gauge covariance (3.33)–(3.34) does not guarantee a canonical transporter.
- **Common physical spacing is not a common carrier.** The fluctuation Gaussian dimension, constraint parametrization, normalization and localization domain may differ despite the same blocked spacing.
- **One-trajectory localization is not a derivative of localization.** Both CMP116 endpoints can satisfy the same absolute activity norm while their difference is uncontrolled absent an operator/measure comparison.

These are logical nonimplications, not counterexamples to a specific correctly stated Bałaban theorem.

## 7. Certified state and pass conclusion

**Source-text witness (positive):**
- CMP99(3) Theorem 3.4: complex analytic extension around a regular background in the (3.37) corridor.
- CMP99(3) (3.64)–(3.65) and (3.84)–(3.86): actual same-domain relative-perturbation Neumann/resolvent mechanism, source remainder gains a relative \(\alpha_1\)-size factor in the described norm regime.
- CMP99(3) (3.33)–(3.34): same-lattice gauge covariance.
- CMP116 (1.2)–(1.18), (1.23)–(1.25), (1.33)–(1.36): nonlinear-map/weakener analyticity, common-domain localization and single-apparatus estimates.

**Exact elementary derivation:**
- Resolvent difference \(G_1-G_0=G_0(\Delta_0-\Delta_1)G_1\) on a common invertible operator carrier, with both operators' admissibility required. This is already visibly instantiated in the source for its relative \(U'U\) construction.

**Open native gates (NOT closed):**
- Actual canonical two-cutoff gauge/constraint/Gaussian carrier and domain compatibility.
- Quantitative bound on the relative source field \(A_{N,j}\) in a common (3.37) chart, with history-age summability.
- Transferred marked estimate for constrained covariance and covariance root with normalization.
- Uniform CMP116 two-input minimizer/operator/localization response in a shared rooted norm.
- Inherited \(E\) relative estimate, vacuum polarization / marginal beta coherence, CMP109 Eq. (0.29) positive-\(\alpha\) residual, large-field continuum/OS theory and spectral mass gap.
- Original-image exact equation verification, including CMP99(3) (3.37), (3.65), (3.85)–(3.86) and CMP109 (0.29)/(5.37)/(5.42).

**New decision:** It is no longer necessary to search blindly for *any* same-domain background-resolvent response in CMP99(3). The **gating question is the actual cutoff-pair relative field and compatible current/gauge carrier in the precise analytic corridor**.

## 8. YM-R105 — next unconsumed cursor

**YM-R105 — Actual-cutoff relative-background chart and constrained-carrier test**

1. Recover the actual \(N\) and \(N+1\) background fields, averaging/gauge conventions and cutoffs from the native Bałaban source definitions, with exact scale and domain indexing.
2. At one *aligned* local test block, attempt to construct or obstruct a same-carrier transport and \(\mathcal T U_{N+1,j+1}=\exp(i\eta_j A_{N,j})U_{N,j}\), with explicit (3.37) weighted norm/control.
3. Determine whether the source provides any **relative amplitude** or history-age bound for this actual \(A_{N,j}\), rather than a generic analytic radius.
4. Identify whether the constrained Gaussian parametrization \(B=C\bar B\) transports compatibly; do not assume \(C_N=C_{N+1}\).
5. If impossible, state the exact missing source theorem or counterexample; if possible, **only then** attempt CMP116 common-polydisc/weighted-response transfer. Avoid generating more untyped abstract lemmas.
6. Keep the CMP99/CMP109 original-image holds explicit. No proof claim may advance from textual recognition alone.

Highest source reference stays [92]; next new bibliography item [93] remains unused. **YM-R105 is not consumed by this R104 source audit.**
