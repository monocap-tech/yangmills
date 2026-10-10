# YM-R82 — covariance-first crosswalk and normalized Gaussian interpolation

Date: 2026-10-10
Prior checkpoint: YM-R81, 5a4e9377094b04664859f4201d9235c0f5780f6e
Status: ABSTRACT THEOREM/AUDIT COMPLETE; NATIVE GATES OPEN
Next cursor: YM-R83

## Source recovery: previous YM-R42/R43 is load-bearing

The earlier repository source audits already extracted Bałaban CMP116 [21] (2.5)–(2.7): the one-step conditioned fluctuation integral is rewritten using B'=(C^(k))^(1/2)X against normalized product Gaussian dmu_0(X). The covariance root is then localized via random-walk/resolvent machinery. CMP116 continues the CMP109 Part-I fluctuation integral. R43 records that the source's product Gaussian normalization already handles the Jacobian of this internal transformation; an additional project transport/pushforward theorem is not automatically proved.

R42 explicitly demoted literal CMP102 Delta_1 = CMP99 Delta_a identification from the covariance-root critical path. The two operators remain a valid precision-provenance side question, but the CMP116 source covariance chart can be used directly if its own definitions and cross-cutoff transport are verified. Prior CMP99 [79] decay is source-located in R32; exact CMP99-to-CMP116 covariance identity remains open. Original CMP109 (5.37),(5.42),(0.29) and CMP102 first Delta_1 definition were NOT retrieved as equation-readable pages here. Reference IDs [7],[21],[41],[77],[79],[85],[86] are reused; no new source.

## Exact finite normalized Gaussian identity — ABSTRACT-DERIVED

On a common finite real Hilbert carrier let b be external real background parameters, C_i(b)>0 covariance matrices, V_i(b,y) sufficiently smooth/integrable real interactions, and
  Z_i(b)=E_{Y~N(0,C_i(b))}[exp(-V_i(b,Y))]>0.
Assume all interchange of derivatives and expectations below is justified.

Write DeltaC=C1-C0, DeltaV=V1-V0, C_t=C0+t DeltaC, V_s=V0+s DeltaV. For tilted expectation E_{C,V}^tilt[F]=E_C[F exp(-V)]/Z(C,V), the Gaussian differentiation identity gives
  d_t log Z(C_t,V1) =
     (1/2)sum_ab DeltaC_ab E_{C_t,V1}^tilt[
          (partial_ya V1)(partial_yb V1)-partial_ya partial_yb V1].
Also d_s log Z(C0,V_s)=-E_{C0,V_s}^tilt[DeltaV].

Therefore the EXACT two-channel comparison is
  log Z1-log Z0
   = (1/2)int_0^1 dt sum_ab DeltaC_ab L_(t,ab)
     - int_0^1 ds E_{C0,V_s}^tilt[DeltaV],
  L_(t,ab)=E_{C_t,V1}^tilt[(d_a V1)(d_b V1)-d_ab V1].

No extra independent Gaussian determinant term belongs in this NORMALIZED measure identity. A source effective action written E_i(b)=K_i(b)-log Z_i(b) has an additional deterministic DeltaK channel containing whatever bare/localization/gauge/chart terms the source actually prescribes.

For external coordinates b_mu,b_nu the covariance channel's mixed derivative is
 (1/2)int dt sum_ab [
 (d_munu DeltaC_ab)L_ab+(d_mu DeltaC_ab)(d_nu L_ab)
 +(d_nu DeltaC_ab)(d_mu L_ab)+DeltaC_ab(d_munu L_ab)].
The interaction and K channels must also be differentiated and bounded; none disappears just because both covariances decay.

If sup_a sum_b |d^alpha DeltaC_ab|<=eps_alpha and sup_(a,b,t)|d^beta L_ab|<=M_beta for alpha,beta=0,mu,nu,munu, then with fluctuation dimension m,
  (1/m)|d_munu Delta logZ|_cov
  <= (1/2)[eps_munu M0+eps_mu Mnu+eps_nu Mmu+eps0 M_munu].
This is a DENSITY estimate, not the spatially weighted second-moment locality required by YM-R77. To use it for native beta extraction requires source identification, localized response kernels, uniform chart/volume normalization, and the interaction/DeltaK estimates.

## Exact orthogonal chart transport — ABSTRACT-DERIVED

If U(b) is orthogonal and C1(b)=U C0 U*, V1(b,y)=V0(b,U*y), with external test directions matched, Gaussian pushforward gives Z1(b)=Z0(b) for every b. Thus their external derivatives agree even if the raw matrices differ by order one. Example: C0=diag(1,2), U a swap; raw ||C1-C0||=1 but the transported partition functions coincide. Nonorthogonal transport requires its correct measure Jacobian; differing cutoff dimensions require an actual conditional-shell comparison, not an invented U.

NEGATIVE CONTROLS: (i) C0=C1=I, V0=0, V1=lambda b_mu b_nu (constant in y) gives mixed derivative of log(Z1/Z0) equal -lambda, despite zero covariance difference. (ii) Two fixed, different exponentially localized covariances at all UV depths give a nonsummable aligned covariance difference despite individual decay.

## Evidence conclusion and YM-R83

PREVIOUS SOURCE-LOCATED: CMP116 product Gaussian/root chart (R42/R43); CMP99 propagator decay (R32). ABSTRACT-DERIVED: Gaussian covariance/potential interpolation, mixed-density bound, chart invariance and negative controls.

OPEN NATIVE: exact CMP109/CMP116 source C,V,K, conditioning/gauge chart, physical scale identification, full beta projection and weighted second moment; CMP99 covariance normalization link; CMP109 (0.29) original positive-alpha polymer bound and one-layer correspondence; P2M Schur Lean proof URI [86].

YM-R83 (unconsumed): identify actual source fluctuation covariance, interacting activity and counterterms on the native CMP116 chart, then seek uniformly summable *localized* covariance-response and interaction/counterterm changes in the full source polarization, independent of the still-open CMP102 precision side record. Seek original CMP109 equations (5.37),(5.42),(0.29) without promoting secondary [85].

No continuum Yang-Mills, OS reconstruction, or positive mass-gap claim. Highest reference [86], next [87].
