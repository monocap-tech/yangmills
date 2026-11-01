# YM-R150 continuation — exact discrete curl, plaquette filling, and contour-defect covariance budget

**Date:** 2026-11-01. **Previous custody:** YM-R150 full one-row bridge cancellation PR #46, merged main 826140232626eed0cae997b6f75dbe29c17b479b. **Disposition:** EXACT COMBINATORIAL ONE-ROW DERIVATION; CONDITIONAL HISTORICAL COVARIANCE CONSUMER; POSITIVITY TRANSFER STILL OPEN. **Native YM-R150 IN PROGRESS / UNCONSUMED; YM-R149 remains canonical completed checkpoint.** The four-dimensional continuum YM construction, OS reconstruction and positive mass gap are UNPROVED.

## 0. Source boundaries

Primary user-provided printed CMP99 (1985), pp428 (3.155)–(3.158) and 432 Theorem 3.15 (3.185)–(3.187) establish an exponentially decaying **historical** constrained propagator on its actual admissible regular Ω/Λ domain under source hypotheses. Theorems are NOT asserted for arbitrarily selected source-shaped fine-edge Gaussian carriers. Printed CMP109 (1987) p253 (0.4) describes symmetric shortest-path coarse-link averaging. The historical comparator is the selected descending contour from CMP98 (15) / CMP95 (1.7), previously recovered by original-paper third-party OCR, with explicit R120 endpoint-frame transports. A verified original CMP98 mathematical page image was not recovered here.

Everything computed below uses the **declared one-step aligned identity-background unrestricted cell**: L=13, old corner y=(0,0,0,0), new center s=(6,6,6,6), identical physical fine bridge and source-shaped path conventions. It is not the full CMP99 nested nonlinear Q_j(U), gauge-supported regional Ω/Λ, or 1987 full source K. This distinction remains essential.

## 1. Correct discrete Hodge type: the defect is an exact 1-cycle

Let D_n,D_o denote the previously audited entire first derivative ROW of one revised/historical coarse e1 bond. Set Δ=D_n−D_o. Each D is represented as a finite rational linear functional on positively oriented fine edges, and its explicit old/new gauge endpoint transport ensures that for each fine pure gradient dφ, D_n(dφ)=D_o(dφ). Thus

    Δ(dφ)=0 for every finitely supported site φ,     (R150.P1)

equivalently the oriented edge chain j=Δ* has discrete boundary ∂j=0 (no source). In a general periodic region a divergence-free 1-cycle need NOT be a plaquette boundary: there may be harmonic/winding components. The current declared two-block graph is contained in the contractible rectangular subset x1=0,...,25; x2,x3,x4=0,...,12, with **no periodic wrap**. On THIS patch an explicit plaquette 2-chain S is constructed with

    ∂S=j,     Δ[B]=〈S, d_1 B〉                    (R150.P2)

for all fine bond cochains B, where d_1 is the oriented discrete plaquette curl and ∂=d_1*. This is an exact *abelian first-variation* Stokes identity, not a claim about finite non-Abelian holonomies or source gauge-fixed stochastic curvature.

**Constructive proof:** choose origin root 0 and an ascending-coordinate axial site path P(u) from 0 to each endpoint u. For positive edge e=(u,u+e_mu), the loop P(u)+e−P(u+e_mu) is the negative sum of elementary (mu,nu)-plaquette boundaries obtained by commuting e left across subsequent coordinate-axis segments nu>mu. Since the coefficient chain j has zero divergence, its P(u) terms cancel globally, giving the explicit cone filling. The exact certificate constructs this S by summing those plaquettes, then recomputes ∂S and checks every oriented edge coefficient equal to j. This is stronger than inferring "curl-like" solely from gauge covariance.

## 2. Verified full 13^4-site exact rational results

[Independent complete coefficient-and-filling certificate](../computations/YM_R150_CONTOUR_DEFECT_DISCRETE_CURL_20261101.py) uses integer accumulators with common denominator 24 L^4, all fine site endpoints and all distinct shortest-axis permutations. It retains the historical descending path and tau transports, checks the bridge and sparse z coefficient, computes ∂j, constructs the axial-cone plaquette chain S, verifies ∂S=j exactly, and returns:

| Property | Exact result |
|---|---|
| revised D_n supported positive edges | 213109 |
| old selected D_o supported positive edges | 32959 |
| Δ supported edges | 210912 |
| interface bridge discrepancies, 2197 crossings | 0 |
| nonzero coefficients of ∂Δ* | 0 |
| nonzero plaquettes of S | 153792 |
| number of erroneous edges in ∂S−Δ* | 0 |

Let κ=1/L³=1/2197, t=1/52, and define the *normalized* gauge-invariant edge chain j_κ=Δ*/κ, using the declared unit-fine-bond counting Hilbert metric. The exact rational sizes are

    ||j_κ||_1 = 2803036/13 ≈ 215618.153846;          (R150.P3)
    ||j_κ||_2² = 523953742/3 ≈ 174651247.333333.    (R150.P4)

The coefficient at the special off-bridge R120 z bond is j_κ(z)=−1/52. Therefore the second R149 corrected defect j_u=j_κ+t e_z (with that z coefficient cancelled) has

    ||j_u||_2² = 1416770918365/8112
               ≈ 174651247.332964.                  (R150.P5)

The *particular* axial cone S (not an area-minimal filling) obeys

    ||S/κ||_1 = 20342037/13 ≈ 1564772.076923,
    ||S/κ||_2² = 3568504628/3 ≈ 1189501542.667. (R150.P6)

These large values directly refute the tempting inference "no bridge component implies a short, small-norm contour defect." The bounds concern the declared row, not RG-depth-uniform source tensors. The exact cone is an existence certificate, not a minimal-area claim or a sharp bound.

## 3. What can be consumed from historical covariance (and what cannot)

If—and ONLY if—the declared j_κ were transported into the **same** legally admitted historical constrained bond Gaussian carrier with covariance Σ_o satisfying CMP99 Theorem 3.15 in the same normalized Hilbert metric, the historical source bound from preceding R150 custody gives ||Σ_o||<=M_hist (symbolic; depends on unknown B0,δ0). Then

    d_a² = 〈j_κ,Σ_o j_κ〉
        <= (523953742/3) M_hist,                      (R150.P7)
    d_u² = 〈j_u,Σ_o j_u〉
        <= (1416770918365/8112) M_hist.              (R150.P8)

These **finite but enormous** upper bounds do not prove d_a or d_u small and cannot establish an R149 rare-exit probability. The complete source Ω/gauge/Hilbert identification and actual Σ_o contraction remain OPEN. Importantly, a covariance with exponential decay is not by itself an *extra smallness* statement in the specific direction j_κ. As an abstract NON-NATIVE countermodel, Σ=I on the unrestricted edge carrier has perfect off-diagonal decay yet d_a²=523953742/3. It does **not** satisfy the historical constrained Gaussian hypotheses and is not a refutation of the true CMP99 theorem.

The Stokes factorization offers an alternative exact variance representation whenever the covariance is defined on this carrier:

    d_a² = κ^(-2)〈S, d_1 Σ_o d_1* S〉.             (R150.P9)

A useful native bound therefore needs control of the *source plaquette-curvature covariance* d_1 Σ_o d_1*, and/or a better source-compatible filling/weighted curl cancellation. The printed CMP99 Theorem 3.15 bound on Σ_o alone gives only the coarse symbolic R150.P7, not a small contraction. Simply substituting a bound on d_1 Σ_o d_1* multiplied by this nonminimal huge S also need not help.

**Critical further qualification:** j_u=j_κ+t e_z is not gauge-closed (a single edge has nonzero boundary), so the curvature-only identity (R150.P9) applies to j_κ, not automatically to j_u. In the second physical observable the isolated z contribution has been removed but the resulting cochain is not necessarily a closed cycle. Keep the R149 variance directions distinct.

## 4. Complete constrained-Hessian transfer is still separate

No step here computes actual CMP99→CMP109 multilevel regional chart F or establishes

    ||(F* K_o F)^(-1/2)(K_n−F* K_o F)(F* K_o F)^(-1/2)|| <= rho < 1.

The divergence cancellation is a first-order gauge/geometry identity; it does not prove the two source actions, gauge-fixing functionals or multiplier-weighted constraint jets agree at second order. A nonzero second jet can disappear at identity J=0 while remaining active at nonidentity source backgrounds. Neither the historical covariance bound nor exact \partial S=j transfers a source numerical positive lower bound for K_n.

## 5. Typed determination and next source gate

**CLOSED IN DECLARED FINITE MODEL:** entire one-row difference, discrete divergence-free condition, constructive exact 153792-plaquette filling, exact normalized defect norms, explicit finite historical-covariance consumer.

**NEGATIVE:** zero bridge coefficients does not imply small contour-defect variance from historical exponential covariance alone; raw and curl norms are large, and generic M_hist bounds are not decisive.

**OPEN NATIVE:** original/source-compatible gauge/Dirichlet Ω and multiscale Q_j on common paired carrier; contraction of historical Σ_o against *this* full defect or tighter curl-covariance/random-walk mechanism; valid transported F and complete Hessian rho; positive interaction W, normalized cutoff masses and independent UV histories; continuum OS and positive mass gap.

**Next bounded YM-R150 pass, still unconsumed:** prioritize a source-specific mechanism to reduce the defect via **historical constraint projection** and the CMP99 random-walk resolvent/covariance, not another ambient-edge norm. Explicitly test whether j_κ has a nontrivial projection annihilated by the source hard constraint/gauge and whether the surviving transverse component has a source-bound weighted norm. In parallel identify the actual common Ω and complete relative Hessian. If no such source projection can be recovered, mark an explicit source obstruction instead of claiming that exact curl form delivers smallness.
