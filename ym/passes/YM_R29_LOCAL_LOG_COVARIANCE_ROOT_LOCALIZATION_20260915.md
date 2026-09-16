# YM-R29 — local-log / covariance-root localization

Date: 2026-09-15
Status: COMPLETE
Next cursor: YM-R30 (native root-localization / source-dictionary audit), UNCONSUMED
Claim status: research reduction only; no 4d Yang–Mills construction or mass-gap proof claimed.

## Entry

YM-R28 reduced the RP-compatible blocker to a bounded-support analytic small-field proof coordinate

`V_soft = log(1 + E_soft)`

with analytic norm `O(g_k)`. The only remaining question introduced by the blocker was whether substituting the CMP116 covariance-root variable spreads this local term into an activity with the same exponential polymer geometry as Bałaban's native localized terms.

## Source architecture

CMP116 (2.5)-(2.6) moves the correlated fluctuation Gaussian to the product Gaussian by `B' = (C^(k))^(1/2) X`. The expression remains global through the covariance root and propagator data. CMP116 (2.7)-(2.10) then introduces weakening parameters, generalized random-walk expansions and a resolvent/series expansion of `(C^(k))^(1/2)`, producing localized activities `H(Z,Z0)` and `H(Z)`. Later estimates culminate in Lemma 3 / (2.38).

The existing source audit correctly keeps `covariance_root_certificate` and `root_localization` as separate obligations: the latter is not an exact finite root-piece identity; the source uses an infinite/resummed generalized random-walk localization.

## Stability lemma for the new local term

Let `S` be the fixed finite block support of `V_soft`, and suppose the covariance root has a source-compatible localized expansion with exponentially summable pieces,

`R = (C^(k))^(1/2)`,

`R = sum_Y R_Y`,

with a weighted kernel bound schematically

`||R_Y|| <= A exp(-mu d(Y,S))`

and the standard summability/overlap conditions used by the generalized random-walk expansion.

Assume on the fixed complex tube

`||D^n V_soft|| <= C_n g_k`

for the finite derivative orders used by the localization argument. Introduce the same weakening variables `s_Y` multiplying root pieces and expand/telescope in them. A contribution assigned to a connected localization domain `Z` contains enough root pieces to connect the base support `S` to the excursions comprising `Z`. Cauchy bounds contribute only fixed constants while the product of root weights contributes exponential distance decay. Tree/polymer summation therefore gives, after a finite loss in exponent,

`|V_soft(Z)| <= C'_soft g_k exp(-mu' d_k(Z))`,

for any `mu'` below the source root-decay margin, with `C'_soft` independent of the UV step once the weak-coupling ceiling and analytic tube are fixed.

The Gaussian change of variables does not cost a negative power of `g_k`: the source-side random variable is canonically normalized and the soft local activity already has `O(g_k)` analytic derivatives. Gaussian moments/Cauchy estimates contribute scale-uniform constants. Hence root localization preserves the coupling power `g_k`.

## Main determination

The RP-compatible blocker introduces no new type of nonlocality. Its only long-range dependence after the product-Gaussian change is through the same covariance root already present in Bałaban's native integrand. Therefore, conditional on the native CMP116 covariance-root/root-localization package, the new local term automatically belongs to the same exponentially localized activity class with amplitude `O(g_k)`.

Combining YM-R28 then yields

`|H_new(Z)| <= C3 (epsilon1 + C_soft' g_k) exp(-c' d_{k+1}(Z))`,

with only a finite decay-margin loss attributable to the same root localization. The scalar D/P/resummation constants need no new mechanism.

## Negative result / custody boundary

This does NOT discharge the native covariance-root source theorem itself. The project source audit still records as open the exact dictionary from Balaban's generalized random-walk/resolvent expansion of `(C^(k))^(1/2)` to a theorem carrying explicit support/enlargement conventions and uniform root-weight constants. R29 shows only that the new RP blocker does not enlarge that obligation.

Do not replace the source's infinite/resummed root expansion by a fictitious finite exact root-piece decomposition.

## Consequence

The UV modification branch has now collapsed onto a pre-existing Bałaban obligation:

`RP blocker -> O(g_k) local analytic factor -> native covariance-root localization -> existing CMP116 activity chain`.

No independent blocker-specific localization theorem remains once the native root package is available.

## Next frontier

YM-R30 — native root-localization / source-dictionary audit.

Extract the actual CMP116/CMP95-96 root kernel/resolvent/random-walk bounds sufficiently sharply to determine whether the covariance-root certificate and root-localization field can themselves be closed with scale-uniform constants. This is now a native Bałaban-source problem rather than an RP-kernel problem.

References reused: cumulative [21] Bałaban CMP116; [32]/[67] Bałaban propagator/RG papers; no new source number consumed.