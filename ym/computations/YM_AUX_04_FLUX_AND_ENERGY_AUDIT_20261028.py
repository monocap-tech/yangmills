#!/usr/bin/env python3
"""Exact independent AUX03 witness flux and energy audit; not source CMP99 K."""
from itertools import product
from fractions import Fraction as F
L=13
N=L**2
A={}
def sh(x,i,j):
 y=list(x);y[i]=(y[i]+j)%N;return tuple(y)
for j in range(0,N,L):
 z=(7,j)
 for (x,mu),v in [((z,0),1),((sh(z,0,1),1),1),((sh(z,1,1),0),-1),((z,1),-1)]:
  A[x,mu]=A.get((x,mu),0)-338*v
def a(x,mu):return int(mu==0)+A.get((x,mu),0)
flux=[sum(a((s,t),0) for t in range(N)) for s in range(N)]
assert len(set(flux))==1 and flux[0]==N
print('PASS AUX03 normal flux =',N,'on every one of',N,'transverse slices')
assert any(a((s,0),0)!=0 for s in (8,15,47,100))
print('PASS AUX03 globally supported horizontal bonds outside selected strip')
Q={}
z=(0,0)
for (x,mu),v in [((z,0),1),((sh(z,0,1),1),1),((sh(z,1,1),0),-1),((z,1),-1)]:Q[x,mu]=v
def q(x,mu):return Q.get((x,mu),0)
assert all(sum(q(x,mu)-q(sh(x,mu,-1),mu) for mu in range(2))==0 for x in product(range(N),repeat=2))
assert all(sum(q((s,t),0) for t in range(N))==0 for s in range(N))
assert all(x[0] in (0,1) for x,mu in Q)
print('PASS supported co-closed elementary circulation has zero normal flux on every slice')
def curl(x):return a(x,0)+a(sh(x,0,1),1)-a(sh(x,1,1),0)-a(x,1)
E=sum(curl(x)**2 for x in product(range(N),repeat=2))
norm=sum(a(x,mu)**2 for x in product(range(N),repeat=2) for mu in range(2))
assert E==29703440 and norm==5969249 and F(E,norm)==F(1040,209)
print('PASS AUX03 ||da||^2 =',E,'||a||^2 =',norm,'ratio =',F(E,norm))
