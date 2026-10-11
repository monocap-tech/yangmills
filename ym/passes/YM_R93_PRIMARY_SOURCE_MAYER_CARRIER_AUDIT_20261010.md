# YM-R93 — primary CMP109 Eq029 custody and CMP116 fixed-carrier Mayer-tag consolidation

Date: 2026-10-10
Prior head: YM-R92 checkpoint 57506f0dc61d1a33fb068fbab8907cd783b0cf99
Status: SOURCE/TYPE AUDIT + EXACT FIXED-CARRIER ALGEBRA; NATIVE SOURCE GATES OPEN
Next cursor: YM-R94 (unconsumed)
Claim: UNPROVED RESEARCH PROGRAM; no four-dimensional continuum Yang-Mills, OS axioms or positive mass gap.

## 1. Primary-source search: no invented Eq (0.29)

Verified bibliographic sources identify CMP109 [7], T. Balaban (1987), CMP 109(2), 249–301, DOI 10.1007/BF01215223, and CMP116 [21], 1988, CMP116(1), 1–22, DOI 10.1007/BF01239022. CMP109's primary publisher/Rutgers abstract supports construction of localized effective actions, beta functions and recursive coupling renormalization in a four-dimensional SMALL-FIELD approximation. CMP116's abstract says Part I's fluctuation integral is represented by an exponentiated cluster expansion.

Attempted to recover CMP109 original text (0.29), (5.37), (5.42): Project Euclid article .full provided iframe-only HTML; direct .pdf endpoints and Springer DOI PDF could not be inspected; SciSpace listed a PDF without readable article equations. Project/Library search did not locate this PDF. External public source-audit repository lluiseriksson/THE-ERIKSSON-PROGRAMME has local CMP116 source-page receipts but explicitly flags its B4 CMP109 complete one-step extraction as pending. That is THIRD-PARTY provenance evidence only, not access to the primary CMP109 formula or a public primary PDF. Existing repo source ledger [85] has a candidate a^(4+alpha) Eq (0.29) claim but source extraction was corrected between v1/v2 and the exact V^(j) sign was unresolved in YM-R70. DO NOT PROMOTE either the alpha or source object as verified.

The separate append-only source request lists exact original-page targets, checksum/page/quantifier requirements and provenance blockers.

## 2. Fixed-carrier Mayer identity resolves an artificial bifurcation — EXACT DERIVED

Let P be a FINITE COMPLETE family of candidate localized source domains Y on ONE fixed gauge/conditional-measure/chart carrier. For each Y let V_Y(t)=V_Y^0+t v_Y and put
  w_Y(t) = exp(V_Y(t))-1.
Then, without approximation,
  exp(sum_(Y in P) V_Y(t))
  = prod_(Y in P)(1+w_Y(t))
  = sum_(D subset P) prod_(Y in D) w_Y(t),
and
  w'_Y(t)=v_Y exp(V_Y(t)).
Differentiating the FINITE sum is exact:
  d/dt sum_D prod_(Y in D)w_Y(t)
   = sum_D sum_(Y in D) v_Y exp(V_Y(t))
        prod_(Y' in D, Y'!=Y)w_Y'(t).

If V_Y^0=0, then w_Y(0)=0 but w'_Y(0)=v_Y. Therefore D containing a dormant Y can become active under t-variation without introducing a new type of ghost polymer. In particular, the D-singleton {Y} supplies a nonzero derivative even though its unperturbed Mayer factor vanished. The empty D itself differentiates to zero; this is consistent and does not lose the newly activated Y.

This unifies R91's factor REPLACEMENT and R92's newly ADJOINED seed as two descriptions of the same exact potential variation IF the source uses a fixed complete Y-index family, INCLUDING zero-baseline activities, and the perturbation v_Y belongs to that family.

An optional ghost is still valuable if a new supported object is outside P, if different physical cutoff carriers are not source-identified, or if the perturbation changes a covariance, cutoff, Jacobian or conditioning map instead of only V_Y. Hence the R91/R92 general theorems remain valid for their own jurisdictions; their distinction should no longer be imposed as TWO independent theorem debts on a fixed CMP116 Mayer carrier.

For complex Y potentials, a quantitative elementary estimate is
  |w'_Y(t)|<=|v_Y| exp(Re V_Y(t)).
Thus a source-uniform bound on exp(Re V_Y(t)) and a tagged input v_Y envelope provides the O(u_x) factor needed by R90-R92 WITHOUT dividing by w_Y^0 or requiring a spurious extra epsilon1. Native source parameters and interpolation admissibility remain OPEN.

## 3. What is and is not source-native

Previously source-extracted CMP116 R50 identifies D/Y0/P/Z0 as a first Mayer/localization stage, then a conditioned Gaussian product chart, second weakening and H(Z,Z0)->H(Z), then connected-log exponentiation. R44/R45 already use bounded-support insertion before the native localization and support hull. These make the *place* to test the new derivative clear.

But the displayed abstract w_Y=exp(V_Y)-1 is a GENERIC Mayer identity. It has not been freshly verified word-for-word against CMP116 Eq(2.1), including its possible signs and cutoff factors; those source details must be checked before declaring the actual paper's activity is exactly w_Y with the chosen V notation. More seriously, the candidate CMP109 V^(1) is a marginal-subtracted FIRST GENERATED REGULAR OUTPUT, and there is no primary source receipt identifying it with a change in the CMP116 native input potentials V_k(Y,B) on the SAME aligned physical carrier. CMP119 later writes explicit vacuum and beta/Wilson subtraction (R65/R70), but that does not settle this earlier Eq (0.29) or an across-cutoff equality.

The simplest source-native tagged target is therefore NOT two independent 'replacement' and 'ghost' lemmas. It is ONE potential dictionary with an exact source convention:
  aligned CMP109 extra-layer irrelevant regular term
     -> delta of local CMP116 potential family v_(N,Y)
     -> derivative of native Mayer factors
     -> D/P/Z0/Z0' marked positive bounds.
Every arrow remains source/uniformity sensitive. Moving Gaussian and gauge/chart/large-field/marginal terms require additional channels from R90/R91.

## 4. Original-article request and STOP on speculative consequences

The outstanding source must settle:
(A) CMP109 (0.29): full formula, V^(j) definition and sign, whether alpha>0 actually occurs, precise norm and constants/quantifiers.
(B) CMP109 (5.37),(5.42): physical beta projection and locality.
(C) CMP116 (2.1)-(2.3),(2.14): exact Mayer input/source support to decide the fixed-complete-carrier hypothesis.
(D) CMP119 (2.24)-(2.25): already source-located coupling/regular bookkeeping, but its tail coherence and first-common-scale endpoint identification are separate.
(E) gauge/covariance/cutoff/measure and R/B/large-field sector matching, which do not reduce to a local potential tag.

ALREADY DERIVED: exact zero-baseline Mayer activation and product derivative on a complete fixed carrier, and the correction to distinguish ghost necessity from ordinary zero-index activation.
PRIMARY VERIFIED IN THIS PASS: bibliographic paper identity and paper-level small-field/cluster role, NOT the key equation text.
OPEN NATIVE: original Eq(0.29) and positive-alpha, actual CMP109 V^(1) type and input/OUT convention, actual CMP116 w_Y normalization and Y carrier, tagged termwise/weakening and fixed chart, beta and complete-density transport.

NEXT YM-R94 (UNCONSUMED): SOURCE-FIRST only. Obtain an actual readable original CMP109 (0.29), (5.37), (5.42) and CMP116 native (2.1) source-window receipt. If source remains inaccessible, give a hard no-promotion status and isolate the concrete input file/reading window instead of producing another derivative theorem. Native R75 gates not closed.
