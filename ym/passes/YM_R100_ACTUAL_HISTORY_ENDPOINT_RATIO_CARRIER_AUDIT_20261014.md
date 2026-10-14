# YM-R100 — native two-trajectory inherited-interaction finite difference / endpoint ratio and common-carrier obstruction

Date: 2026-10-14
Repository: monocap-tech/yangmills
Prior head verified: YM-R99 4e63f0db885fecb41988a86486f4658a537dfb9d
Status: COMPLETE AS A FINITE-ENDPOINT MATHEMATICAL AUDIT; NATIVE YANG–MILLS BETA / EQ029 / CONTINUUM GATES OPEN
Next unconsumed cursor: YM-R101
Claim discipline: OPEN RESEARCH PROGRAM; no continuum Yang–Mills or positive mass gap.

## 0. Aim and source custody

R99 identified a source-shaped full one-step log integral, separating normalized Gaussian history score, inherited interaction, moving covariance, gauge chart, deterministic normalization and sharp cutoff. It warned that derivatives with respect to independently varied earlier couplings may not be meaningful on the canonical tuned RG trajectory. R100 asks for an EXACT comparison of two ACTUAL admissible histories, not an interpolated artificial history.

Preflight repository: main was YM-R99. R63–R68 and R72 are the controlling old stable-fiber/scalar mismatch audits; R77–R85 control the second-spatial-moment, normalized Gaussian and connected-log interface; R90–R93 control CMP116 tagged potential source and moving localization. No R99 historical records are overwritten.

Repeated source [7] Bałaban CMP109 and [21] CMP116, [59] CMP119, [85] secondary locator; highest cumulative source [92] unchanged. Publisher/Rutgers article identity and abstract verify 4d SMALL-FIELD one-step localized actions/beta recursion, not continuum existence (https://www.researchwithrutgers.org/en/publications/renormalization-group-approach-to-lattice-gauge-field-theories-i-/). Actual inspected third-party OCR text of [7] is chboishabba/dashi_agda file 'Docs/support/reference/balaban-source-extracts/cmp109-effective-actions-part-i.txt', Git blob f1aec083a3a6470c67a2c1205ca740c2583fe37a. Printed pp256–257 prose explicitly gives E_k prior-coupling dependence; printed pp267–268 around Eq(2.13) describes B=g_k B' and the constrained normalized Gaussian integral; printed p298 explicitly says beta_j(g_(j-1)) suppresses all previous coupling dependence. The original equation images for Eq(0.29), (5.37), (5.42) have not been inspected; their mathematical signs, norms and constants remain SOURCE IMAGE HELD. CMP116 exact inter-cutoff marked carrier is NOT established.

## 1. THEOREM: real, fixed-carrier two-endpoint log ratio, with no history interpolation

Let Y be a fixed finite-dimensional real fluctuation carrier and mu a FIXED normalized Gaussian probability, or more generally a finite positive reference measure. Let chi(Y)>=0 be a common bounded measurable cutoff (may be sharp). Let U_0(b,Y), U_1(b,Y) be two real integrable endpoint interactions attached to two actual admissible coupling histories at the SAME current source chart/current coupling and the same background variable b. Assume
  0<Z_i(b)=int chi(Y) exp(U_i(b,Y)) dmu(Y)<infinity.

Define D(b,Y)=U_1(b,Y)-U_0(b,Y) and the tilted baseline probability
  d rho_0(b,Y)=Z_0(b)^(-1) chi(Y) exp(U_0(b,Y)) dmu(Y).
Then EXACTLY,
  Z_1(b)/Z_0(b)=<exp D(b,Y)>_(rho_0),                      (R100.1)
  logZ_1-logZ_0=log<exp D>_(rho_0).
This is algebraic (divide one existing integral by the other); no third source trajectory or artificial independent h_s coordinate is needed.

If |D(b,Y)|<=epsilon uniformly on the common real carrier, then
  exp(-epsilon)<= Z_1/Z_0 <=exp(epsilon),
  |logZ_1-logZ_0| <=epsilon.                               (R100.2)
This is an ABSOLUTE global bound: epsilon must control the total input interaction, not merely individual roots; a volume-growing sum of small local insertions may fail it.

The full one-step effective correction may be F_i=K_i+log Z_i (or K_i-log Z_i under source conventions); the deterministic K_i difference must always be appended separately. The SOURCE-NATIVE mapping from actual CMP109 (1.3)/(1.6)/(2.13), Gaussian normalization Z^(j), cutoff and inherited E_k to this frozen-current data is still a hypothesis. In particular the two canonical cutoffs may have distinct current couplings, charts and fine dimensions, so (R100.1) is NOT automatically the N versus N+1 common-scale comparison.

## 2. THEOREM: endpoint two-background response, no complex history-coordinate variation

Assume additionally a fixed b-INDEPENDENT positive reference weight chi(Y)dmu(Y), U_i twice differentiable in two real external background coordinates x,y, justified dominated differentiation and positivity. Standard tilted expectation calculus gives
  partial_xy logZ_i = <U_(i,xy)>_i
                     +Cov_i(U_(i,x),U_(i,y)),             (R100.3)
where rho_i is the normalized endpoint tilted probability. For a moving b-dependent cutoff, covariance or chart the formula needs their separate score/boundary contributions (R99), and this theorem does not apply as written.

Suppose uniformly in Y at b=0,
  |D|<=epsilon, |D_x|,|D_y|<=epsilon_1, |D_xy|<=epsilon_2,
  |(U_0)_x|, |(U_0)_y|<=K_1, |(U_0)_xy|<=K_2,
all nonnegative. Put delta=e^(2epsilon)-1.

Then the RADON-NIKODYM ratio between endpoint probabilities satisfies
  d rho_1/d rho_0=exp(D)/<exp D>_0 in [e^(-2epsilon),e^(2epsilon)],
so for |O|<=M,
  |<O>_1-<O>_0| <=delta M.                            (R100.4)

An elementary covariance telescoping bound
  |Cov_1(A,B)-Cov_0(A,B)| <=3 delta ||A||_infty ||B||_infty
combined with |Cov(A,B)|<=2||A||_infty||B||_infty yields

  |partial_xy(logZ_1-logZ_0)|
    <=epsilon_2 + delta K_2 +3 delta K_1^2
       +4 K_1 epsilon_1+2 epsilon_1^2.                 (R100.5)

Proof: write (U_1)_x=(U_0)_x+D_x and similarly y, subtract (R100.3). The expectation of U_xy contributes epsilon_2+delta K_2. The baseline covariance difference contributes 3delta K_1^2; the two cross terms <=2K_1 epsilon_1 each and the D_x,D_y covariance <=2epsilon_1². No interpolation in ANY history variable was used.

This is a CERTIFIED finite-dimensional real endpoint bound. It does not establish a source-normalized momentum derivative, infinite-volume/local rooted estimate, or summable UV defect. Constants K_1,K_2 could grow with volume and total-action sup norms can be useless. The actual CMP109 Pi comes after localization/resummation and Ward/F² projection.

## 3. COMPLEX ENDPOINT RATIO LEMMA — avoids synthetic-history zero crossings

Suppose on a common complex background polydisc |b_x|<r_x, |b_y|<r_y the endpoint integrals Z_0,Z_1 are holomorphic, Z_0 never vanishes, and a common dominating measure lambda with integrable weights w_i(b,Y) permits
  Z_i(b)=int w_i(b,Y) d lambda(Y),
  sup_(b on polydisc) [int |w_1-w_0| d lambda / |Z_0(b)|] <=eta<1.

This formulation ALLOWS different cutoff weights and different SPD Gaussian densities on the same finite chart, but the full chart and densities must be explicitly identified; lambda need not be probability. It controls the FULL measure difference, not merely U_1-U_0.

Then |Z_1/Z_0-1|<=eta. Hence Z_1/Z_0 lies in the disk centered at 1 with radius eta, and the holomorphic branch
  Delta L(b)=log(Z_1(b)/Z_0(b))
is uniquely fixed by its power series around 1. By summing the logarithm series,
  sup_b |Delta L(b)| <=-log(1-eta).
Cauchy's estimate therefore gives, for x != y,
  |partial_xy Delta L(0)| <= [-log(1-eta)]/(r_x r_y).  (R100.6)
For twice the same coordinate the conservative bound is 2[-log(1-eta)]/r_x².

This requires NO logarithm of an interpolating synthetic history, avoiding R83's potentially vanishing Z_t on nonphysical interpolation paths. It DOES require the extra quantified complex ratio margin eta and background/source collar; real endpoint positivity alone does not certify either. It is GLOBAL until spatial root/tag attachment and marginal normalization are added.

## 4. SOURCE REINTEGRATION: the cutset becomes more sharply typed

For CMP109 (2.13) at FROZEN current g_k, background and identified constrained Gaussian covariance, changing an admissible prior history potentially changes the inherited E_k in the nonlinear interaction. If the same normalized Gaussian, chi, gauge chart and deterministic current contribution truly serve both histories, then R100.1 applies, with D the entire difference of inherited interaction insertions. The historical label is not required as an independent smooth coordinate.

To upgrade:
(A) verify that two actual tuned histories can be compared with a common CURRENT coupling and source domain, or first explicitly separate current-coupling mismatch;
(B) establish the exact E_k -> U_i difference inside CMP109 Eq(2.13), including sign, background subtraction, inherited Wilson/beta terms, and any history dependence of Gaussian normalization or chi;
(C) construct the common CMP116 conditioned chart, including any extra fine shell, moving Green covariance, gauge cutoffs and root indexing;
(D) provide a *localized* root-wise bound on the FULL ENDPOINT DIFFERENCE (or a connected-log endpoint ratio), including analytic two-source background insertions and a spatial second-moment norm;
(E) prove an ultraviolet-depth summable amplitude (or precise marginal-history/coupling terminal condition); CMP109 Eq(0.29) SOURCE-IMAGE verification alone is not a relative two-history bound;
(F) retain R/B and large-field sectors, cutoff and volume limits, full RP/OS and physical-time mass-gap obligations.

R77–R93 already construct abstract rooted/cumulant/marked KP consumers. The new R100 result removes the EXTRA off-trajectory interpolation/differentiability hypothesis for the frozen-current source comparison but does NOT remove the source-tagged activity DIFFERENCE or CMP116 common chart obligations. Interpolation of two honest positive weights is a mathematical convenience; no assumption that its intermediate coupling history is a canonical Bałaban trajectory is needed for this endpoint identity.

## 5. Counterexample: even identical current Gaussian and interaction is insufficient if cutoffs differ

Take Y standard normal, chi_0(Y)=1_{Y>0}, chi_1(Y)=1_{Y<0}. Let U_0(b,Y)=U_1(b,Y)=b_x b_y sign(Y). The Gaussian is the same for both, the interaction difference D=0 everywhere, and each sharp cutoff is independent of background.

But the endpoint partition functions are
  Z_0(b)=(1/2) exp(b_x b_y), Z_1(b)=(1/2) exp(-b_x b_y),
so
  log(Z_1/Z_0)=-2 b_x b_y,
  partial_xy log(Z_1/Z_0)|_(b=0)=-2.
Thus a moving CUT-OFF-CARRIER between two trajectories can generate a nonzero quadratic background mismatch even when the two inherited potentials coincide, without any covariance change.

CERTIFIED ABSTRACT OBSTRUCTION:
  same Gaussian covariance + U_1-U_0=0
  does not imply equality of polarization jets when chi_0!=chi_1.
This is not evidence that Bałaban's own cutoff actually differs in this way. It shows that the fixed-cutoff assumption in R100.1 cannot be silently omitted; the full-weight criterion of Section 3 is the safe carrier-independent branch when an actual common domination exists.

## 6. Distinct issue: spatial localization cannot produce UV summability or historical fade

R98 proved a finite-range Ward-transverse PSD polarization can retain order-one dependence on the oldest coupling; R99 established moving sharp cutoff boundary flux. R100 does NOT negate those no-go results. An absolute source E^(j) bound (even if the original Eq0.29 is eventually verified) is not a bound on D=E^(j)[history1]-E^(j)[history0] with cutoff-uniform UV gain. Nor does the exact log-ratio force a uniform nonvanishing complex margin, rooted connected-log estimate or physical beta/F² second-moment identification.

A pointwise O(g_0^(N)) error with g_0^(N)~N^(-1/2) need not be summable over N. The correct eventual stopping criterion is summability of full normalized projected one-step mismatch with R72 scalar-tail amplification, rather than the amount by which individual current couplings are small.

## 7. Bounded determination and next cursor

CERTIFIED ABSTRACT:
- R100.1 exact two-existing-trajectory partition ratio, allowing a fixed sharp common cutoff;
- R100.2 finite real log-stability from bounded full interaction difference;
- R100.3–R100.5 exact endpoint second-source response and explicit total-variation covariance bound;
- R100.6 complex endpoint relative-weight Cauchy theorem, with no synthetic-history zero crossings;
- sharp-cutoff counterexample proving identical Gaussian+interaction insufficient without cutoff alignment.

TEXT-WITNESS:
- primary [7] prior-coupling history dependence, constrained Gaussian and (2.13) source architecture from third-party paper transcription only.

CONDITIONAL NATIVE:
- actual common-current Gaussian/gauge/constraint and weak regular domain for two histories;
- quantitative inherited E_k endpoint difference as a CMP116 tagged insertion with correct four-dimensional root, analytic two-background moment and UV exponent;
- matching of all deterministic, marginal and cutoff terms, and source Wilson projection;
- appropriate common complex collar/log-ratio margin or separately justified real source differentiation.

OPEN: original printed Eq(0.29),(5.37),(5.42) IMAGE proof/norm/normalization; native one-layer V^(1) dictionary and relative tagged estimate; beta stationarity or summable history defect; continuum Cauchy, OS, mass gap.

YM-R101 (UNCONSUMED): source-first native frozen-current E_k -> CMP109 Eq(2.13) -> CMP116 input POTENTIAL dictionary. Decide whether the difference of two genuine canonical histories becomes a supported local potential insertion on a common chart, or whether deterministic marginal subtraction, Gaussian/cutoff mismatch and/or differing current couplings obstruct the frozen-carrier reduction. Obtain original primary equation image windows if available before any claim about alpha. No further generic transfer theorem is needed until that dictionary is checked.

Highest bibliography [92] unchanged; next new source [93]. Historical R1–R99 records preserved.
