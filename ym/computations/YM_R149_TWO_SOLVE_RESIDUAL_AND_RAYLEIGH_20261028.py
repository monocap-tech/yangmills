#!/usr/bin/env python3
"""YM-R149 rational synthetic certificate; A_test=I is NOT CMP109."""
from fractions import Fraction as F
from math import sqrt, pi, erfc, exp
t=F(1,52)
C=[[F(1),F(0),F(0),F(0)],[-1,-1,-1,t],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
K=[[sum(r[i]*r[j] for r in C) for j in range(4)] for i in range(4)]
def dot(a,b): return sum(u*v for u,v in zip(a,b))
def mv(M,v): return [dot(r,v) for r in M]
def inv(A):
 n=len(A)
 B=[[F(q) for q in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
 for i in range(n):
  p=next(j for j in range(i,n) if B[j][i])
  B[i],B[p]=B[p],B[i];a=B[i][i];B[i]=[z/a for z in B[i]]
  for j in range(n):
   if j!=i:
    a=B[j][i];B[j]=[u-a*v for u,v in zip(B[j],B[i])]
 return [r[n:] for r in B]
S=inv(K)
assert [[dot(K[i],[S[j][l] for j in range(4)]) for l in range(4)] for i in range(4)] == [[F(i==j) for j in range(4)] for i in range(4)]
alpha=1/max(sum(abs(u) for u in row) for row in S)
assert alpha>0
for v,expected in [([F(1),F(0),F(0),F(0)],F(8113,10817)),([F(1),F(0),F(0),-t],F(8115,10817))]:
 sol=mv(S,v)
 exact=dot(v,sol)
 assert exact==expected
 h=[F(round(float(x)*1000),1000) for x in sol]
 residual=[x-y for x,y in zip(v,mv(K,h))]
 lower=2*dot(v,h)-dot(h,mv(K,h))
 upper=lower+dot(residual,residual)/alpha
 assert 0<=lower<=exact<=upper
 print('exact variance',exact,'residual enclosure',lower,upper)
Q3=lambda z:erfc(z/sqrt(2))+sqrt(2/pi)*z*exp(-z*z/2)
for T in (3,4,6):
 old=Q3(T)+Q3(T/(1+float(t)))
 new=Q3(T)+Q3(T/sqrt(1+float(t*t)))
 assert 0<new<old
 print('T sqrt(alpha)',T,'old',old,'direct Rayleigh',new)
print('PASS: R149 rational synthetic two-solve/Rayleigh check. NATIVE K OPEN.')
