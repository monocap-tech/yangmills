#!/usr/bin/env python3
"""YM-EXT-02 finite rational SU(2) flat-seam arithmetic witness.
All-time Wilson-flow stationarity is proved analytically by zero smooth action.
This is NOT source-admitted CMP109 and does not prove mass gap.
"""
from fractions import Fraction as F
from itertools import product

I=((F(1),F(0)),(F(0),F(1)))
V=((F(3,5),F(4,5)),(-F(4,5),F(3,5)))
def mm(A,B):
 return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def T(A): return tuple(tuple(A[j][i] for j in range(2)) for i in range(2))
def move(x,d,n):
 y=list(x);y[d]=(y[d]+1)%n;return tuple(y)
def link(x,d,n):
 return V if d==0 and x[0]==n-1 else I
def p(x,d,e,n):
 return mm(mm(mm(link(x,d,n),link(move(x,d,n),e,n)),T(link(move(x,e,n),d,n))),T(link(x,e,n)))
assert mm(T(V),V)==I
assert V[0][0]*V[1][1]-V[0][1]*V[1][0]==1
for n in (3,4):
 for d in (3,4):
  sites=product(range(n),repeat=d)
  assert all(p(x,mu,nu,n)==I for x in sites for mu in range(d) for nu in range(mu+1,d))
  x=(0,)*d;h=I
  for k in range(n):
   h=mm(h,link(x,0,n));x=move(x,0,n)
  assert h==V
  assert (h[0][0]+h[1][1])/2 == F(3,5)
  slab=product(range(n-1),*(range(n) for _ in range(d-1)))
  assert all(link(x,mu,n)==I for x in slab for mu in range(d))
  print("PASS",d,"dimensions",n,"per side; plaquettes=I; winding=3/5; local slab=I")
print("PASS exact flat-seam arithmetic; stationary flow follows from smooth Wilson action minimum")
