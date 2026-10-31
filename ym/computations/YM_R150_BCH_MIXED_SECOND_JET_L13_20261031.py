#!/usr/bin/env python3
"""YM-R150 exact BCH mixed second jet for DECLARED aligned L13 old/new path comparison.
Old selected contour CMP98(15) with descending CMP95 path and R120 endpoint
transport; new shortest-permutation CMP109(0.4). NOT full regional CMP99 Q_j.
"""
from fractions import Fraction as F
from itertools import permutations, product
L=13
s=(6,6,6,6)
p=((1,2,6,6),1)  # positively oriented e2 bond, generator X
q=((1,1,2,6),2)  # positively oriented e3 bond, generator Y

def hits(start,end,order):
    z=list(start);found=[]
    for mu in order:
        step=1 if end[mu]>=z[mu] else -1
        while z[mu]!=end[mu]:
            nxt=z.copy();nxt[mu]+=step
            edge=(tuple(z) if step>0 else tuple(nxt),mu)
            if edge==p: found.append(("X",step))
            if edge==q: found.append(("Y",step))
            z=nxt
    return found

total=F(0);sites=0;permutations_with_both=0
for x in product(range(L),repeat=4):
    # Necessary geometric conditions for BOTH edges: verified from support and order
    if x[0]!=1 or x[1]!=1 or x[2]>2: continue
    sites+=1
    axes=[j for j in range(4) if x[j]!=s[j]]
    perms=list(permutations(axes))
    for perm in perms:
        got=hits(s,x,perm)
        if len(got)==2:
            assert got==[("X",-1),("Y",-1)],(x,perm,got)
            permutations_with_both+=1
            total+=F(1,len(perms))
assert sites==39 and permutations_with_both==39
assert total==3*(F(12,24)+F(1,6))==2
mixed_hessian=total/F(2*L**4)
assert mixed_hessian==F(1,28561)
# Old left descending 4,3,2,1: transverse edges always have x1=0
for x in product(range(L),repeat=4):
    assert hits((0,0,0,0),x,[3,2,1,0])==[]
# Old/new gauge-endpoint transport legs have no supported edges
assert hits((0,0,0,0),s,[3,2,1,0])==[]
assert hits((13,0,0,0),(19,6,6,6),[3,2,1,0])==[]
print("PASS: 39 eligible endpoints, weighted path count 2")
print("PASS: mixed D2 log Mnew = 1/28561 [X,Y], old = 0")
print("NOTE: CMP98-style old selected contour, source-shaped identity cell only")
