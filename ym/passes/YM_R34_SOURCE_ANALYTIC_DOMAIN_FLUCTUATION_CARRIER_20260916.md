# YM-R34 — source analytic-domain definition / fluctuation-carrier dictionary audit

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior head: `ym/checkpoints/YM_HEAD_R33_20260916.json`
Next cursor: YM-R35 (unconsumed)

## Question

R33 reduced the native UV interface to two source-level tasks:

1. extract the exact coordinate definition of Bałaban's complex field domain
   `U^c_{k+1}(X, alpha_0, alpha_1)` and the field bounds used around CMP116
   (2.20)/(2.22);
2. identify the precise carrier of the product-Gaussian variables `X(b)` in the
   localized activity/component factorization around CMP116 (2.8)-(2.10).

This pass deliberately does not backfill either item from notation or from the
scalar Dimock analogues.

## Source state recovered

The primary CMP116 artifact is known and checksum-custodied in the external
source audit:

- `balaban-rg-II-cmp116-1104161193.pdf`
- SHA-256 `EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC`
- full extracted text `text/balaban-rg-II-cmp116-1104161193.txt`
- localized text windows and rendered pages.

Those artifacts are explicitly recorded as private/local runtime artifacts in
the source-packet manifest; they are not committed in the public repository.
A File-Library search in the current environment did not recover the primary
CMP116 PDF/text packet. Consequently the exact definition of
`U^c_{k+1}(X,alpha_0,alpha_1)` cannot be transcribed honestly in this pass.

The public source ledger does verify the locator:

- CMP116 printed p.15 frames the termwise analytic estimate on
  `U^c_{k+1}(X,alpha_0,alpha_1)`;
- printed p.16, around (2.20)/(2.22), contains the field-dependent estimates;
- after Eq. (2.37), the source assumes `(LM)^4 alpha_0`, `(LM)^4 alpha_1`,
  `(LM)^4 alpha_4`, and `(LM)^4 gamma_2` are bounded by an M-independent
  constant.

This is sufficient to identify the source location and parameter hierarchy,
but **not** the coordinate inequalities defining the domain or a numerical
inner/outer Cauchy collar.

## Fluctuation-coordinate facts that are source-extracted

CMP116 (2.5)-(2.6) gives the exact product-Gaussian interface after the
correlated fluctuation is conditioned/localized and the change of variables

`B' = (C^(k))^(1/2) X`.

The measure `dmu0(X)` is the standard product Gaussian over bond variables
`X(b)`, with one factor

`dX(b) exp(-|X(b)|^2/2)/(2*pi)^(dim(g)/2)`

per product coordinate. Thus the variable species and independence structure
are source-identified: the ultralocal fluctuation coordinates are bond-indexed
Lie-algebra variables `X(b)`; the nonlocal covariance/root dependence has been
moved into the integrand `G`.

CMP116 (2.7)-(2.10) then localizes that integrand by weakening parameters,
generalized random-walk expansions and a resolvent/series expansion of
`(C^(k))^(1/2)`. The resulting objects are `H(Z,Z0)` and `H(Z)`, with
component factorization in (2.10). The source also states that `H(Z)` is
localized in the interior of `Z` with respect to **external gauge fields**.

## What can and cannot be inferred for fluctuation support

The source-extracted data establish:

1. the Gaussian coordinates are `X(b)` bond variables;
2. localization pieces are assigned to connected M1-cube domains whose union
   is the final carrier `Z`;
3. the product measure factorizes over disjoint coordinate sets;
4. the localized activities have the source component factorization (2.10).

These facts make the natural project contract

`fluctuationSupport(H_Z) subset Bond(Z)`

(or the source-appropriate interior/enlarged-bond version) the correct **target
shape**. It is a conservative envelope, not a minimal-support equality.

However the current public extraction still does not print the exact mapping
from each random-walk/root term to the set of `X(b)` coordinates it uses.
Therefore the inclusion above remains a derived target awaiting the finite
source-domain dictionary; it is not promoted here to a source theorem.

In particular, do not import the scalar Dimock identity
`fluctuation support = X cap Lambda` into the four-dimensional gauge source.
That is architecture only, not the CMP116 dictionary.

## Cauchy-collar determination

R32 proved the following model-independent reduction: once the exact local
finite-range precision is identified, a real coercivity margin `m0>0` and a
local analytic perturbation estimate

`||A(U_c)-A(U_r)|| <= K_loc delta`

give a uniformly coercive complex subtube whenever

`delta <= m0/(2 K_loc)`.

R34 finds no source evidence contradicting a fixed collar. But the public
source packet does not contain the coordinate definition of
`U^c_{k+1}(X,alpha_0,alpha_1)`, so it cannot yet prove that the derived subtube
is contained in the source domain.

Thus the exact status is:

`source analytic domain LOCATED but DEFINITION-PENDING`;
`derived complex coercive subtube STRUCTURALLY AVAILABLE once definition is supplied`.

The definition-pending item is a provenance/dictionary gap, not evidence of an
analytic obstruction.

## Determination

R34 does **not** discover a new obstruction from the RP blocker or from the
covariance root. It narrows the remaining interface to two explicit source
records:

A. `CMP116ComplexDomainDefinition`
   - exact coordinate inequalities defining
     `U^c_{k+1}(X,alpha_0,alpha_1)`;
   - relation to the real admissible domain;
   - enough margin data to choose a fixed source-contained Cauchy/coercive
     subtube.

B. `CMP116FluctuationCarrierDictionary`
   - source M1-cube/bond convention for final `Z`;
   - exact carrier of `X(b)` variables in each localized `H(Z)` term;
   - component-factorization compatibility;
   - conservative inclusion into the project `fluctuationSupport` object.

No exact finite covariance-root decomposition is required. No minimal support
equality is required. External active support remains separately controlled by
R33's `supp_ext H(Z) subset IntBond(Z)` envelope.

## Negative results / guardrails

- Do not reconstruct `U^c_{k+1}(X,alpha_0,alpha_1)` from the notation alone.
- Do not call the scalar Dimock support convention the four-dimensional
  Yang-Mills convention.
- Do not identify component factorization with a minimal fluctuation-support
  equality without the source carrier map.
- Do not treat the absence of the private source artifact in the public corpus
  as a mathematical failure of Bałaban's construction.

## Next frontier — YM-R35

**Primary-source dictionary recovery / minimal closure contract.**

Instead of reopening the entire analytic argument, determine the minimum exact
source statements needed to instantiate A and B above. If the primary artifact
becomes available, transcribe the definition-level lines and close the
finite dictionaries. If it remains inaccessible, formulate the weakest
source-facing hypotheses that preserve all distinctions and test whether the
rest of the R28-R32 chain is already theorem-stable under those hypotheses.

## References

No new bibliography source is consumed. Existing [21], [32], [67], [69],
[76]-[79] and the external primary-source audit are reused. Highest source ID
remains [79]; next new source is [80].
