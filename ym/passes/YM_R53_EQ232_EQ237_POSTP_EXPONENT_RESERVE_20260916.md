# YM-R53 — CMP116 Eq. (2.32)–(2.37) post-P geometry / exponent-reserve closure

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R52_20260916.json`
Next cursor: YM-R54 (unconsumed)

## Question

After R51 closed the D-stage Eq. (2.29) summation and R52 closed the native P-stage Eq. (2.31) carrier/count and entropy bracket, R53 audits the remaining native resummation from partially resummed Z0 data through fixed Z0' and the final Z0' sum. The target is to determine whether CMP116 itself supplies the full geometry, constant hierarchy, and exponent reserve leading to Lemma 3 / Eq. (2.38).

## Primary source inspection

CMP116 [21], printed pages 19–20, was inspected directly at the source PDF. The relevant source chain is (2.33)–(2.38).

## 1. Partially resummed Z0 bound

After the D and P sums, the source writes the partially resummed term in the form (2.35):

`|sum_{D,P} (2.14)|`
`<= exp(-(kappa1-1)(LM)^(-4)|Z\Z0'|)`
`   * [prod_i epsilon2 exp(-(1-5 delta) kappa d_k(Z_i))]`
`   * exp(O(1) alpha5 |Z|)`

where Z0 is a union of connected components Z_i.

This is the exact native entry to the post-P stage. No normalized standalone Z0 theorem is required beyond this displayed partially resummed estimate.

## 2. Z0 -> Z0' geometry

Fix a connected component Z_i' of Z0'. For every connected component Z_i of Z0 determining it, the source states

`2 d_k(Z_i) >= L d_{k+1}(Z_i')`.  (2.36)

The source then decomposes the sum by the number n of Z_i components determining a fixed Z_i'. Using (1.28) with delta*kappa, plus the finite `(L+2)^4` placement sum, one obtains the same basic form with

`epsilon2 -> (L+2)^4 O(1) epsilon2`

and

`(1-5 delta) kappa d_k(Z_i) -> ((1-6 delta)/2) L kappa d_{k+1}(Z_i')`.

For n>1 the source leaves one exponential and bounds the remaining same-Z_i' exponentials by one. The n>=1 sum is therefore bounded by

`2 (L+2)^4 O(1) epsilon2`

provided

`(L+2)^4 O(1) epsilon2 <= 1/2`.

## 3. Families of Z_i' and fixed-Z0' estimate

The source next sums over families of distinct localization domains Z_i' with union Z0'. It reuses Eq. (2.29) at scale k+1, with the extracted delta-weight now `delta/2 * L*kappa*d_{k+1}(Z_i')`, and uses Eq. (2.27) on the remaining decay.

Under

`2 (L+2)^4 O(1) epsilon2 exp(5 kappa) <= 1`,

CMP116 obtains Eq. (2.37):

`|sum_{D,P,Z0} (2.14)|`
`<= exp(-(kappa1-1)(LM)^(-4)|Z\Z0'|)`
`   * prod_i [2(L+2)^4 O(1) epsilon2`
`             * exp(-((1-7 delta)/2) L kappa d_{k+1}(Z_i'))]`
`   * exp(O(1) alpha5 |Z|)`

where Z_i' are the connected components of Z0'.

Thus the seven-delta fixed-Z0' source estimate is explicit and source-owned.

## 4. Final Z0' sum

The final sum is over Z0', equivalently over Z\Z0'. The source uses an adapted form of Eq. (2.32), together with the connected-component product and half of the first reserve factor, to bound the square-bracket decay by

`exp(-((1-7 delta)/2) L kappa d_{k+1}(Z))`.

The source assumes

`(kappa1-1)/2 >= 2 L kappa`.

The remaining half of the first reserve factor controls the sum over Z\Z0' by an Eq. (2.34)-type estimate, producing

`exp(exp(-(kappa1-1)/2) (LM)^(-4) |Z|)`.

This is of the same volume-exponential type as `exp(O(1) alpha5 |Z|)`.

## 5. alpha5 / C3 hierarchy

The source recalls

`alpha5 = O(1) exp(-(delta0/36) M) + O(alpha0+alpha1) + O(1) alpha4 + gamma2`

(up to the source's fixed absolute constants), and assumes `(LM)^4 alpha0`, `(LM)^4 alpha1`, `(LM)^4 alpha4`, `(LM)^4 gamma2` are bounded uniformly, e.g. by one. Hence

`O(1)(LM)^4 alpha5 + exp(-(kappa1-1)/2)`

is bounded by an absolute constant.

The source then spends one additional factor

`exp(-(delta/2) L kappa d_{k+1}(Z))`

and uses Eq. (2.30) to absorb these residual volume exponentials. This is exactly the reserve transition

`(1-7 delta)/2 -> (1-8 delta)/2`.

One factor `2(L+2)^4 O(1) epsilon2` is retained; all remaining such factors are bounded by one. Since

`epsilon2 = 2 E0 epsilon1 C1 alpha4^(-1) alpha6^(-1) M^q exp(C2 kappa1)`,

the retained factor is `C3 epsilon1`, with

`C3 = 2(L+2)^4 O(1) 2 E0 C1 alpha4^(-1) alpha6^(-1) M^q exp(C2 kappa1)`.

## 6. Lemma 3 endpoint

CMP116 therefore proves

`|H(Z)| <= C3 epsilon1 exp(-((1-8 delta)/2) L kappa d_{k+1}(Z))`.  (2.38)

This is the exact native Lemma-3 activity estimate.

## Determination

The entire post-P resummation and exponent-reserve stage is CLOSED at mathematical/source level:

`Eq. (2.35) partially resummed Z0 bound`
`-> Eq. (2.36) component geometry`
`-> fixed-Z0' component/family resummation`
`-> Eq. (2.37) seven-delta bound`
`-> final Z0' sum with half reserve`
`-> alpha5 volume absorption`
`-> spend delta/2 decay`
`-> Eq. (2.38) eight-delta Lemma-3 bound`.

The source-to-Lean D/P/Z0/Z0'/component flattening remains a formalization dictionary. It is not a mathematical research obligation for the source proof.

Combined with R50–R52, the native CMP116 Lemma-3 resummation chain is now exhausted at mathematical/source level.

## Negative results / guardrails

- Do not split Eq. (2.37) into independent normalized Z0 and Z0' source theorems; the source uses a combined ordered resummation.
- Do not treat the seven-delta to eight-delta transition as arbitrary slack: it is the explicit delta/2 reserve spent to absorb the alpha5/volume exponentials.
- Do not omit the conditions `(L+2)^4 O(1) epsilon2 <= 1/2`, `2(L+2)^4 O(1) epsilon2 exp(5 kappa) <= 1`, and `(kappa1-1)/2 >= 2L kappa`.
- Do not treat project index encodings as additional source mathematics.
- Do not interpret Lemma 3 closure as a proof of four-dimensional Yang-Mills existence or continuum mass gap.

## Next frontier — YM-R54

Native Lemma-3 closure / remaining one-step baseline consolidation.

Assemble R47–R53 into a single source-level one-step closure ledger and determine the next genuinely mathematical native obligation after CMP116: either post-Lemma-3 effective-action exponentiation / Paper-I inductive handoff, or the complete-density / large-field CMP119/CMP122 frontier if the small-field one-step chain is now exhausted.

## References

Reused [21] CMP116. No new cumulative source consumed. Highest source ID remains [80]; next new source is [81].