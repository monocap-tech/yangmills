#!/usr/bin/env python3
"""Full ONE-COARSE-LINK CMP109 (0.4) vs CMP98 selected-contour source-shaped test.
Exact integer accumulator denominator 4! L^4; includes all 13^4 sites, right
block, bridge, historical descending contours and R120 endpoint-frame paths.
NOT full multi-row regional CMP99 Q_j; cannot certify K_new or rho.
"""
from itertools import product, permutations, combinations
from collections import defaultdict
from math import factorial
from fractions import Fraction as F
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
    for j in range(L):new[(x[0]+j,x[1],x[2],x[3],0)]+=W
new={k:v for k,v in new.items() if v}
a=(L-1,0,0,0,0); b=(L-1,r,r,r,0); z=(0,1,0,0,2)
bridge={(L-1,u,v,w,0) for u,v,w in product(range(L),repeat=3)}
kappa=F(1,L**3); t=F(1,52)
assert len(bridge)==L**3==2197
assert all(F(new[key],den)==kappa for key in bridge)
assert F(new[z],den)==-F(1,4*L**4)
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
    for j in range(L):old[(x[0]+j,x[1],x[2],x[3],0)]+=W
add_path((0,0,0,0),s,-den)
add_path((L,0,0,0),(L+r,r,r,r),den)
old={k:v for k,v in old.items() if v}
diff={k:new.get(k,0)-old.get(k,0) for k in new.keys()|old.keys()}
diff={k:v for k,v in diff.items() if v}
assert all(old.get(key,0)==new[key] for key in bridge)
assert all(key not in bridge for key in diff)
assert old.get(z,0)==0 and F(diff[z],den)==-kappa*t
# Full one-ROW dual from F=P_a C_n^b, NOT full multiscale regional F:
va={key:-F(val,new[b]) for key,val in new.items() if key!=a}
vu=va.copy();vu[z]-=t
assert all(va[key]==vu[key]==-1 for key in bridge-{a})
assert va[z]==t and vu[z]==0
assert sum(abs(va[key]) for key in bridge-{a})==2196
assert sum(va[key]**2 for key in bridge-{a})==2196
assert (len(new),len(old),len(diff))==(213109,32959,210912)
assert (sum(map(abs,va.values())),sum(v*v for v in va.values())) == (F(1033788,13),F(3165876))
assert (sum(map(abs,vu.values())),sum(v*v for v in vu.values())) == (F(4135151,52),F(8560528703,2704))
vold={key:-F(val,new[a]) for key,val in old.items() if key!=a}
vdef={key:-F(val,new[a]) for key,val in diff.items() if key!=a}
assert all(va.get(key,0)==vold.get(key,0)+vdef.get(key,0) for key in va.keys()|vold.keys()|vdef.keys())
print("PASS: 2197 crossing bridge coefficients kappa=1/2197 cancel in delta exactly")
print("PASS: z source curvature coefficient -1/114244; t=1/52 and vu[z]=0")
print("PASS: 213109 new, 32959 old, 210912 difference supported bonds")
print("PASS: full one-row dual |va|_1=1033788/13, |vu|_1=4135151/52")
print("PASS: bridge-only each old-coordinate dual has 2196 unit coefficients")
print("PASS: dual va = full historical eliminated pivot + normalized contour defect")
print("NOTE: no full regional chart, historical variance contraction, rho, normalized UV law or mass gap")
