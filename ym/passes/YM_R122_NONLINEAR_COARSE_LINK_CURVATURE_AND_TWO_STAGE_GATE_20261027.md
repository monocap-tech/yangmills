# YM-R122 — Nonlinear CMP109 coarse-link curvature certificate

**Date:** 2026-10-27. **Predecessor:** [YM-R121](../checkpoints/YM_HEAD_R121_20261027.json), main 533cd94474e2c7614c6b8403d58cf4f045532b30. **Completed:** exact source-shaped nonlinear real-SU(2) single-link and deterministic two-stage M-composition bounds, under explicit stringent local curvature and full-halo hypotheses. **Not completed:** source-indicator applicability, regional Ω/Dirichlet cutoff control, actual two-independent-UV normalized probability law, covariance, OS or mass gap. **Next:** YM-R123 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Source boundary
T. Bałaban, CMP109 (1987), published original printed p.252–253, (0.3),(0.4), visually inspected in third-party [54-page printed scan](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), zero-based PDF indices 3,4. (0.3) defines centered L-block and all shortest coordinate-order permutation paths. (0.4) DEFINES the actual nonlinear full coarse link as the exponential of uniformly averaged logarithms of loops relative to straight fine lift U(c), followed by multiplication by U(c). We take the equivalent skew-Hermitian SU2 Lie-algebra convention, absorbing the printed i factor:
\[
 M(U,c)=\exp(\mathbb E_{x,\Gamma,\Gamma'}\log X_{x,\Gamma,\Gamma'})\,U(c),\quad
 X=U(\Gamma)U([x,x'])U(\Gamma')^{-1}U(c)^{-1}. \tag{R122.1}
\]
x is uniform on L^4 centered fine sites. Gamma and Gamma' are independently uniform among shortest-axis permutations from coarse endpoints y,y' to x,x'=x+Le1. U(c) is source fine path of coarse bond length L, not an independent group variable. For real SU2 only; NO assertion for complexified source fields.

**Source geometry gate:** to build all plaquette homotopies, require every used bond/plaquette in an eligible real source field region. A sufficient halo for y=0, c parallel e1 is the coordinate box \([-r,L+r]\times[-r,r]^3\) in fine units, r=(L-1)/2. Full periodic tori admit lifts of these paths if periods are compatible; for restricted Ω/Λ/Dirichlet regions the required halo/cutoff coverage is NOT source certified. This is a derived sufficient set, not a claimed printed Bałaban collar condition.

## 1. Exact source-weighted ribbon count
For n=x-y with each coordinate in [-r,r], choose descending 4,3,2,1 as canonical at both endpoints. Swapping each pair of transverse/longitudinal coordinate runs to canonical creates \(|n_i n_j|\) elementary plaquette swaps per inverted unordered axis pair (i,j). The canonical closed link ribbon differs from straight e1 transport by L strips of \(|n_j|\) plaquettes in each transverse direction j=2,3,4. Thus a source-permitted path pair has an explicit homotopy requiring at most
\[
 N(n,\pi,\pi')=
 L\sum_{j=2}^{4}|n_j|+
 \sum_{1\le i<j\le4}|n_i n_j|
 (I_\pi(i,j)+I_{\pi'}(i,j)). \tag{R122.2}
\]
I is 1 when that pair is reversed relative to canonical descending axis order; missing/zero axes contribute zero. This counts an explicit homotopy, not the minimal area.

At L=13, r=6:
\[
 \boxed{N\le 13\cdot3\cdot6+2\cdot6\cdot6^2=666.}\tag{R122.3}
\]
For uniformly weighted x and independently uniform shortest permutations, each pair is inverted at each endpoint with probability 1/2. Since E|n_i|=42/13 and E|n_i n_j|=(42/13)^2,
\[
 \boxed{\mathbb EN=13\cdot3(42/13)+6(42/13)^2
 =126+10584/169=31878/169.}\tag{R122.4}
\]
This mean is for the constructed homotopy counts, not minimal two-chain area. [Independent exact certificate](../computations/YM_R122_NONLINEAR_RIBBON_AND_TWO_STAGE_20261027.py) evaluates all 28561 sites with rational arithmetic.

## 2. Exact nonlinear source M-to-fine holonomy theorem
Define \(\eta=\sup_{p\subset\text{eligible halo}}\|U(\partial p)-I\|_{\rm op}\) for real SU2. Every elementary swap replaces a subpath by another across one plaquette; unitary outer factors preserve operator norm. Consequently,
\[
 \|X_{x,\Gamma,\Gamma'}-I\|\le N\eta\le666\eta. \tag{R122.5}
\]
**Theorem R122.6 (conditional)**: if the full halo is eligible and **666η<1**, then the actual source (0.4) satisfies
\[
 \boxed{\|M(U,c)-U(c)\|_{\rm op}\le
 (31878/169)\,\eta/(1-666\eta).}\tag{R122.6}
\]
Proof: all X lie in the norm-one matrix-log disk around I. The power series gives \(\|\log X\|\le \|X-I\|/(1-\|X-I\|)\le N\eta/(1-666\eta)\). Hence \(Y=\mathbb E\log X\) obeys \(\|Y\|\le(\mathbb EN)\eta/(1-666\eta)\). Since all real SU2 principal logarithms here are skew-Hermitian, Y is skew-Hermitian and \(\|\exp Y-I\|\le\|Y\|\) by integration along the unitary one-parameter path. Multiplying by U(c) preserves norm. QED. This is a full NONLINEAR source M estimate, not a first variation or a normalized RG probability law. At η=0, M(U,c)=U(c). The numerical chart threshold is an independently proved sufficient condition, NOT the actual source indicator threshold or a source-verified uniform-in-cutoff estimate.

## 3. True deterministic TWO-STAGE M map — not a UV measure law
On compatible nested CENTERED periodic lattices with complete halos, let \(U_1=M(U_0)\), \(U_2=M(U_1)\), where each M is the actual source nonlinear (0.4) evaluated at its own lattice scale (no stochastic integration). Define \(C=31878/169\) and for all necessary fine plaquettes let η0 be the uniform plaquette deviation. Set
\[
 \delta_0=C\eta_0/(1-666\eta_0),\qquad
 \widehat\eta_1=L^2\eta_0+4\delta_0.\tag{R122.7}
\]
Replacing four U1 coarse plaquette edges by straight fine U0 lifts costs ≤4δ0 (unitary product telescoping). The resulting L-by-L fine plaquette boundary differs from I by ≤L²η0 (nonabelian tiling into elementary plaquettes). Thus the coarse elementary curvature η1 obeys
\[
 \boxed{\eta_1\le\widehat\eta_1.}\tag{R122.8}
\]
If 666η0<1 and **666\widehatη1<1**, apply R122.6 at the second scale, and replace each of L scale-1 straight links on the scale-2 straight path with its fine lift at cost Lδ0. This proves
\[
 \boxed{
 \|M(M(U_0),c_2)-U_0(c_{2,\mathrm{fine\ straight}})\|
 \le L\delta_0+C\widehat\eta_1/(1-666\widehat\eta_1),\quad L=13.
 }\tag{R122.9}
\]
The nested centered coarse sites lie on all finer centered lattices because L is odd, so straight axis bond lifts compose exactly. **Do not add R121's 2808 corner-center axial τ cocycle to R122.9**: it is a DIFFERENT historical-frame comparison. This two-stage result is an actual deterministic M-composition estimate but does NOT compare two independent UV cutoffs, impose the same prescribed Ω/V, or control Jacobians, Faddeev–Popov factors, Gaussian fluctuations, inherited E and determinant normalization. It is generally weak/growing, NOT a renormalization contraction. All fine/coarse required halos must lie in their respective source domains.

## 4. Stop and successor
| Native gate | Result |
|---|---|
| Printed CMP109 full nonlinear M (0.4) | VISUALLY VERIFIED |
| Real SU2 L13 homotopy maximum/mean | EXACT 666 / 31878/169 |
| One-step actual nonlinear M vs fine U(c) | PROVED CONDITIONALLY, R122.6 |
| Two-stage actual deterministic M(M(U)) | PROVED CONDITIONALLY, R122.9 |
| Actual Bałaban indicator/Ω collar controls 666η<1 | OPEN |
| CMP99 nested Q' and late A_k/Delta_k precision | OPEN |
| Paired independent UV Ω,V normalized measures, OS/mass gap | OPEN / UNPROVED |

**YM-R123 unconsumed:** inspect source small-field indicators (0.17),(0.19),(2.9) and source regional Ω/collar to determine whether the required fine and coarse HALO η conditions actually follow; if not, precisely obstruct. Only then connect deterministic M to R110 Gaussian cutoff-exit/normalization and the independent two-UV laws. Separately recover original CMP99 (3.157)–(3.158). No continuum Yang–Mills proof.

Historical cumulative bibliography [92] unchanged; previous checkpoint append-only.
