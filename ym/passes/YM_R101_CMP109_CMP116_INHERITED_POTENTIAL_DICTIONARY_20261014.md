# YM-R101 — CMP109 inherited-E to CMP116 Mayer potential source dictionary / two-history carrier audit

Date: 2026-10-14
Repository: monocap-tech/yangmills
Prior certified head: YM-R100, 9a8a03fb9ed2e0abe65d1225fc2298072d8828fb
Status: COMPLETE AS SOURCE-TEXT OBJECT-DICTIONARY AND MATHEMATICAL AUDIT; NATIVE CROSS-CUTOFF GATES OPEN
Next unconsumed cursor: YM-R102
Claim discipline: UNPROVED RESEARCH PROGRAM. No four-dimensional continuum Yang–Mills, OS construction or positive mass gap claimed.

## 0. Preflight, custody levels, and target

Preflight verified that repository main was YM-R100, with live cursor YM-R101. Existing source/technical controls R69–R75, R77–R93 and R97–R100 were preserved. New source reading was conducted on [21] T. Bałaban, *Renormalization Group Approach to Lattice Gauge Field Theories II. Cluster Expansions*, CMP 116 (1988), 1–22, DOI 10.1007/BF01239022, using the public third-party FULL PAPER OCR/transcription in chboishabba/dashi_agda:

  https://github.com/chboishabba/dashi_agda/blob/master/Docs/support/reference/balaban-source-extracts/cmp116-effective-actions-part-ii.txt
  observed Git blob 2de28469578fcdc14270f57516b190234f9c8812.

Cross-check source [7] CMP109 (1987) in the same repository:
  https://github.com/chboishabba/dashi_agda/blob/master/Docs/support/reference/balaban-source-extracts/cmp109-effective-actions-part-i.txt
  observed Git blob f1aec083a3a6470c67a2c1205ca740c2583fe37a.

These are readable third-party transcriptions of the PRIMARY AUTHORS' PAPERS, NOT original source PDF-image receipts. Prose and structural displayed equations can be identified with their original labels, but OCR-corrupted signs/norms/constants are NOT image-certified. R94–R100 original CMP109 Eq(0.29)/(5.37)/(5.42) IMAGE HOLD persists; CMP116 formula-image validation also remains to be performed before a load-bearing literal sign or exact norm is adopted. Reused bibliography [7], [21], [59], [85], [87], [90]–[92]; highest ID [92], next [93]. The new OCR receipt is an ADDITION to source custody under existing [21], not a new numbered mathematical source.

R100 obtained an exact endpoint identity for two REAL admissible histories under an explicitly common Gaussian and cutoff: Z1/Z0=<exp(U1-U0)>_rho0. R101's task is whether the U input has a source-native CMP116 potential meaning, and exactly what is and is not common across historical/cutoff comparisons.

## 1. Source-text recovery: THE SINGLE-TRAJECTORY DICTIONARY IS REAL

CMP109 printed p.268 around (2.12)–(2.13) states that the one-step normalized constrained Gaussian interaction is exp[P^(k)(g_k,U_(k+1),B)+{...}] with the curly part containing the inherited previous action E_k evaluated on transformed/background configurations. The same extraction describes B=g_k B' and the actual remaining Gaussian covariance (C* A^(k) C)^(-1) on independent constrained variables. The new effective term is a logarithm of that fluctuation integral.

CMP116 printed pp.9–10, Lemma 1 / (1.33) (OCR lines 430–445) explicitly gives a localized decomposition of the INHERITED E_k DIFFERENCE in the second expression of the CMP109 (2.13) fluctuation action:

  E_k(U_k(expi B' V^(k))) - E_k(U_k(V^(k)))
      = sum_(Y in D_k) V'_k(Y,U_(k+1),B).                [CMP116 (1.33), schematic normalization]

The lemma requires source regular-background and analytic fast-field domains (1.34)–(1.35), and gives absolute bounds (1.36). The source notation of the exact transformed configuration is OCR degraded; the role of the term as a difference of inherited E_k is NOT ambiguous.

CMP116 printed pp.11–12, Lemma 2 / (1.41) (OCR lines 511–529), then combines the CURRENT perturbative fluctuation term P^(k) and the inherited curly-bracket interaction as a single LOCALIZED source potential family:

  P^(k)(g_k,U_(k+1),B) + inherited curly bracket
      = sum_(Y in D_k) V_k(Y,U_(k+1),B).                  [CMP116 (1.41), schematic]

The lemma records a quadratic-plus-remainder form (1.42), gauge invariance and source analytic bounds. The source V_k(Y) is the potential INSIDE the fluctuation integral; it is NOT the marginal-subtracted final irrelevant effective-action activity V^(j) posited by the earlier CMP109 Eq(0.29) traceability manuscript [85]. This same-letter ambiguity is a load-bearing typing hazard.

CMP116 Sect. 2 begins its Mayer expansion from precisely this source potential family in (2.1) (OCR lines 534–550). The SOURCE characteristic cutoff chi_k is decomposed separately in (2.3) (lines 556–569), and the conditioned Gaussian/chart/second weakening then produce localized pre-exponent activity H(Z) in (2.9), a hard-core polymer gas in (2.11), and after exponentiation a connected-log expansion E^(k+1)(X) in (2.12)–(2.13) (lines 659–713). Lemma 3 / (2.38) supplies an UNMARKED bound on H(Z) under source parameter restrictions (OCR lines 995–1005).

This genuinely improves source custody relative to the R93 concern "is there a native potential object?": YES, for ONE canonical trajectory and under the explicit CMP116 source hypotheses. The chain is:

  CMP109 inherited E_k difference
   -> CMP116 Lemma 1 localized V'_k(Y)
   -> CMP116 Lemma 2 complete fluctuation potential V_k(Y)
   -> CMP116 (2.1) Mayer expansion with separate chi_k decomposition
   -> conditioned/weakening H(Z)
   -> connected-log E^(k+1)(X).

Classification: PRIMARY-ARTICLE OCR TEXT-WITNESS OF THE SOURCE CONSTRUCTION, not new Yang–Mills proof and not an ORIGINAL-IMAGE-LOCKED equation certification. It does NOT prove a TWO-HISTORY difference estimate.

## 2. Exact two-endpoint difference on a synchronized frozen current chart

Let two actual canonical histories i=0,1 reach an IDENTIFIED fixed current coupling g_k and common source background b, with common constrained fast coordinate Y, Gaussian, sharp cutoff, minimizer/field map Phi_b(Y), Phi_0, and deterministic current perturbative contribution P^(k)(g_k,b,Y). Define the inherited terms

  I_i(b,Y) = E_(k,i)(Phi_b(Y)) - E_(k,i)(Phi_0).

Then the two complete unlocalized interaction potentials are

  U_i(b,Y) = P^(k)(g_k,b,Y) + I_i(b,Y).

By subtraction, EXACTLY

  D := U_1-U_0
     = Delta E_k(Phi_b(Y)) - Delta E_k(Phi_0),          (R101.1)
  Delta E_k := E_(k,1)-E_(k,0).

This elementary identity is independent of independent "past coupling coordinates" and of a hypothetical history interpolation. If P, Phi, Gaussian, chi or coupling are NOT the same, their differences must be added as distinct current-step geometry, marginal and measure channels. In particular the two cutoff-depth canonical trajectories have NOT been shown to obey the synchronization assumptions (R64–R75, R97–R100).

Assume both potentials receive COMPATIBLY INDEXED localized source decompositions on the same complete D_k family:

  U_i = sum_(Y in D_k) V_(k,i)(Y,b,Yfast).

Then subtraction gives the exact formal identity
  D = sum_Y [V_(k,1)(Y)-V_(k,0)(Y)]                 (R101.2)
whenever the sums converge in the same declared norm. The source's single-trajectory localization result guarantees such a decomposition INDIVIDUALLY, not the synchronized operators, common admissible complex domains, and relative norm that would make R101.2 a native cross-cutoff theorem. Moreover, a localization construction that depends nonlinearly on E_(k,i) can invalidate an assertion that delta V_Y equals "apply one fixed linear localization map to delta E"; no such map is assumed here.

If the source localization maps are shown to be identical AND linear in the inherited input at fixed g/background, then
  Delta V'_k(Y) = L_(k,Y)[Delta E_k(Phi_b)-Delta E_k(Phi_0)]
is a valid CONDITIONAL stronger dictionary. Actual operator identity/linearity is a source obligation, not an inference from Lemma 1 alone.

## 3. Mayer-level finite-difference algebra, without extra epsilon factors

For any two complex potentials V_0(Y),V_1(Y) on the SAME source complete Mayer index Y, adopt the mathematical convention w_i(Y)=exp(V_i(Y))-1. (CMP116 (2.1) OCR has damaged signs; if the precise original convention uses exp(-V), replace V by -V consistently.)

Then EXACTLY,
  Delta w(Y) = w_1(Y)-w_0(Y)
      = exp(V_1(Y))-exp(V_0(Y))
      = Delta V(Y) int_0^1 exp(V_0(Y)+t Delta V(Y)) dt.   (R101.3)

This local algebraic interpolation is NOT an RG trajectory and takes no logarithm of an artificial intermediate partition function. Thus
  |Delta w(Y)| <= |Delta V(Y)| exp[max(Re V_0(Y), Re V_1(Y))].    (R101.4)

In particular even if w_0(Y)=0 (V_0(Y)=0 on the selected branch), a new Mayer activity can be controlled by delta V without dividing by w_0. This is the fixed-complete-carrier activation identity already anticipated in R93, now placed against the actual SINGLE-TRAJECTORY CMP116 potential-source witness.

For a declared rooted entropy-inclusive norm at root x,
  ||Delta V||_(lambda,x)=sum_(Y contains x) exp(lambda d_k(Y)) sup_source_complex |Delta V(Y)|,
the sum of |Delta w(Y)| receives the same rooted bound times a uniform source-local sup exp(Re V) majorant IF that majorant and the common source chart are verified. No assertion is made that CMP116's unmarked Lemma-3 bound alone supplies ||Delta V||.

R90–R93's tagged positive majorants, including replacement versus new zero-baseline activation, remain the correct ABSTRACT transfer machinery. The new input theorem, not another combinatorics lemma, is an ACTUAL two-history relative localized-potential estimate.

## 4. New sharply typed open native gates

(A) Current coupling / renormalization: CMP109's E_k contains historical vacuum and marginal Wilson-extraction bookkeeping. Even equal current g_k does not by notation force same local beta projection after the next step. The new V_k source potential must NOT be declared irrelevant solely by its label. Keep the beta-history marginal difference and a repeated Loc_F² subtraction separate.

(B) Common current Gaussian: CMP109 (2.10)–(2.13) has constrained independent variable C and covariance (C* A^(k) C)^(-1) that depend on regular background and source coordinates. Source equality and conditioning for two histories must be proved; matching physical lattice spacing does not produce it. If different, R82/R99 moving-covariance scores or R100 common-dominated endpoint weight comparison are needed, including log Z^(k), chart Jacobians and normalization.

(C) Cutoff: CMP116 (2.3) explicitly treats chi_k separately from V_k in its D/P/Z0 localization, and R99/R100 prove that sharp cutoff mismatch can create quadratic background response with D=0. This MUST be an independent comparison channel.

(D) Source regular domain: CMP116 Lemma1/2 bounds are proved in one-trajectory analytic (U,J,B) corridors; the intersection of two actual history domains at aligned scales, with uniform radius in cutoff and volume and source root geometry, has not been established.

(E) Relative bound versus absolute bound: Lemma1 (1.36) and Lemma3 (2.38) are absolute single-trajectory bounds. They do NOT say the two-history difference has a UV-decaying per-root factor. Counterexample: for each N, V_(N,0)(Y*)=+epsilon, V_(N,1)(Y*)=-epsilon on one common local source index Y*, both satisfy the same |V|<=epsilon absolute bound and common analytic domain, yet |Delta V|=2epsilon independent of N. Therefore no geometric cutoff summability follows.

(F) Second-moment beta: even a genuine relative potential bound must be propagated through conditioned Gaussian, connected-log exponentiation, Ward/Taylor subtraction, two background insertions, and the source-normalized mixed spatial moment defining beta. R77–R85 provide CONDITIONAL consumers, not source-native closure.

(G) Primary alpha: CMP109 Eq(0.29)'s original-page V^(j) definition, exponent, norm and constants remain source-image-held. CMP116's V_k(Y,B) is an INPUT potential; the final "irrelevant" Eq(0.29) activity is an OUTPUT after vacuum/Wilson projection. It cannot be identified with Delta V_k(Y) or with first extra-UV-layer defect without another native source dictionary.

(H) Global: R/B, large fields, full cutoff/volume Cauchy, RP/OS and physical-time spectral gap are independent obligations.

## 5. Determination and tight YM-R102 frontier

SOURCE-TEXT-WITNESS ESTABLISHED:
- CMP116 Lemma1 (1.33) actually localizes the inherited E_k difference into V'_k(Y);
- CMP116 Lemma2 (1.41) packages full current step into V_k(Y);
- CMP116 (2.1) Mayer expansion uses that family and (2.3) separately localizes sharp chi_k;
- CMP116 (2.9)–(2.13) builds H(Z) and connected-log effective action;
- CMP116 Lemma3 (2.38) gives a SINGLE-TRAJECTORY unmarked activity bound under restrictions.

CERTIFIED ABSTRACT:
- R101.1 frozen-current exact inherited interaction difference;
- R101.2 termwise difference if same complete indexed convergent representation;
- R101.3/4 exact Mayer activation/change estimate independent of baseline activity being nonzero;
- two individually small/local potentials can have nonsummable historical difference.

CONDITIONAL NATIVE / OPEN:
- two actual cutoff histories synchronize g_k, background, gauge slice, covariance and chi_k on the same source D_k family;
- CMP116 localization for historical difference is common/linear or has an independent Lipschitz relative estimate;
- rooted analytic TWO-HISTORY potential difference with true summable UV excess and two-background derivative control;
- entire moving Gaussian / cutoff / deterministic beta-normalization channels;
- original Eq(0.29)/(5.37)/(5.42) image verification and source V^(j) output / V_k input distinction;
- all continuum, OS, gap tasks.

YM-R102 (UNCONSUMED): audit source-owned CMP116 Lemma1 localization map and original domain/gauge dependence to decide whether it is linear in inherited E_k at FROZEN current g/background, or whether localization consumes history-dependent propagators/chart. If source-linear, formulate the minimal quantitative ROOTED relative bound on Delta E_k that would pass to Delta V'_k; if not, isolate the exact operator-difference term. Do not manufacture positive-alpha or history-age decay; original scan receipt remains held.

Highest cumulative reference [92], next [93]. Historical files preserved.
