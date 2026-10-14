# YM-R99 — source-shaped one-step historical derivative / normalized Gaussian score and cutoff integrity

Date: 2026-10-14
Repository: monocap-tech/yangmills
Prior authoritative commit: YM-R98 6fa9c52f3b559892af64aecf5875c378573befa1
Status: COMPLETE AS PRECISE ABSTRACT DERIVATION AND NATIVE SOURCE CUTSET; HISTORY-AGE, EQ029 AND CONTINUUM GATES OPEN
Next live cursor: YM-R100 (unconsumed).
No 4D Yang–Mills existence, Osterwalder–Schrader continuum or positive mass-gap claim.

## 0. Preflight and source custody

Main was verified at YM-R98 before investigation. Relevant historical passes consulted: R77 weighted second-moment projection; R78 determinant jet/dimension; R82 normalized Gaussian covariance interpolation; R90–R93 fixed versus moving CMP116 localization and marked termwise transfer; R97–R98 source-history and physical-time separation. Existing [7],[21],[59],[85],[90]–[92] are reused. Highest cumulative bibliography remains [92], next new source [93].

CMP109 [7] originally published in CMP109(1987), pp249–301, DOI 10.1007/BF01215223. Rutgers/publisher page confirms 4D small-field RG/beta architecture but is not itself equation-level custody. The full third-party OCR/text witness remains
  https://github.com/chboishabba/dashi_agda/blob/master/Docs/support/reference/balaban-source-extracts/cmp109-effective-actions-part-i.txt
  Git blob f1aec083a3a6470c67a2c1205ca740c2583fe37a.
This was actually read, but its original printed Eq(0.29), (5.37), (5.42) images were not available. Therefore exact displayed signs, tensor normalization, polymer norm, alpha quantifiers and coupling-domain constants remain ORIGINAL-IMAGE-OPEN.

Usable source PROSE and formula-locator roles in the OCR:
- printed pp256–257 around (0.22)–(0.23), witness lines 398–410: E_k includes prior coupling dependence;
- printed p264 around (1.20)–(1.22), lines 765–801: one-step merged fluctuation contribution, polarization second background variation, beta from mixed Fourier moment;
- printed pp267–268 around (2.10)–(2.15), lines 943–1004: B=g_k B' linearized constrained Gaussian, remaining independent variables B with covariance (C* A^(k) C)^(-1), the logarithm of a NORMALIZED Gaussian interaction integral with characteristic cutoff chi_k, and coupling renormalization;
- printed pp290–298 (4.35), (4.37), (5.8)–(5.10), (5.37)–(5.44): source-localized quadratic kernel resummation, spatial Ward/decay, marginal plus higher-derivative decomposition;
- printed p298, lines 2494–2499: beta_j notation explicitly SUPPRESSES dependence on all preceding couplings.

Source-semantic boundary: the one-step source formula is a function of its current background, g_k and inherited E_k. Historical coupling variation may be viewed as an off-trajectory parameter variation ONLY if the native current-step analytic chart actually extends over those independent coupling variables. A canonical tuned sequence is not automatically an open Cartesian parameter box.

## 1. Source-shaped split: current Gaussian block versus earlier history

Define a FINITE COMMON GAUGE-FIXED CARRIER and source-aligned external background b, coupling history h=(g_0,...,g_{k-1}), and prescribed current coupling g_k. A convenient abstract representation of the *complete one-step correction* is

  F_k(h,b)
   = D_k(h,b) + log Z_k(h,b),                              (R99.1)
  Z_k(h,b)
   = integral chi_k(h,b,y) exp(U_k(h,b,y)) d gamma_{C_k(h,b)}(y),

where gamma_C is a normalized centered Gaussian on a finite-dimensional independent fluctuation chart. D_k must include whatever constrained Gaussian normalization log Z^(k), chart Jacobian, deterministic source terms and background counterterms are OUTSIDE the normalized nonlinear integral. The split is a DEFINITION OF ABSTRACT BOOKKEEPING, not a newly quoted literal decomposition of CMP109, and all pieces must be source-identified before native use. The normalized log integral may be vacuum-subtracted; an independent b=0 constant disappears under the subsequent quadratic b-variation, but a background-dependent logdet does not.

For s<k, consider a formal partial derivative w.r.t. h_s holding current g_k, source block geometry and external b fixed. The *displayed* CMP109 current Gaussian (2.10)–(2.13) is constructed from the current source covariance/background rather than listing an independent earlier-coupling argument. The inherited action E_k in the interaction DOES contain earlier couplings by printed source prose. Hence a plausible and materially cheaper native target is

  [d_(h_s) C_k =0, d_(h_s) D_k=0, d_(h_s) chi_k=0] (FIXED-CURRENT-CHART HYPOTHESIS)
       => d_(h_s) F_k = expectation of d_(h_s) U_k.

This is CONDITIONAL, not a blanket source assertion about all hidden dependence or the N-vs-(N+1) comparison. At aligned cutoff depths, C/chart/background/localization can move and must be compared independently (R82/R90/R91). In particular the step-index or absolute cutoff should not be modeled as a smooth h coordinate.

## 2. Exact Gaussian score derivative: works for a fixed sharp cutoff

CERTIFIED FINITE-DIMENSIONAL LEMMA. Let C(h,b) be C^1 and real symmetric positive definite; let chi(b,y)>=0 be measurable, bounded and independent of h, perhaps a sharp indicator; let U(h,b,y) be C^1 in h with integrable differentiable chi exp(U); and suppose Gaussian density derivatives are dominated uniformly near the chosen h and Z>0. Write rho for the normalized TILTED law proportional to chi exp(U) d gamma_C.

The normalized Gaussian density has logarithmic derivative

  d_h log gamma_C(y)
   = 1/2 [y* C^(-1) (d_h C) C^(-1) y
            - Tr(C^(-1) d_h C)].

Consequently

  d_h log Z
    = <d_h U>_rho
      + 1/2 < y* C^(-1) (d_h C) C^(-1) y
                 - Tr(C^(-1) d_h C) >_rho.             (R99.2)

Proof: differentiate the finite-dimensional Gaussian density under the common Lebesgue integral, divide by Z. The Gaussian score includes the derivative of the normalization determinant and requires no y-derivative of chi. In particular a FIXED SHARP chi is permitted under the stated domination and differentiability of U,C.

If chi is ALSO h-dependent and differentiable in a suitable sense, append

  (1/Z) integral (d_h chi) exp(U) d gamma_C.              (R99.3)

For a moving hard cutoff, d_h chi is usually a boundary measure/distribution rather than an ordinary bounded function; there is NO license to set it to zero. A moving gauge constraint/integration subspace additionally requires a common source chart, its Jacobian and a justified transported-measure derivative.

Under smooth enough chi exp(U), Gaussian integration by parts rewrites the covariance score channel as

  1/2 sum_ab (d_h C_ab)
      < U_ab + U_a U_b
        + 2 (d_a log chi) U_b
        + (chi_ab/chi) >_rho,                         (R99.4)

where written chi derivatives are valid only away from zeros and with integrability. If chi≡1 (or smooth and absorbed into U through a legitimate nonvanishing log), this reduces exactly to
  1/2 sum_ab d_h C_ab <U_ab+U_a U_b>_rho,
the R91/R82 smooth Gaussian response identity. The score form R99.2 is the safe default for source-shaped characteristic functions.

Differentiating (R99.1) with respect to earlier h_s, and applying the source-defined two-background variation, gives formally

  d_(h_s) D_b^2 F_k =
    D_b^2 [d_(h_s) D_k
           + interaction-score channel
           + covariance-score channel
           + moving-cutoff/transport channel],        (R99.5)

subject to commutation of h and b derivatives, chart/source covariance and existence of a localized kernel. This is NOT automatically a momentum second derivative: CMP109's local resummation and Fourier/Ward projection require their own source dictionary and second-spatial-moment budget.

## 3. Exact moving-cutoff obstruction, including a nonzero background second jet

Let Y be standard normal, C=1 fixed, U=0 and chi(h,b,y)=1_{y<=h+b}; all background and historical dependence is in a sharp cutoff. Set Z(h,b)=Phi(h+b), Phi the standard Gaussian cumulative distribution.

Although d_h C=0 and d_h U=0, we have

  d_h log Z(h,b) = phi(h+b)/Phi(h+b) != 0.

Moreover
  d_h d_b^2 log Z(h,b)|_(h=b=0)
   = (log Phi)'''(0)
   = sqrt(2/pi) [ 4/pi - 1 ] > 0.

Proof: r(x)=phi(x)/Phi(x), r'=-x r-r^2; r''=-r-x r'-2r r', so at zero r''(0)=-r(0)+2r(0)^3. The expression follows from r(0)=sqrt(2/pi).

Thus even a *quadratic background polarization-type response* can arise entirely from moving small-field domain geometry. Treating a moving chi as fixed in R99.2 misses a genuinely nonzero term. This is an ABSTRACT control, not evidence that the particular CMP109 chi_k has this derivative.

Also note a fixed but SHARP chi under covariance variation cannot be handled by naively applying the smooth formula <U_ab+U_aU_b>; the Gaussian score R99.2 remains valid under its hypotheses and automatically captures the fixed hard boundary effect.

## 4. Local-history attenuation requires an RG dynamical inequality

For an abstract differentiable map on a Banach complementary coordinate K with successive maps T_r(K,h_r), consider a perturbation inserted in h_s. The variational recurrence on a native fixed trajectory is

  v_(s+1) = J_s := d_(h_s) T_s,
  v_(r+1) = L_r v_r,  L_r = D_K T_r,
  v_j = L_(j-1) ... L_(s+1) J_s.                        (R99.6)

If on a SOURCE-DEFINED repeatedly re-extracted irrelevant quotient
  ||L_r||<=q<1 and ||J_s||<=M uniformly,
then ||v_j||<=M q^(j-s-1). This is a valid CONDITIONAL sufficient derivation of history-age gain. It is not the same thing as spatial propagator decay or the CMP116 *absolute* E-bound. R63–R68 already distinguish projected quotient contraction from source-scale absolute activity bounds.

If there are later direct-history injections J_(r,s), add the Duhamel sum over r; the q-product alone is no longer sufficient. The marginal/Wilson sector is NOT known to be contractive under these maps and may carry a neutral direction. Therefore a source-realizable history-response decay for beta needs either repeated exact marginal extraction with quantitative cancellation, a direct marked full-polarization response estimate, or a weaker summable fixed-endpoint mismatch. One cannot simply iterate an unproved q on the entire state.

## 5. What now actually needs a source theorem

At fixed current Gaussian chart the most economical potential native branch is:
  [E_k inherited coupling dependence]
    -> insertion d_(g_s) U_k inside (2.13)
    -> one-marked normalized interacting expectation / connected-log resummation
    -> spatial second moment of the full differentiated Pi
    -> beta history response.
But to derive a bound with age j-s, the insertion must acquire attenuation through the many-step RG/localization, not merely exponential decay in spatial |x-y|. R90–R93 give abstract potential/marked transfers but do not supply a source-native E_k historical insertion majorant or the moving cross-cutoff dictionary.

Independent moving-covariance, chart, determinant, gauge/cutoff and source-retuning terms remain if two different cutoff depths are compared. The precise stage obligations are:

(A) recover exact source decomposition of (1.3),(1.6),(2.13) and determine which earlier-history variables appear in D_k,C_k,chi_k,U_k when present g_k is held fixed;
(B) prove the relevant off-trajectory historical differentiable extension on the weak-coupling source complex collar, or abandon differentiation and use actual two-trajectory finite differences;
(C) construct one-marked history insertion with rooted/lattice decay and a genuine HISTORY-AGE rate or directly summable endpoint norm;
(D) control the full source-defined polarization's second spatial moment, Fourier normalization and beta projection after Gaussian, interaction and localization;
(E) separately compare source geometry and cutoff charts when N changes, including Gaussian score/determinant and boundary flux;
(F) verify original printed CMP109 Eq(0.29),(5.37),(5.42) from actual page images, and exact CMP109-to-CMP116 one-layer dictionary;
(G) retain distinct R/B/large-field, continuum cutoff Cauchy, reflection positivity/OS and uniform physical-time gap obligations.

The fact that U goes to zero as current g_k goes to 0 (source prose near (2.13)) does NOT furnish a history-derivative estimate: f(g,h)=g^2 sin(h/g^4) can go to 0 uniformly in h while d_h f is O(g^(-2)). A uniform differentiated analytic collar is an additional hypothesis. No power or uniform derivative gain is inferred from mere vanishing.

## 6. Determination and next unconsumed cursor

CERTIFIED ABSTRACT:
- R99.2 Gaussian-score derivative on a finite normalized carrier with fixed possibly sharp cutoff;
- R99.3 moving-cutoff flux accounting under a justified differentiability interpretation;
- nonzero background second-jet moving-boundary example (logPhi)'''(0);
- R99.6 variational product and conditional q^(history-age) sufficient theorem.

TEXT-WITNESS SOURCE PROVENANCE:
- CMP109 E_k prior-history dependence, current B=g_k B' covariance and normalized fluctuation log integral; original exact formula images still held.

CONDITIONAL NATIVE:
- absence of earlier-history dependence from current Gaussian, D_k and chi_k when fixed current g_k/background/chart;
- differentiable source history extension and full marked/CMP116 response;
- source-aligned full Pi/beta moment, history attenuation or summable fixed-endpoint mismatch.

OBSTRUCTED AS GENERIC INFERENCES:
- historical dependence of marginal beta can be bounded from spatial covariance decay alone (R98);
- frozen smooth interpolation identity may be applied to moving hard cutoffs;
- the vanishing of nonlinear interaction as g_k->0 implies derivative smallness in arbitrary earlier h;
- finite OS transfer positivity or absolute small-field RG estimates automatically provide continuum Cauchy or physical mass gap.

No native history-decay theorem or Eq(0.29) gate is closed. Schur remains non-load-bearing for these source-history response obligations.

YM-R100 (UNCONSUMED): inspect source-native dependence of actual inherited E_k in (2.13) at frozen current coupling, and determine if a two-trajectory/finite-difference source bound can avoid the unproved off-trajectory history derivative; then test compatibility with the marked CMP116 potential input and R98 prefix insertion. Original CMP109 scanned equation image custody remains a hard source gate. No continuum or gap claim.
