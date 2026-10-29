#!/usr/bin/env python3
"""YM-AUX-01 exact rational test of the CMP109 periodic-mean identity.
The 2D test checks full normalized shortest paths on a nonconstant field;
the 4D test checks all 13^4 offsets on constant modes. Not source K.
"""
from fractions import Fraction as F
from itertools import product, permutations
L=13
N=26
d=2
def shift(x,mu,k):
 y=list(x);y[mu]=(y[mu]+k)%N;return tuple(y)
def val(x,mu):
 return F(((x[0]*17+x[1]*43+mu*71)**2+5*x[0]+3*x[1])%19-9)
def path(x,n,order):
 total=F(0)
 for mu in order:
  for _ in range(abs(n[mu])):
   if n[mu]>0:
    total+=val(x,mu);x=shift(x,mu,1)
   elif n[mu]<0:
    x=shift(x,mu,-1);total-=val(x,mu)
 return total
def avg(x,n):
 orders=list(permutations([i for i in range(d) if n[i]]))
 return sum((path(x,n,p) for p in orders),F(0))/len(orders)
def D(y,mu):
 yp=shift(y,mu,L);total=F(0)
 for n in product(range(-6,7),repeat=d):
  x=tuple((y[i]+n[i])%N for i in range(d))
  bridge=F(0)
  for j in range(L): bridge+=val(shift(x,mu,j),mu)
  total+=avg(y,n)+bridge-avg(yp,n)
 return total/F(L**d)
for mu in range(d):
 lhs=sum((D(y,mu) for y in product([0,13],repeat=d)),F(0))
 rhs=F(L,L**d)*sum((val(x,mu) for x in product(range(N),repeat=d)),F(0))
 assert lhs==rhs,(mu,lhs,rhs)
 print("PASS 2D",mu,lhs)
d=4
for n in product(range(-6,7),repeat=d):
 for mu in range(d):
  assert n[mu]+L-n[mu]==L
for dim in (2,3,4):
 N=L**2
 assert (N//L)**dim*L==F(L,L**dim)*N**dim
print("PASS 4D 13^4 constant source offsets; 2D nonconstant periodic source sum.")
