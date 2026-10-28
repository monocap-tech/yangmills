# YM-R147 — Composite constraint/pivot transport and physical-cutoff boundary layer

**Date:** 2026-10-28. **Committed predecessor:** YM-R146, main 183cba0. **Live cursor:** YM-R147. **Next:** YM-R148 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM. **Classification:** conditional exact linear-algebra derivation, source-shaped L=13 finite test, negative control and source-applicability audit. No continuum 4D Yang–Mills existence, OS construction or positive mass gap.

## 0. Source-facing question and custody

R142–R145 compared historical CMP95/CMP98 corner-anchored averaging to CMP109 Euclidean-symmetric centered averaging after the R120–R121 affine frame transport. R146 proved a *pivot exchange on a fixed constraint* but did not combine it with the *change of constraint*. This pass constructs the composite for one declared identity-background cell and writes the native source cutoff precisely in transported coordinates.

**Source images directly rechecked:** Bałaban, CMP109(2) (1987), original printed p.253 Eq.(0.4) in the third-party 54-page printed scan, PDF index 4; p.266 Eq.(2.9), PDF index 17; p.267 Eq.(2.11), source h and its support, PDF index 18; p.268 Eqs.(2.12)–(2.14), PDF index 19: https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf . Eq.(2.9) monitors all fluctuation bonds *except source b0(c)*, p.267 eliminates b0, and the Gaussian background normalizer and full nonlinear integral survive into the coarse action. Native R111–R112 already show the nonlinear constraint correction does not move the **source-monitored** components on the valid chart.

**Lower-custody historical source:** CMP95 (1.7)–(1.8), CMP98 (14)–(15), CMP99(3) (3.13)–(3.19),(3.155)–(3.158), via pinned third-party original-paper OCR and native R117–R121. CMP99 original (3.157)–(3.158) printed equation images and its precise hard-to-soft source precision remain unavailable. The *source-shaped* old derivative below is R120's declared old axial path transported to a common centered frame—not an attested complete CMP99 regional Gaussian-law identity.

## 1. General composite-transport lemma (proved abstractly)

Let D_o,D_n:H→Y be two surjective maps on the **same** finite-dimensional real bond-coordinate space, and let h_a:Y→H be a common right inverse with D_o h_a=D_n h_a=I. Let P_a delete the coordinate pivot a, with P_a h_a=0, and suppose ker D_o is uniquely parametrized by the graph embedding C_o^a satisfying D_o C_o^a=0 and P_a C_o^a=I. Let the new source pivot b be distinct, and C_n^b parametrizes ker D_n with D_n C_n^b=0 and P_b C_n^b=I. Assume the coordinate domains have the same dimension.

Define the **constraint shear** S=I−h_a(D_o−D_n). Because (D_o−D_n)h_a=0, S^{-1}=I+h_a(D_o−D_n), det S=1 and D_o S=D_n. Then

  **F=P_a C_n^b**, so **S C_n^b=C_o^a F**.              (R147.1)

Proof: D_o S C_n^b=D_n C_n^b=0, and P_a S C_n^b=P_a C_n^b since P_a h_a=0. Uniqueness of the graph C_o^a identifies the equality. If F is invertible, the old/new coordinate chart relationship is y=F x and **B_n=C_n^b F^{-1}y=S^{-1}C_o^a y**. The same physical CMP109 cutoff has the exact old-chart pullback

  **χ_n^{pull}(y)=χ_n(S^{-1}C_o^a y)**.                 (R147.2)

Not χ_n(C_o^a y), and definitely not an arbitrarily redefined box omitting pivot a. F must be proven invertible on the actual carrier; an abstract invertible S alone does not authorize identifying source independent-coordinate deletions in differing regional domains.

If H_o,H_n are any real symmetric quadratic forms on the common ambient bond space, the reduced precisions obey the exact *defect identity*:

  Q_n−F*Q_o F = (C_n^b)* [H_n−S*H_o S] C_n^b,        (R147.3)

where Q_i=(C_i)* H_i C_i. In particular, no Gaussian equality or determinant transfer follows just from det F=1: the transported Hessian defect must vanish or be quantitatively controlled.

## 2. One L=13 source-shaped sparse coefficient computation

Use R120's **declared common integer cell** {0,…,12}^4, common-frame old descending axial path with τ transports, and revised CMP109 (0.4) symmetric shortest permutations at identity. Select e1 interface-crossing fine bonds:
- a: transverse coordinate (0,0,0), old corner-line pivot;
- b: transverse coordinate (6,6,6), revised center-line pivot;
- w1,w2: any two other distinct interface-crossing bonds.
Let z denote R120's sparse positive e3 fine bond (0,1,0,0)→(0,1,1,0), in one fixed real su(2) color direction. Extend all other bond components by zero.

R143's bridge count gives the equal coarse-link coefficient κ=13/13⁴=1/2197 on a,b,w1,w2 in both averaged derivatives. Native R120's exact same-frame sparse computation gives the NEW-minus-OLD coefficient −ε on z, with ε=1/(4·13⁴)=1/114244. Therefore on this **declared five-bond test subspace only**, in common coarse-link normalization,

  D_o(a,b,w1,w2,z)=κ(a+b+w1+w2),
  D_n(a,b,w1,w2,z)=κ(a+b+w1+w2)−ε z,
  **t=ε/κ=1/52**.                                   (R147.4)

This is not the complete lattice operator, not an actual independent UV history pair, and not a full CMP99 multiscale constraint matrix.

The common old-pivot right inverse is h_a(s)=(s/κ,0,0,0,0). The constraint shear **S(a,b,w1,w2,z)=(a−t z,b,w1,w2,z)** takes ker D_n to ker D_o. Parametrize the new constraint by x=(a,w1,w2,z), deleting b; the old by y=(b,w1,w2,z), deleting a. Then

  **y=F x=(-a−w1−w2+t z,w1,w2,z)**,                 (R147.5)

with

  **F²=I, det F=−1, |det F|=1**                    (R147.6)

per real color; in all three su(2) colors the absolute determinant remains one. These identities were checked with exact rational matrix arithmetic, including S C_n^b=C_o^a F. A unit coordinate Jacobian is not an estimate for the full source field-dependent FP and nonlinear normalization.

## 3. New strict obstruction: curvature-sensitive constraint shear moves a MONITORED bond

Let θ>0 be a real scalar cutoff for the declared color-component model. In old coordinates y=(b,w1,w2,z), the **physical revised CMP109** deleted-b cutoff, after the complete transport, is

  χ_n^{pull}(y)
  = 1{|−b−w1−w2+t z|<θ}
    1{|w1|<θ,|w2|<θ,|z|<θ},                       (R147.7)

with further monitored-bond factors equal to one in this sparse test. If one incorrectly evaluates the cutoff on the old ambient representative C_o^a y *without* applying S^{-1}, the first factor becomes 1{|−b−w1−w2|<θ}. These are different **even when the same source pivot b is omitted in both expressions**. The distinction is not just R145's two different deleted-bond choices.

**Exact strict witness (θ=1):** y=(−207/208,0,0,1/2) gives old representative a_o=207/208 and physical new a_n=a_o+t/2=209/208. Hence both old/new coarse constraints hold on their respective transported fields, but χ_n(C_o^a y)=1 while χ_n(S^{-1}C_o^a y)=0. The numerical margins are 1/208 and are therefore strict (open stable) in the small finite model. Source nonlinear χ may have other restrictions outside the five-bond test, and actual global chart admissibility remains OPEN.

**Separate negative control:** at z=0 and y=(0,−3/5,−3/5,0)θ, physical new a=6/5 θ, while a hypothetical coordinate box that omits a accepts y; literal source b-deleted χ rejects. The latter comparison is ONLY with a hypothetical old-box event, not with a documented CMP99 χ.

## 4. Conditional quantitative boundary-layer consumer, not a native estimate

Write u=−b−w1−w2, d=t z. The physical event and a naively unshifted event differ only if an eligible u is within |d| of the scalar boundary ±θ. For a normalized nondegenerate Gaussian γ on y=(b,w1,w2,z), suppose Varγ(u | w1,w2,z)=σ²>0. Condition on w1,w2,z, including any shared restrictions |wi|,|z|<θ. The two intervals { |u|<θ } and { |u+d|<θ } have symmetric difference of total length at most 2|d|. A conditional Gaussian has maximum density 1/(sqrt(2π)σ), so

  **δ_γ:=γ(χ_n^{pull}≠χ_n^{naive})
      ≤min{1, 2|t| θ/(sqrt(2π)σ)}.**              (R147.8)

In the source-shaped test |t|=1/52, but **σ is not a source-certified covariance quantity**. This is a one-component finite Gaussian bound, not automatically an su(2) radial cutoff estimate. Additional monitored restrictions only decrease the symmetric-difference probability if they are the same in both events.

If a positive reference-weighted probability ν has density L=dν/dγ and K=Eγ[L²]<∞, then by Cauchy–Schwarz,

  ν(χ^{pull}≠χ^{naive}) ≤sqrt(K δ_γ).            (R147.9)

For both ν-event probabilities p,p'>0, their normalized conditioned laws have TV at most ν(A△A')/max(p,p') (exact common-part argument). These conditional consumers explain what a native source variance, likelihood-second-moment and partition lower bound would need to provide. **They do not prove any such source values**. If either cutoff has a zero normalizing mass, the conditional-law formula is not applicable.

## 5. Complete source measure interface and stopping point

For a genuinely native common reference chart, let f_o(y) be the *complete* old unnormalized density and f_n(x) the complete new one (including gauge/FP/Jacobian, Gaussian determinant normalization, inherited E, interaction and physical χ). If F is an admissible invertible chart map, exact change of variables gives

  f_n^{old}(y) = f_n(F^{-1}y)|det F^{-1}|.         (R147.10)

The normalized relative likelihood is [f_n(F^{-1}y)|det F^{-1}|/Z_n]/[f_o(y)/Z_o] wherever both are positive, with an explicit unmatched-support term otherwise. **Equation R147.10 is bookkeeping, not an established CMP99/CMP109 f_i identity.** In the finite test |det F|=1 but H_n−S*H_oS, actual old gauge selectors, nonlinear χ, FP and inherited action still lack native estimates.

**R147 closed:** conditional composite shear+pivot identity, exact L13 five-bond coefficient t=1/52, unit chart determinant, strict physical-cutoff counterexample even with a fixed deleted pivot, and conditional Gaussian cutoff-boundary consumer. [Exact rational certificate](../computations/YM_R147_COMPOSITE_TRANSPORT_RATIONAL_20261028.py). Original printed CMP109 images rechecked. **NOT CLOSED:** CMP99 nested Ω/Λ and precise old physical chart; real SU2 full covariance/conditional variance; nonlinear measure normalizers; relative two-UV inherited actions; OS and positive spectral mass gap.

**Next YM-R148, unconsumed:** on the actual CMP109 constrained Gaussian, identify the *monitored coordinate conditional variance for a source-local curvature-induced shift* and determine whether the region/collar and source determinant/interaction weights permit the boundary-layer estimate (R147.8–R147.9). Also require a source-exact common CMP99/CMP109 regional chart before claiming native law comparison. Do not initiate an abstract-only positivity or covariance detour.
