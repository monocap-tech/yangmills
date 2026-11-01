#!/usr/bin/env python3
"""YM-R150 exact cone filling for the DECLARED full one-coarse-link L=13 model.
CMP109(0.4) new shortest paths vs CMP98(15) old descending axial paths,
with R120 endpoint frame transport. NOT actual CMP99 regional Q_j/Ω/Gaussian.
Pure standard library, exact integer and Fraction arithmetic.
"""
from itertools import product, permutations, combinations
from collections import defaultdict
from math import factorial
from fractions import Fraction as Q

L=13; r=6; s=(r,)*4; den=factorial(4)*L**4; W=factorial(4)
orders={ax:tuple(permutations(ax)) for k in range(5) for ax in combinations(range(4),k)}
new=defaultdict(int)
for x in product(range(L),repeat=4):
    ax=tuple(i for i in range(4) if x[i]!=r)
    wt=W//factorial(len(ax))
    for perm in orders[ax]:
        cur=list(s)
        for mu in perm:
            d=1 if x[mu]>r else -1
            for _ in range(abs(x[mu]-r)):
                edge=tuple(cur) if d==1 else tuple(cur[i]-(i==mu) for i in range(4))
                new[edge+(mu,)]+=wt*d
                new[(edge[0]+L,)+edge[1:]+(mu,)]-=wt*d
                cur[mu]+=d
    for j in range(L):
        new[(x[0]+j,x[1],x[2],x[3],0)]+=W
new={k:v for k,v in new.items() if v}
old=defaultdict(int)
def add_path(start,end,weight):
    cur=list(start)
    for mu in (3,2,1,0):
        d=1 if end[mu]>=cur[mu] else -1
        for _ in range(abs(end[mu]-cur[mu])):
            edge=tuple(cur) if d==1 else tuple(cur[i]-(i==mu) for i in range(4))
            old[edge+(mu,)]+=weight*d
            cur[mu]+=d
for x in product(range(L),repeat=4):
    add_path((0,0,0,0),x,W)
    add_path((L,0,0,0),(x[0]+L,x[1],x[2],x[3]),-W)
    for j in range(L):
        old[(x[0]+j,x[1],x[2],x[3],0)]+=W
add_path((0,0,0,0),s,-den)
add_path((L,0,0,0),(L+r,r,r,r),den)
old={k:v for k,v in old.items() if v}
delta={k:new.get(k,0)-old.get(k,0) for k in new.keys()|old.keys()}
delta={k:v for k,v in delta.items() if v}
kappa=Q(1,L**3); t=Q(1,52)
a=(L-1,0,0,0,0); b=(L-1,r,r,r,0); z=(0,1,0,0,2)
bridge={(L-1,u,v,w,0) for u,v,w in product(range(L),repeat=3)}
assert (len(new),len(old),len(delta))==(213109,32959,210912)
assert all(new[k]==old[k] and k not in delta for k in bridge)
assert Q(delta[z],den)==-kappa*t
# Independent exact chain boundary test (0-cells).
boundary=defaultdict(int)
for e,c in delta.items():
    u=e[:4];mu=e[4]
    v=tuple(u[i]+(i==mu) for i in range(4))
    boundary[u]-=c
    boundary[v]+=c
assert all(c==0 for c in boundary.values())
assert all(0<=e[0]<=25 and all(0<=e[i]<=12 for i in range(1,4)) for e in delta)
scale=den*kappa
assert scale==312
l1=Q(sum(abs(c) for c in delta.values()),1)/scale
l2sq=Q(sum(c*c for c in delta.values()),1)/(scale*scale)
assert l1==Q(2803036,13) and l2sq==Q(523953742,3)
assert Q(delta[z],1)/scale==-t
u2sq=l2sq-t*t
assert u2sq==Q(1416770918365,8112)
# Axial-cone plaquette filling with root (0,0,0,0), ascending-axis paths.
plaquettes=defaultdict(int)
for e,c in delta.items():
    u=e[:4];mu=e[4]
    for nu in range(mu+1,4):
        for j in range(u[nu]):
            v=list(u);v[nu]=j
            for k in range(nu+1,4):v[k]=0
            plaquettes[tuple(v)+(mu,nu)]-=c
plaquettes={k:v for k,v in plaquettes.items() if v}
assert len(plaquettes)==153792
bdy=defaultdict(int)
for p,c in plaquettes.items():
    u=p[:4];mu,nu=p[4],p[5]
    v=list(u);v[mu]+=1
    w=list(u);w[nu]+=1
    bdy[u+(mu,)]+=c
    bdy[tuple(v)+(nu,)]+=c
    bdy[tuple(w)+(mu,)]-=c
    bdy[u+(nu,)]-=c
assert all(bdy.get(e,0)==delta.get(e,0) for e in bdy.keys()|delta.keys())
pl1=Q(sum(abs(c) for c in plaquettes.values()),1)/scale
pl2sq=Q(sum(c*c for c in plaquettes.values()),1)/(scale*scale)
assert pl1==Q(20342037,13)
assert pl2sq==Q(3568504628,3)
print("PASS: ∂Δ=0 and 153792-plaquette axial-cone chain ∂S=Δ exactly")
print("PASS: all 2197 interface bridges cancel and Δ(z)/κ=-1/52")
print("PASS: ||Δ/κ||1 =",l1,"||Δ/κ||2² =",l2sq)
print("PASS: ||(Δ/κ)+t e_z||2² =",u2sq)
print("PASS: ||S/κ||1 =",pl1,"||S/κ||2² =",pl2sq)
print("NOTE: no source Ω, covariance contraction, 1987 relative form rho or YM gap")
