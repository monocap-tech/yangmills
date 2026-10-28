#!/usr/bin/env python3
"""YM-R148 exact rational certificate; A_test=I is SYNTHETIC, not CMP109."""
from fractions import Fraction as F
from math import sqrt, pi, exp, erfc
t=F(1,52)
assert F(1,4*13**4)/F(1,13**3)==t
C=[[F(1),0,0,0],[-1,-1,-1,t],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
K=[[sum(r[i]*r[j] for r in C) for j in range(4)] for i in range(4)]
def inverse(A):
 n=len(A); B=[[F(q) for q in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
 for i in range(n):
  p=next(j for j in range(i,n) if B[j][i])
  B[i],B[p]=B[p],B[i];v=B[i][i];B[i]=[q/v for q in B[i]]
  for j in range(n):
   if j!=i:
    v=B[j][i];B[j]=[x-v*y for x,y in zip(B[j],B[i])]
 return [r[n:] for r in B]
S=inverse(K)
assert [[sum(K[i][j]*S[j][h] for j in range(4)) for h in range(4)] for i in range(4)]==[[F(i==j) for j in range(4)] for i in range(4)]
assert K[0][0]==2
assert (S[0][0],S[3][3],S[0][3])==(F(8113,10817),F(10816,10817),F(52,10817))
su2=S[0][0]+t*t*S[3][3]-2*t*S[0][3]
assert su2==F(8115,10817)
q3=lambda x: erfc(x/sqrt(2))+sqrt(2/pi)*x*exp(-x*x/2)
a=float(4*t/pi)*sqrt(float(K[0][0]*S[3][3]))
assert .0346<a<.0347
for T in (1,3,4):
 b=min(1,q3(T/sqrt(float(S[0][0])))+q3(T/sqrt(float(su2))))
 if T==3: assert .0147<b<.0149
 if T==4: assert .00017<b<.00019
 print("threshold",T,"boundary",round(a,8),"rare-exit",round(b,8))
print("PASS: rational reduced precision/covariance; synthetic source-shaped test ONLY")
