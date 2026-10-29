#!/usr/bin/env python3
"""YM-AUX-03 exact rational non-pure-gauge co-closed regional null witness.
Source-shaped derivative: CMP109 (0.3)-(0.4), identity linearization, full torus.
N=L^2=169. No actual source Ω, CMP99 K, covariance or 4D mass-gap proof.
"""
from fractions import Fraction as F
from itertools import product, permutations
L=13
N=L**2
d=2
O=tuple(product(range(-(L-1)//2,(L-1)//2+1),repeat=d))
Y=tuple((0,j) for j in range(0,N,L))
def sh(x,i,z):
    y=list(x)
    y[i]=(y[i]+z)%N
    return tuple(y)
def plaq(x):
    return {(x,0):F(1),(sh(x,0,1),1):F(1),
            (sh(x,1,1),0):F(-1),(x,1):F(-1)}
A={}
for j in range(0,N,L):
    for k,v in plaq((7,j)).items():
        A[k]=A.get(k,F(0))-338*v
def a(x,mu):
    return A.get((x,mu),F(0))+int(mu==0)
def path(x,n,p):
    t=F(0)
    for i in p:
        for _ in range(abs(n[i])):
            if n[i]>0:
                t+=a(x,i)
                x=sh(x,i,1)
            else:
                x=sh(x,i,-1)
                t-=a(x,i)
    return t
def P(y):
    total=F(0)
    for n in O:
        pp=list(permutations(i for i in range(d) if n[i]))
        total+=sum((path(y,n,p) for p in pp),F(0))/len(pp)
    return total/L**d
def coarse(y,mu):
    yp=sh(y,mu,L)
    b=F(0)
    for n in O:
        x=tuple((y[i]+n[i])%N for i in range(d))
        for j in range(L):
            b+=a(sh(x,mu,j),mu)
    return P(y)-P(yp)+b/L**d
for y in Y:
    assert coarse(y,0)==coarse(y,1)==0,(y,coarse(y,0),coarse(y,1))
print("PASS",len(Y)*d,"regional CMP109 coarse link constraints on N=L^2")
for x in product(range(N),repeat=d):
    div=sum((a(x,mu)-a(sh(x,mu,-1),mu) for mu in range(d)),F(0))
    assert div==0,(x,div)
print("PASS all",N**d,"ordinary Landau co-closed site equations")
# x1 in [-6,6], all transverse x2, only a1=1 inside.
assert all(A.get(((x1%N,x2),0),0)==0
           for x1 in range(-6,7) for x2 in range(N))
print("PASS regional horizontal mean exactly 1")
def curl12(x):
    return a(x,0)+a(sh(x,0,1),1)-a(sh(x,1,1),0)-a(x,1)
for j in range(0,N,L):
    assert curl12((7,j))==-1352,(j,curl12((7,j)))
print("PASS nonzero plaquette curl -1352 at each boundary circulation")
assert max(abs(a(x,mu))
           for x in product(range(N),repeat=d) for mu in range(d))==339
print("PASS finite sup norm 339; scaling remains linear constraint solution")
# A 4D shortest-contour average on a 2D-invariant field reduces exactly
# to the two-dimensional relative-order marginal for axes 0 and 1.
for mask in range(1<<4):
    active=[i for i in range(4) if mask&(1<<i)]
    pp=list(permutations(active))
    if 0 in active and 1 in active:
        assert 2*sum(o.index(0)<o.index(1) for o in pp)==len(pp)
print("PASS 4D shortest permutation marginal lift")
