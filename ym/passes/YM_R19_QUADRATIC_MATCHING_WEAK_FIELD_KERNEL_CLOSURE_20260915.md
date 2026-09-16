# YM-R19 — quadratic matching / weak-field kernel closure

Date: 2026-09-15
Status: COMPLETE
Next cursor: YM-R20

## Target

Compare the linearized/quadratic Bałaban gauge RG with the reflection-adapted soft matrix-kernel proposal from YM-R18. Determine whether the soft kernel lies in the same Gaussian operator class, how its coarse quadratic action differs from hard block averaging, how gauge modes and reflection support behave, and what nonlinear remainder remains to be controlled.

## Source-attested structural input

Bałaban's free/vector-field analysis treats lattice gauge theory as a perturbation of a Gaussian vector field. The multiscale continuation is developed in Propagators and renormalization transformations for lattice gauge theories I–II. Modern Balaban-style notes write the linear gauge block average explicitly as

(QA)(y,y+Le_mu) = sum_{x in B(y)} L^{-4} A(Gamma_{x,x+Le_mu}),

with Q(A-d lambda)=Q(A)-d(Q lambda), and define the hard RG density by delta(A_k-Q_k A). In covariant gauge the Gaussian minimizer is controlled by

G_k(a) = (M_k + a Q_k^T Q_k)^{-1},

where M_k denotes the gauge-fixed quadratic operator (in the cited exposition M_k = delta d + d R_k delta), and

H_k(a)=G_k(a) Q_k^T (Q_k G_k(a) Q_k^T)^{-1}.

Random-walk/exponential-decay estimates are developed for this operator family. The Q_k^T Q_k term is explicitly described as providing an effective mass for the propagator; this is a technical gauge-fixed propagator mass, not the physical Yang–Mills mass gap.

## Linearized kernel

Choose the soft coarse-link kernel from YM-R18 with path/weight geometry selected so its matrix-valued block observable Qmat_e(U) has the same linearization as Bałaban's Q:

U = exp(g A),  V = exp(g B),

Qmat_e(U) = c_e I + g c_e (Q A)_e + O(g^2).

For the normalized matrix-Fisher-type kernel

k_e(dV|U) proportional to exp[ beta kappa ReTr(V Qmat_e(U)^dagger) ] dV_Haar,

with beta proportional to g^{-2}, the normalized weak-field expansion has conditional quadratic term

( a / 2 ) || B - Q A ||^2,

where a>0 is a scale-independent constant determined by kappa, normalization conventions, representation normalization and c_e. Pure U-dependent terms at quadratic order are removed by the link-kernel normalization; field-dependence of the radial part contributes only to higher-order/local corrections after the leading conditional Gaussian is isolated.

Thus the quadratic fine-field Hessian is

M + a Q^T Q.

This is exactly the operator family already present in the Bałaban Gaussian analysis.

## Hard versus soft Gaussian RG

Work on the gauge-fixed subspace where M is invertible (or interpret inverses on the corresponding quotient). Define

C = Q M^{-1} Q^T.

### Hard constraint

The hard block transformation with QA=B gives

H_infty = M^{-1} Q^T C^{-1},

Delta_infty = C^{-1},

S_eff,hard(B) = (1/2) <B, Delta_infty B>.

The hard constrained fluctuation covariance is

C_fluc,infty = M^{-1} - M^{-1}Q^T C^{-1} Q M^{-1}.

### Soft kernel

For

S(A;B) = (1/2)<A,M A> + (a/2)||B-QA||^2,

let

G_a = (M+aQ^TQ)^{-1}.

Gaussian integration gives the conditional mean

H_a B = a G_a Q^T B
          = M^{-1}Q^T (C+a^{-1}I)^{-1} B,

and the effective coarse Hessian

Delta_a = aI - a^2 Q G_a Q^T
        = (C+a^{-1}I)^{-1}.

Equivalently, the soft transformation adds independent local covariance a^{-1}I to the hard coarse covariance:

C_soft = C_hard + a^{-1} I.

As a -> infinity,

H_a -> H_infty,
Delta_a -> Delta_infty,
G_a -> C_fluc,infty.

## Key correction to YM-R18

YM-R18 said that fixed kappa automatically becomes a hard block constraint as beta -> infinity. That statement is true only in unrescaled group coordinates: both fine fields and kernel width shrink like O(g).

In canonically rescaled weak fields U=exp(gA), V=exp(gB), fixed kappa gives a finite a and therefore a finite conditional Gaussian width. It does NOT converge to the hard delta constraint merely because g -> 0.

Therefore:

- exact recovery of Bałaban's hard block map requires a -> infinity (equivalently an additional hardening limit), or
- one treats the soft map as a different RG scheme and proves its induction directly.

This correction is canonical.

## Why fixed-a softening may still be admissible

Although Delta_a != Delta_infty, their difference is explicit:

Delta_a = Delta_infty (I + a^{-1} Delta_infty)^{-1},

so

Delta_a - Delta_infty
= -a^{-1} Delta_infty^2 (I+a^{-1}Delta_infty)^{-1}.

For a massless gauge kinetic operator, Delta_infty behaves like p^2 at small momentum. Hence

Delta_a(p) = p^2 - a^{-1} p^4 + higher powers,

schematically.

Thus softening preserves the leading p^2 kinetic term and produces a higher-derivative correction. In RG language the quadratic mismatch is a candidate irrelevant operator rather than a generated mass term.

This is the most important positive result of R19: quadratic matching succeeds up to an explicit higher-derivative correction.

## Gauge-zero-mode custody

The linear averaging satisfies

Q d = d Q_0.

Hence the joint soft penalty ||B-QA||^2 is invariant under simultaneous linearized gauge transformations

A -> A-d lambda,
B -> B-d(Q_0 lambda).

The Q^TQ contribution in G_a therefore does not constitute a physical Proca mass. It regularizes the gauge-fixed fluctuation propagator. Gauge fixing / quotienting remains necessary exactly as in the hard construction.

## Reflection support at the linear level

For a reflection-aligned block decomposition, Bałaban/Dimock's straight-path formula for Q can be chosen so a coarse link lying strictly in the positive half-space uses only fine bonds in that half-space. Spatial links inside a positive block and temporal links not crossing the reflection plane satisfy the required support property directly. Reflection-plane/boundary variables must be assigned to the neutral boundary algebra rather than the positive algebra.

Therefore the linearized Q does not itself obstruct the conditional half-space factorization needed by the RP soft kernel.

## Nonlinear remainder

After writing U=exp(gA), V=exp(gB), beta~g^{-2}, analyticity of finite products and traces gives

-log k(B|A)
= (a/2)||B-QA||^2 + g R_3(A,B) + g^2 R_4(A,B)+...,

on a fixed regular weak-field domain, with R_j finite-range gauge-covariant analytic local functions determined by the chosen path family.

Thus the first nonlinear correction has the perturbative size expected in a weak-coupling constructive expansion. However this alone does not prove Bałaban-norm closure. One must still control:

1. all analytic derivatives required by the effective-action norm;
2. polymer localization after integrating the soft Gaussian fluctuation;
3. large-field characteristic functions / complete-density bookkeeping;
4. scale-uniform constants;
5. the extra quadratic irrelevant operator Delta_a-Delta_infty.

## Determination

Quadratic obstruction: NOT FOUND.

The soft RP-compatible kernel linearizes to the same Q and produces the same fine-field propagator family M+aQ^TQ already present in Bałaban's Gaussian machinery. The only leading difference from hard averaging is the explicit coarse Hessian

Delta_a=(Q M^{-1}Q^T + a^{-1}I)^{-1},

whose mismatch from the hard Hessian is higher derivative at low momentum.

The remaining interface is therefore not the Hessian itself but an inductive-norm theorem:

- prove the quadratic higher-derivative correction has the required RG scaling gain and quasi-locality;
- prove the normalized kernel's cubic-and-higher terms satisfy Bałaban's analytic/polymer bounds under iteration.

## Next frontier — YM-R20

Title: irrelevant-remainder / inductive-norm audit.

Target the explicit operator

E_a := Delta_a-Delta_infty

and the nonlinear local remainder R_g. Determine their scaling dimensions and whether one RG step maps them into the irrelevant/polymer sector with a strict contraction factor. The highest leverage question is whether the soft blocking modification can be absorbed into the existing irrelevant interaction E_k rather than requiring a new principal action at every scale.
