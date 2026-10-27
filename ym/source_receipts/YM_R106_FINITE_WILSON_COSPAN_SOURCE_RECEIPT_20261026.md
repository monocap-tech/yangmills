# YM-R106 — source and self-contained finite-Wilson test receipt

Date: 2026-10-26. [Native R106 pass](../passes/YM_R106_FINITE_WILSON_OBSERVABLE_COSPAN_COUPLING_CUTSET_20261026.md). Evidence classes: directly verified previous R105 repository checkpoint; paper bibliographic metadata/abstract; explicit elementary finite-Wilson gauge/measure calculations; standard-Borel abstract maximal-coupling lemma. No original publisher image equations checked.

## Provenance

- Native R105 pass/receipt/checkpoint: [pass](../passes/YM_R105_PAIRED_VARIATIONAL_CARRIER_LAW_SEPARATION_20261026.md), [receipt](YM_R105_PAIRED_CARRIER_SOURCE_RECEIPT_20261026.md), [checkpoint](../checkpoints/YM_HEAD_R105_20261026.json).
- Earlier exact scale algebra: [R75](../passes/YM_R75_BETA_INDEX_SEMANTICS_PHYSICAL_SCALE_STATIONARITY_20260922.md).
- Bałaban, *Averaging operations for lattice gauge theories*, CMP 98(1) (1985), 17–51, DOI https://doi.org/10.1007/BF01211042. Bibliographic abstract supports existence/study of gauge-field averaging maps; **NOT** a formula-level check that a Wilson edge-perimeter product equals Bałaban \(M\).
- Bałaban, *The variational problem and background fields in renormalization group method for lattice gauge theories*, CMP 102(2) (1985), 277–309, DOI https://doi.org/10.1007/BF01229381. Peer-reviewed abstract: fixed averages and minimizer unique modulo gauge under its hypotheses; original averaging/variational formula-image checks **OPEN**.
- Sussman–Alpöge YM4 Part III at commit af96f9c5ec6d05a5c8f251256d87970d73b7f25a, raw blob 6012ff578fb1c67c29651f1f4192ab59a4c862a3: paired input III:34655–34735, candidate relative minimizer III:35626–35641, covariance/root III:36675–36807, explicit gaps III:37398–37443, 37533–37560, 111209–111275. **External unrefereed conditional draft**, not a verified theorem. Locations were independently captured in [R105 receipt](YM_R105_PAIRED_CARRIER_SOURCE_RECEIPT_20261026.md); R106 does not claim new Part III source-line reinspection.
- CMP109 original equation images (0.29), (5.37), (5.42), CMP102b original averaging/minimizer images, and CMP99 background equations: **OPEN**. No new primary source numbered reference claimed.

## Directly checked independent reasoning

1. SU(2) Wilson loop target [-1,1]: normalized half-trace of SU(2) element; a closed-loop holonomy conjugates under local lattice gauge transformations, so the trace is gauge invariant.
2. At \(\eta_N=L^{-N}\), a physical square of side \(L^j\eta_N\) is traced by \(L^j\) microscopic edges per side at depth N and \(L^{j+1}\) per side at depth N+1. This is physical *contour* equality, not equality of microscopic links or source block averages.
3. Compact finite-volume product Haar with continuous, finite, strictly positive Wilson density yields finite \(0<Z_N<\infty\), and gives positive probability to each nonempty open set. Near \(-I\) plaquette holonomy yields a nonempty open complement to the proper small-field event for \(0<\epsilon<2\).
4. Maximal coupling of the data pushforward laws and standard-Borel disintegration proves the exact best diagonal matching probability \(1-\mathrm{TV}\); no statement about the actual native prescribed-data distributions is made.
5. Conditioning proves \(|E_{\mu_i}F_i-E_{\mu_i|G_i}F_i|\le 2\|F_i\|_\infty \mu_i(G_i^c)\), hence R106.1 and the fully conditional R106.2.

## Refusals

Do not identify an elementary Wilson-loop contour with Bałaban CMP98's nonlinear \(M\); do not promote a shared observable target to matching determining-set \(V\); do not use a matched-data coupling with unmatched cutoff law marginals; do not drop large-field complements or pretend their probabilities are summable. The finite SU(2) test is **not** the full compact-simple-group target, and no physical limit/mass gap result is claimed.
