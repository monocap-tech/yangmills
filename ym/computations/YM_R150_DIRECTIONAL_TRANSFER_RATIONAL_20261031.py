#!/usr/bin/env python3
"""YM-R150 exact rational R147 five-bond dual transport.
The one-step F is source-shaped but NOT a verified full CMP99/CMP109 chart.
"""
from fractions import Fraction as Q
t=Q(1,52)
F=[[Q(-1),Q(-1),Q(-1),t],[Q(0),Q(1),Q(0),Q(0)],
   [Q(0),Q(0),Q(1),Q(0)],[Q(0),Q(0),Q(0),Q(1)]]
I=[[Q(int(i==j)) for j in range(4)] for i in range(4)]
assert [[sum(F[i][k]*F[k][j] for k in range(4)) for j in range(4)] for i in range(4)]==I
def tvec(A,v):
    return [sum(A[j][i]*v[j] for j in range(4)) for i in range(4)]
wa=[Q(1),Q(0),Q(0),Q(0)]
wu=[Q(1),Q(0),Q(0),-t]
va=tvec(F,wa); vu=tvec(F,wu) # F^{-T}=F^T since F^2=I
assert va==[-1,-1,-1,t] and vu==[-1,-1,-1,0]
assert (sum(map(abs,va)),sum(map(abs,vu)))==(Q(157,52),Q(3))
assert (sum(x*x for x in va),sum(x*x for x in vu))==(Q(3)+t*t,Q(3))
# Completely synthetic Ko=I4 and E=-(1/4)F^T F only:
rho=Q(1,4)
actual=[sum(x*x for x in v)/(1-rho) for v in (va,vu)]
ell1=[sum(abs(x) for x in v)**2/(1-rho) for v in (va,vu)]
assert all(a<=b for a,b in zip(actual,ell1))
print("PASS: exact dual directions, t cancellation, symbolic conditional variance sanity check")
print("synthetic exact variances:",actual,"synthetic B*=1 bounds:",ell1)
print("NATIVE SOURCE F, Ko, relative form rho and full regional cutoff remain OPEN")
