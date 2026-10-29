# YM-R150 — CMP99→CMP109 source-exact reduced-precision crosswalk and transfer-seam audit

**Date:** 2026-10-29. **Parent:** `a42a785397770ab41de4ecf0325a3114e4806470` (original CMP99 source-image custody). **Type:** original-image/source attestation and conditional algebraic operator comparison. **Native YM-R150 IN PROGRESS/UNCONSUMED**; this is not a completed numbered pass, native numerical K, or physical mass-gap result. **Source scan:** user-provided original-typeset CMP99 46-page PDF SHA256 `9904f303f01e2d267a0d138d4fc08d60742086d6557fc78bef6f2d25faeaad20`; scanned printed pages 420,421,427,428,429,431,432 visually rechecked. PDF itself NOT redistributed in GitHub. **Comparator:** CMP109 original printed pp.265–268, public original scan https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf, PDF indices 16–19 directly inspected.

## 0. Question

Can the original CMP99 **positive historical** reduced precision `C_old* Δ_k C_old >= γ0 I` be transferred directly to CMP109's **exponential-gauge** reduced precision `K_new=C_new* A^(k) C_new`? The source explicitly connects the two papers, but its gauge, coarse observable, support and independent carrier must be reconciled before assigning `γ0` to `K_new`.

## 1. Original source equations — typed without substitution

**Historical CMP99, p.427 (3.155):** unit-lattice source Gaussian on supported bonds B in Λ, with hard `δ(Q₁B)` and regional support `δ_Λ(B)`. Its exponent includes the variational inverse and second-order correction, not merely a free lattice Laplacian.

**Historical CMP99, p.428 (3.156):** quadratic form `q_old(B):=<B,Δ_k B>` equals
```
q_old(B)=<B,(Q G₁ Q*)^(-1) B> - a(B,B)
          - 2 <H₁ D̃^(2)(B),J>.
```
Here B is an admitted **coarse bond** source variable. This formula inherits the article's k-dependent domains, background, Hilbert products, H₁ and G₁ from the original gauge-fixed variational construction. It must not be read as an identity on unrestricted arbitrary bonds.

**p.428 (3.157)–(3.158):** after deleting one special b₀(c) per coarse link, `B=C_old b`, where independent b parameterize `ker Q₁` on the stated regional support. The independently parameterized Gaussian precision is `K_old=C_old* Δ_k C_old`, covariance `K_old^(-1)`, and covariance on the full constrained B-space is `C_old K_old^(-1) C_old*`. The source explicitly states a lower bound `γ0>0`, independent of k and U **under its regularity/smallness conditions**, on this historical K_old; no numerical γ0, actual finite L13 matrix or CMP109 transfer is printed.

**CMP109 p.266 (2.5):** Landau-gauge fixing has `G(B)=1/2 G^(2)(B)+G₃(B)`, where `G^(2)(B)` is an explicit **sum of squared norms of a linearized site-link gauge function**. Thus `G^(2)(B)>=0` on the **CMP109 source field B**, an immediate source-derived quadratic nonnegativity, not a claim on the reduced K's net difference.

**CMP109 p.267 (2.11):** after the nonlinear constraint-linearizing reparameterization `B'=B-h D̃(B)`, the order-zero exponent is
```
-1/2 G^(2)(B) -1/2 <H₁ B,Δ₁ H₁ B>
 + <H₁ h C̃^(2)(B),J>.
```
Therefore the new quadratic `q_new(B):=<B,A^(k) B>` at this stage is
```
q_new(B)=G^(2)(B)+<H₁ B,Δ₁ H₁ B>
         -2<H₁ h C̃^(2)(B),J>.
```
**Actual text:** the paragraph immediately after (2.11) refers directly to **CMP99 (3.156)**, with its `δ`-gauge-fixing term replaced by an exponential. CMP109 p.268 (2.12) states covariance in independent variables as `(C_new* A^(k) C_new)^(-1)` and includes nonlinear Jacobian, σ, interaction and partition normalization. The new C_new is specified by the **current background V^(k)** after nonlinear chart linearization and special b₀ links; a source admissible equality `C_new=C_old` has NOT been established.

## 2. An exact formal mismatch ledger (DERIVATION, CONDITIONAL SAME-CARRIER)

**Only after** constructing a shared admissible B-space, matching scalings/metric, backgrounds and charts, and matching the two H₁ operators, the literal difference of the two *source-shaped* quadratic expressions is
```
q_new(B) - q_old(B) = G^(2)(B) + E_var(B) + E_jet(B),

E_var(B)=<H₁B, Δ₁ H₁B>
         -<B,(QG₁Q*)^(-1)B> + a(B,B),

E_jet(B)= -2<H₁(h C̃^(2)(B)-D̃^(2)(B)),J>.
```
This is an **algebraic comparison**, not a certified operator equality; outside a shared source jurisdiction even this expression is a comparison *request*, not a legitimate subtraction. Here the old `D̃^(2)` and new `h C̃^(2)` arise from **different nonlinear linearization descriptions**; they are not equated by typography.

There is a promising **variational cancellation interface**. CMP99 p.421, (3.128)–(3.129), states `H₁B=G₁Q*(QG₁Q*)^(-1)B` for a gauge-restricted minimizer. Consequently on exactly this same carrier/metric,
```
<H₁B,G₁^(-1)H₁B>=<B,(QG₁Q*)^(-1)B>.
```
CMP99 (3.128) relates `G₁^(-1)` to the underlying quadratic action, gauge term `||RD*A||²`, and bond average penalty `a||QA||²`. Since `RD*H₁ B=0`, `QH₁B=B`, **an appropriate source identification of Δ₁ as the gauge-restricted action term** can force `E_var=0`. This is a *conditional* cancellation, not an independently proved identification of CMP109's `Δ₁` with the historical term. Need compare precise definition, source gauge `R=Proj_{Δ_U ker Q'}`, and the actual H₁ plus its source χ/Λ regions.

If `E_var=E_jet=0` **and** `C_new=C_old=C` on the same Hilbert carrier, then
```
K_new - K_old = C*G^(2)C >= 0,
```
and the historical `γ0` bound would imply `K_new>=γ0 I` **on that same normalized metric and within its source hypotheses**. **None of the italicized equality preconditions is yet discharged.** Do not assert this order or a numeric α as a result of source quotation alone. An alternative sufficient route is a rigorously quantified lower bound on all non-gauge residual terms compared with γ0.

This is the exact **promotion condition** for the positivity idea; it replaces an unjustified direct transfer.

## 3. Critical CMP99 (3.185)–(3.186) covariance correction (SOURCE-IMAGE FACT + ALGEBRA)

Original printed p.432 (3.185) is
```
C^(k)(Λ) = (I + D̃ μ) Q G̃₂ Q* (I+ μ* D̃*).
```
**The exterior coarse observable is un-tilded Q on BOTH sides**, not the constraint's `Q̃`. It is also not a bare transformed G̃₂. The preceding R150 source receipt accidentally **omitted the left Q** and its shorthand could imply a wrong operator type. This pass corrects the earlier receipt append-only.

Source (3.186) introduces the **different** operator `Q̃`, defining the hard-constrained propagator
```
G̃₂ = G₂ - G₂ Q̃*(Q̃ G₂ Q̃*)^(-1) Q̃ G₂,
```
where G₂ is the exponential-gauge Gaussian covariance in the same auxiliary A-field domain. Thus
```
Q̃ G̃₂ = 0,     G̃₂ Q̃* = 0
```
by direct multiplication, assuming the indicated inverse exists. If (3.185) used `Q̃` in place of **Q** on both sides, it would yield zero covariance, contradicting the generally nonzero (3.158) source propagator. The **two averages must be kept distinct**. This exact annihilation check is mathematical evidence of the source's typed relation and why the older transcription was dangerous.

Eq.(3.185) is a covariance **of transformed coarse observables** after the actual historical hard-to-exponential-gauge **change of variables and source transform**; it is NOT proof that `K_old` and a later `K_new` coincide. Eq.(3.186) is a Gaussian conditioning identity, not a source-free coercivity certificate for the CMP109 exponential fluctuation.

## 4. Disposition and exact next requirements

**Closed this audit:** original CMP99/CMP109 printed expressions directly compared; formal three-term mismatch decomposed with explicit positivity of source `G^(2)`; historical H₁ variational identity recovered; missing **Q versus Q̃** in (3.185) fixed; exact constraint-covariance annihilation established.

**OPEN:** source-source equality of Δ₁/H₁ and the old/new quadratic measure, `h C̃^(2)=D̃^(2)` on same region/scale (or bounded discrepancy), source gauge and Dirichlet collar matching, `C_new=C_old` on source independent bonds, actual finite eligible L13 ambient source K and numerical γ0 or another α, source cutoff/θ and normalization, R149's two native inverse directional solves, independent two UV laws, continuum OS and positive physical mass gap.

**STOP:** YM-R150 source crosswalk remains **IN PROGRESS, UNCONSUMED**; no synthetic matrix to fill the domain or numeric K. Do not promote historical lower bound to new exponential-gauge precision without `E_var,E_jet` and C/metric closure. The outcome is a source-specific transfer checklist and exact typed identity, not an automatic positivity proof.
