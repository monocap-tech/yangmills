# YM-AUX-05 — Projected Landau flux defect and three-way source-carrier split

**Date:** 2026-10-28. **Predecessor:** merged YM-AUX-04 main `5033189a5f9b5cce6511af59c737f4362a4c349f`. **Classification:** lower-custody original-paper transcription audit; exact finite-dimensional projected-gauge theorem; executed exact-arithmetic, single-scale identity-background *countermodel*; precisely typed non-transfer. **Native YM-R149 last completed; YM-R150 UNCONSUMED/SOURCE_DATA_HOLD.** Not a proof or refutation of 4D continuum Yang–Mills or the positive physical mass gap.

## 0. Target and critical source correction

AUX-04's exact flux theorem assumed **ordinary divergence-free** `div a=0` and a zero-normal-flux slice. Its CMP99 admission inquiry then noticed Dirichlet support, but did not establish the **actual gauge operator**. The CMP99 original-paper OCR reveals a strictly different historical **projected Landau** gauge condition `\mathcal R D^*A=0`, not `D^*A=0`. There is ALSO a separate `Q_1B=0` **bond-averaging** constraint in the unit-lattice Gaussian, with an excluded-bond reconstruction `B=C\bar B`. These three equations occupy distinct mathematical types and need not be imposed on the same field before their source map is identified.

**Strict evidence:** Bałaban, *Propagators for lattice gauge theories in a background field*, CMP 99 (1985) 389–434, DOI `10.1007/BF01240355`; ORIGINAL PAPER, THIRD-PARTY OCR only, immutable `ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743` in `chboishabba/dashi_agda`, `Docs/support/reference/balaban-source-extracts/cmp99-background-propagators.txt`, printed pp.393–395,427–431. Text: (3.17)–(3.21) defines `Q'` on **site gauge transformations** and `\mathcal R` as the orthogonal projection onto `N(Q')=ker Q'`; (3.26) builds a gauge-regularized operator with a projected-gradient term; near (3.178) the manuscript explicitly applies `\mathcal R D^*A=0` as the Landau gauge in the transformed integral. Separately (3.155)–(3.159), on printed pp.427–429, restricts **bond** Gaussian fields to Dirichlet support and `Q_1 B=0` and parametrizes the excluded bonds through `C`.

OCR has damaged mathematical superscripts, original printed page-image equations are NOT recovered; no assertion here that CMP99 `Q_1` equals the later CMP109 `DM_{109}`, or that these three fields are identical. The new mathematical identities below follow from **declared** finite Hilbert operators, not from source numerical K.

## 1. Exact projected-gauge carrier identity (DERIVATION)

Let `G` be finite-dimensional real site-gauge Hilbert space, `H` a bond Hilbert space, `D:G→H` a discrete derivative with adjoint `D^*:H→G`, and `Q':G→F` an arbitrary linear site gauge averaging map. Let `\mathcal R` be the orthogonal projection onto `ker Q'`. In finite dimension,

`(ker Q')^⊥=ran(Q'^*)`,

so

`BOXED: \mathcal R D^* a=0 \iff D^*a \in ran(Q'^*).`  (AUX05.1)

This is **strictly weaker** than `D^*a=0` unless `ran(Q'^*)` intersects `ran D^*` trivially in the actual field domain. No such disjointness follows from CMP99's OCR.

On a periodic oriented site lattice with `D^*a(x)=Σ_μ[a_μ(x-e_μ)-a_μ(x)]`, define the positive-axis normal flux `Φ_μ(s)=Σ_{x_⊥}a_μ(s,x_⊥)`. The transverse differences telescope, giving

`Φ_μ(s)-Φ_μ(s-1)=-Σ_{x_⊥}D^*a(s,x_⊥)`. (AUX05.2)

For a projected-Landau field choose `λ∈F` with `D^*a=Q'^*λ` (exists by AUX05.1). Let `1_s` be the indicator of the complete normal slice `x_μ=s`. Then

`BOXED: Φ_μ(s)-Φ_μ(s-1)= -\langle Q'1_s,λ\rangle_F.` (AUX05.3)

This is the *exact missing source-admission interface*. AUX-04's conservation follows when **ordinary** `D^*a=0`, or under the alternative **verified source-specific** annihilation `\langle Q'1_s,λ\rangle=0` at every s. A single zero-flux slice alone does not force all others zero under projected Landau gauge.

The formula uses the Hilbert adjoint appropriate to the actual source metric. It must not be specialized to source `Q'` or `\mathcal R` until their block layers, gauge fields, domains and scalar products are verified.

## 2. Exact source-shaped one-scale countermodel WITH Dirichlet zero-extension (NEGATIVE CONTROL)

Use L=13, N=L²=169, on the 2D torus. The **identity-background single-step site-gauge block-average model**, inspired by CMP99 (3.19) but not claimed to be its full multiscale regional Q', is

`(Q'_{site}f)(y)=L^{-2} Σ_{n∈[-6,6]^2} f(y+n)` on coarse sites `y∈(LZ/NZ)^2`.

Its adjoint is `(Q'^*_{site}λ)(x)=L^{-2} λ(y(x))`, where `y(x)` is the unique centered coarse block containing x. Set coarse λ=+1 on **all transverse coarse origins** with normal coordinate 13, λ=−1 for normal origin 26, and λ=0 elsewhere. Then the site density `ρ=Q'^*_{site}λ` is +1/169 on normal fine slices 7..19, −1/169 on 20..32, and zero elsewhere.

Define a real positive-axis bond field

`a_1(s,t)=-Σ_{u=0}^{s}ρ(u,t),\quad a_2=0`

using the ordinary linear ordering s=0,...,168, which defines a periodic bond field because Σ_{s=0}^{168}ρ(s,t)=0. It satisfies

`D^*a=ρ=Q'^*_{site}λ`, hence `\mathcal R D^*a=0` for `\mathcal R=\mathrm{Proj}_{ker Q'_{site}}`,

**at every fine site**, yet `D^*a\ne0`. Its support is **strictly contained** in the normal strip `7≤s≤31`; it vanishes at **every** bond outside that strip (Dirichlet zero extension). The normal flux at s=0 equals 0, while `Φ_1(19)=−13`. Its mean over the 25-slice support strip is `−1/25`, and mean over the full torus is `−1/169`.

`BOXED: projected-Landau + proper Dirichlet support + zero flux slice DOES NOT imply conserved or zero normal flux.` (AUX05.4)

The [standalone standard-library Fraction certificate](../computations/YM_AUX_05_PROJECTED_GAUGE_DIRICHLET_RATIONAL_20261028.py), executed locally, asserts all N²=28,561 identities, support, flux values, block adjoint identity, and exact means; [run output](../computations/YM_AUX_05_RATIONAL_RUN_LOG_20261028.txt).

**Critical limitation:** This model does **not** satisfy or claim the independent CMP99 Gaussian `Q_1B=0` bond-averaging constraint, and does not instantiate `C`, `A^{(k)}`, admissible Ω/Λ/Dirichlet collars, full source site `Q'`, or the fields transformed between (3.155) and (3.178). It is a precise logical countermodel to using *two* conditions (projected gauge + Dirichlet) as if they implied ordinary divergence; NOT a native source admissibility obstruction or negative energy vector. The two-dimensional countermodel extends to extra passive directions, but we make no claim of a 4D complete source verification.

## 3. Correct source obligation graph: THREE carriers, then K

1. **Bond blocking:** source CMP99 `Q_1 B=0` on restricted supported **bond** Gaussian field, `B=C\bar B` reconstructing one special bond per coarse link; its exact Q1, admissible A and boundary scope remain source-image pending. It is not the site Q'.
2. **Projected Landau:** source historical transformed **bond** variable A satisfies `\mathcal R D^* A=0`, with `\mathcal R` onto `ker Q'_{site}` on site gauges. Need reconstruct transformations (3.159)–(3.183) and source Hilbert metrics before pulling a flux property back to Gaussian B.
3. **Ordinary co-closed:** `D^*a=0` is the strictly stronger AUX-04 abstract theorem hypothesis. It is neither visibly a printed gauge condition nor a consequence of Dirichlet restriction alone.
4. **Actual precision:** source positive `C^*Δ_k C` is separately discussed near CMP99 (3.158), but CMP109 exponential-gauge `K=C^*A^{(k)}C` requires original symbolic and domain comparison, not a positivity-label transfer.

**Decision:** AUX-04 remains a correct theorem on its explicitly declared co-closed zero-flux domain, but its suggested *source* admission route must be marked **NOT YET LICENSED**. Any direct path `CMP99 projected Landau + Dirichlet ⇒ AUX04 flux conservation` is false in the independently certified one-scale model. The source-specific missing criterion is the expression `\langle Q'1_s,λ\rangle`, **together with** the actual `Q_1B=0` constraint and source transformations. This is a type correction, not a contradiction of the original paper.

## 4. Stopping point

**CLOSED:** finite projector-range characterization AUX05.1; exact projected-gauge flux defect AUX05.3; one-step Dirichlet model counterexample AUX05.4. **SOURCE TEXT FOUND, LOWER CUSTODY:** source projected gauge, site vs bond averages, Dirichlet restrictions. **OPEN:** original CMP99 printed pp.393–395 and pp.427–432 equation images; genuine region/collar and Q1/Q' domains; source relationship between A and B; actual native K/coercivity; FP, weights, partitions, two-UV normalized laws; continuum OS and positive physical mass gap.

**YM-R150 REMAINS UNCONSUMED under SOURCE_DATA_HOLD**, machine checkpoint YM-R149 unchanged. No new YM-R151; do not proliferate synthetic boundary examples before native Q1/Q' and source image reconciliation.
