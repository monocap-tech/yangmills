# YM-R150 — append-only correction to YM-AUX-05 and source-projector retyping

**Date:** 2026-10-29. **Trigger:** actual user-provided original typeset CMP99 46-page PDF, SHA-256 `9904f303f01e2d267a0d138d4fc08d60742086d6557fc78bef6f2d25faeaad20`; visually inspected printed p.393–395, esp. **(3.21)–(3.25)**. See [primary image receipt](../source_receipts/YM_R150_CMP99_ORIGINAL_IMAGE_VERIFIED_20261029.md).

## 1. Source correction (HIGH IMPORTANCE, SOURCE-IMAGE FACT)

**FALSE PRIOR INTERPRETATION in [AUX-05](YM_AUX_05_PROJECTED_LANDAU_FLUX_DEFECT_AND_GAUGE_CARRIER_SPLIT_20261028.md):** `R = orthogonal projector onto ker Q'`. The mathematical PDF proves otherwise:

- `N(Q')={λ:Q'λ=0}` is a space of *site gauge transformations*.
- `Δ_U^η=D_U^*D_U` is the covariant site Laplacian, eq.(3.23).
- `R=Proj_{Δ_U^η N(Q')}` is the orthogonal projection in the **source site L² metric** onto the Laplacian **image** of that kernel, eqs.(3.20)–(3.22). The printed Δ was lost from the damaged third-party OCR; (3.25) supplies a nontrivial G'/Q' formula for R.

Hence even for U=1, *source* projected Landau `R D^*A=0` implies
```
<D^*A, Δ λ> = 0 for every λ∈ker Q'
⟺  Δ(D^*A) ∈ (ker Q')^⊥ = ran(Q'^*)   [finite dimensional, source-matched metric].
```
It does **NOT** imply `D^*A∈ran Q'^*`. At nonidentity U, use the correct covariant self-adjoint Δ_U and actual boundary domains/adjoints. The identity still does not force D^*A=0.

**Correct source-typed gate:** `R D^*A=0 iff D^*A ⟂ Δ_U(ker Q')`, or after adjointing, `Δ_U D^*A∈ran Q'^*` under the explicitly matching domain and metric. This is not the AUX-05 source-read formula.

## 2. Why AUX-05's exact finite countermodel does NOT test the true source R

AUX-05 constructed a declared orthogonal projector `R_model=Proj_{ker Q'_{site}}` and an exactly verified field with `f=D^*a=Q'^*_{site}λ`. Its logical statement is valid for **R_model**, but it was not a negative test of the actual historical source R.

In that **same** one-step centered block model, on periodic L=13, N=169, its f(x)=ρ(x₁) equals 0 at x₁=5,6 and 1/169 at x₁=7. Let Δ be the identity-background positive discrete site Laplacian and choose `ψ=δ_{(6,0)}−δ_{(5,0)}`, where 5 and 6 are in the *same* centered block, so `Q'_{site}ψ=0`. Then
```
Δ f(6,0)= 2 f(6,0)−f(5,0)−f(7,0)=−1/169
Δ f(5,0)=0
<f, Δ ψ>=<Δ f,ψ>=−1/169 ≠ 0.
```
Therefore f is NOT orthogonal to Δ ker Q' and `R_source-shaped f≠0`. The original field **fails** the corrected projected Landau test. All AUX-05 arithmetic assertions about its *declared different projection* remain valid; the inference about source gauge does not. Reproducible [exact check](../computations/YM_R150_AUX05_PROJECTION_COUNTERCHECK_20261029.py).

**Disposition:** explicit **CORRECTION / NON_TRANSFER** of the source comparison, not retroactive deletion of historical auxiliary files. AUX-04 ordinary-divergence flux theorem remains mathematically valid but source-admission still open. The prior AUX-05 phrase 'projected gauge + Dirichlet does not imply flux conservation' is a correct finite countermodel only for R_model, NOT proved for CMP99 source R.

## 3. Revised operator graph and next native gate

```
site λ ─Q'─→ averaged gauge λ'
  │
  └─Δ_U=D_U*D_U─→ Δ_U λ,  λ∈ker Q'
                      │
                      ▼
             ran R = Δ_U ker Q'
                      │ orthogonal condition
bond A ─D_U*─→ D_U* A ─┴→ source projected Landau
                 (not ordinary divergence)

separate bond B ─Q₁─→ 0, with B=C Bbar and actual regional support
                 │
                 ▼
            historical C*Δ_k C ≻ 0 (source hypotheses)

CMP109 exp-gauge A^(k) and source-valid C/domain
                 │
                 ▼
            native K=C* A^(k) C   [NOT YET CERTIFIED]
```

**SOURCE-IMAGE RECOVERED**, old source-access blocker lifted. Actual *new* blocker is source operator/domain **transfer**, not missing article images. Do not promote R150 or a numerical coercivity certificate until complete K, source-region and two R149 inverse solves have been verified.
