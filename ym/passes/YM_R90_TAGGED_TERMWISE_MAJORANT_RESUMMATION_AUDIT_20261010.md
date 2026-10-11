# YM-R90 — differentiated CMP116 single-term majorants / tagged resummation interface

Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior checkpoint: YM-R89 dafca6bb7db364e5086a3851a485625f681835bc
Status: COMPLETE AS CONDITIONAL TAGGED TRANSFER AUDIT; NATIVE TAGGED SOURCE THEOREM OPEN
Next cursor: YM-R91 (unconsumed)
Claim: UNPROVED RESEARCH PROGRAM; no continuum Yang-Mills or mass gap.

## 1. Source preflight and actual published endpoint

Earlier repository primary-source audits R50, R53, R54 are the controlling source custody:
- CMP116 Eq (2.14) is a term indexed by D/P/Z0/Z (plus weakening data) in the conditioned product-Gaussian representation.
- Eq (2.26) is its positive pre-resummation majorant, including D-activity factors, P-suppression, weakening decay and alpha5 volume correction.
- Eqs (2.27)-(2.37) perform the D/P/Z0/Z0' absolute estimates; Lemma 3/(2.38) gives the UNMARKED output |H(Z)|<=h exp[-lambda_H d_(k+1)(Z)], h=C3 epsilon1, lambda_H=((1-8delta)/2)L kappa.
- Eqs (2.39)-(2.41) expend a further positive exponent reserve to restore the next-scale effective-action bound, with lambda_eff=((1-10delta)/2)Lkappa.

New public source check reconfirmed the bibliographic record and abstract for Bałaban CMP116, which says the Part-I fluctuation integral is represented by an exponentiated cluster expansion, not that a two-cutoff tagged derivative is proved. The original CMP109 (5.37),(5.42),(0.29) page windows and purported per-root a_N^(4+alpha) bound were NOT directly verified here; [85] remains only secondary traceability. Existing references [7],[21],[59],[85],[87] reused, no new numbered source; highest [87].

Critical distinction: the source UNMARKED endpoint bound is not automatically an absolute positive bound on the collection of derivatives. A new marked term estimate, together with an absolute summation check, is necessary.

## 2. Frozen-localization tagged derivative is algebraically simple

Fix a finite source localization index family I_Z and operators L_(Z,i) linear in the source integrand G. Hold covariance, conditional Gaussian chart, cutoff functions, weakener, gauge coordinates, support indexing and all L_(Z,i) fixed as an insertion amplitude varies:
  H_Z(t)=sum_(i in I_Z) L_(Z,i)[G_t],
  G_t=G_0 exp[-sum_x t_x v_x].
If termwise differentiation is legitimate, then
  partial_(t_x) H_Z(t)
    =-sum_i L_(Z,i)[v_x G_t].
No independent Gaussian normalization/Jacobian derivative is created by varying an inserted potential inside the already-normalized source chart.

But the formula is ONLY for the frozen operator. In a full cross-cutoff comparison, C^(k), gauge/background/conditional support, cutoffs, source localization seed or the chart itself can change. For a moving linear operator L_t the correct derivative is
  partial_(t_x)[L_t(G_t)]
    =L_t(partial_(t_x)G_t)+(partial_(t_x)L_t)(G_t).
The second term includes any moving covariance/Green, measure, gauge, cutoff or source-index data and cannot be silently labeled an irrelevant V^(1) insertion. A changing discrete seed index also requires a common typed summation carrier before differentiating.

## 3. Tagged termwise domination transfers through ABSOLUTE resummation — ABSTRACT-DERIVED

Fix connected output Z and write d=d_(k+1)(Z), and v=pi_N(x) its marked cube. Suppose:
(A) a finite/common or absolutely convergent source index family I_Z and nonnegative absolute majorants M_i with sum_i M_i<=h exp(-lambda_H d), UNIFORMLY across all partial insertion environments;
(B) each differentiated source term has a separate TAGGED estimate
  |partial_(t_x) T_i(t)|<=C_ins u_x (1+d)^p exp[-sigma dist(v,Z)] M_i,
  with p>=0, sigma>0, C_ins independent of cutoff, volume and partial environment;
(C) the differentiated series is absolutely summable and termwise differentiation is justified.

Then by the triangle inequality and the source positive resummation majorant,
  |partial_(t_x)H_Z(t)|
   <=C_ins h u_x (1+d)^p exp[-lambda_H d-sigma dist(v,Z)].
For every 0<theta<lambda_H, set
  C_(p,theta)=sup_(s>=0)(1+s)^p exp(-theta s)<infinity
and lambda_tag=lambda_H-theta. Then
  |partial_(t_x)H_Z(t)|
   <=C_ins h C_(p,theta) u_x exp[-lambda_tag d-sigma dist(v,Z)].

If the native CMP116 localization geometry provides d>=c_M (|Z|-1) on the same source cube carrier, and tau(Z,v)=(|Z|-1)+dist(v,Z) on its unit-edge lattice hull, any
  0<mu<=min(lambda_tag c_M,sigma)
gives the R88/R89 tagged attachment bound
  |partial_(t_x)H_Z(t)|<=C_ins h C_(p,theta)u_x exp[-mu tau(Z,v)].
The condition theta<lambda_H-lambda_eff preserves a still-positive post-exponentiation reserve in this simplified bookkeeping; it must also satisfy the actual original parameter hierarchy.

This is a CONDITIONAL mathematical transfer, not an assertion that CMP116 (2.26) or (2.38) prints assumption (B). In some source operations differentiating a fresh insertion REPLACES an existing epsilon1 activity factor rather than multiplying it; then a bound proportional to h*u_x can be false. One must instead prove a separate marked absolute sum with prefactor C_tag u_x. The same polynomial/exponential argument applies after that new marked majorant is source-established. Do not infer extra epsilon1 smallness from differentiation.

## 4. Exact form of the remaining marked source audit

To promote R90 to native Yang-Mills, verify for each original CMP116 stage:
(1) D/Y0: a tagged inserted root lies in a source-owned connected seed; show the D-family Mayer/absolute bound survives with one marked activity and anchor attachment.
(2) P and Z0: all cutoff/P-bond factors, conditional Gaussian and normalization terms either remain frozen or their derivatives are explicitly controlled; count marked bonds/seed possibilities, not just unmarked P-subsets.
(3) Z0' and Z: prove tagged weakening/random-walk paths connect the mark to the final output Z and retain sigma>0 in the source metric, with one polynomial mark cost.
(4) Final Lemma 3: pass a POSITIVE marked majorant through the same D/P/Z0/Z0' resummation with strict rate reserve; the unmarked endpoint alone is insufficient.
(5) Cross-cutoff: identify the actual CMP109 first-layer V^(1) within G_t, scalar marginal and gauge/chart transport, and R/B/large-field channels; the model may require moving-L_t terms.

The stage-by-stage source pages for the new MARKED construction were not obtained. These remain new source-consumer hypotheses and cannot be reported closed from previously audited unmarked results.

## 5. Negative controls

(a) UNMARKED CONTROL DOES NOT CONTROL TAG DERIVATIVE. For u>0, let T_Z(t)=h exp(-lambda d(Z)) sin(t/u). It satisfies the unmarked real amplitude estimate at every t, but partial_t T_Z(0)=h exp(-lambda d)/u, not O(u). A uniform complex insertion-coordinate radius or direct derivative bound is missing. CMP116 analyticity in the background field U^c alone does not supply such an insertion-coordinate radius.

(b) FROZEN TAG ALONE DOES NOT CONTROL A MOVING COVARIANCE. For a one-dimensional normalized Gaussian with covariance C_t=1+t u and test integrand G(y)=y^2, the average E_{C_t}[G]=1+t u varies even with no inserted potential v_x. Its derivative comes from the moving Gaussian/covariance operator, not -v_x G. Thus a frozen-covariance tagged proof is insufficient for full cross-cutoff transport.

(c) MARKED SMALLNESS MAY REPLACE BASELINE ACTIVITY SMALLNESS. If a term contains an O(epsilon1) local factor and differentiation replaces it by v_x of size u_x, a bound O(epsilon1*u_x) is unwarranted without an additional source estimate. A direct C_tag u_x marked majorant is the correct weaker target.

## 6. Consequence and next cursor

ABSTRACT-DERIVED: algebraic frozen/moving localization derivative split; conditional positive-majorant tagged resummation; polynomial marked multiplicity absorbed by finite exponent spend; transfer to R88/R89 tagged tree bound given source metric identification.
PREVIOUS SOURCE-LOCATED: CMP116 (2.14),(2.26), D/P/Z0/Z0' unmarked resummations (R50-R54); R44/R45 bounded-support native insertion as conditional source use.
OPEN NATIVE: exact tagged single-term majorant and source mark ownership, differentiation/conditioning on the *moving* cross-cutoff chart, tagged D/P/Z0/Z0' resummation, uniform input admissibility over partial environments, CMP109 Eq(0.29) alpha and first-layer V^(1), marginal beta and R/B/measure sector matching.

YM-R91 (UNCONSUMED) should choose the weakest source-native marked proof target: a direct one-marked positive majorant at CMP116 (2.14)/(2.26), with no gratuitous h factor, or a tagged source activity-level response estimate already available from random-walk/localization machinery. Audit whether the derivative *replaces* an existing small factor and quantify any root-count/exponent loss. In parallel pursue the original CMP109 Eq(0.29) and first-common-scale coupled/large-field dictionary. No native R75 gate is closed.

No 4D continuum Yang-Mills existence, Osterwalder-Schrader reconstruction or mass gap is proved.
