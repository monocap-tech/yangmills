#!/usr/bin/env python3
"""YM-R150 source Q1 vs introductory selected-path and transported rows.
Uses archived exact full L13 source-shaped Dnew/Dtau/jtau enumeration.
CMP99 printed p393 references CMP98(124), not introductory CMP98(15).
CMP98(124)-(125) are ORIGINAL-PAPER OCR and still need image audit.
NOT a complete legal CMP99 Ω/Λ/Q1 or native YM Gaussian theorem.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from runpy import run_path
p=run_path(str(Path(__file__).with_name("YM_R150_CONTOUR_DEFECT_DISCRETE_CURL_20261101.py")))
new,oldtau,j=p["new"],p["old"],p["delta"]
den,kappa=p["den"],p["kappa"]
L=13;W=den
assert len(j)==210912 and den*kappa==312
def dot(a,b):return sum(v*b.get(e,0) for e,v in a.items())
def proj_fraction(v,row):return F(dot(v,row)**2,dot(v,v)*dot(row,row))
# Reconstruct the R120 endpoint-frame paths T, in the same raw denominator.
def add_path(row,start,end,weight):
    cur=list(start)
    for mu in (3,2,1,0):
        step=1 if end[mu]>=cur[mu] else -1
        for _ in range(abs(end[mu]-cur[mu])):
            edge=tuple(cur) if step>0 else tuple(cur[i]-(i==mu) for i in range(4))
            row[edge+(mu,)]+=weight*step
            cur[mu]+=step
T=defaultdict(int)
add_path(T,(0,0,0,0),(6,6,6,6),-W)
add_path(T,(L,0,0,0),(L+6,6,6,6),W)
Dsel={e:oldtau.get(e,0)-T.get(e,0) for e in set(oldtau)|set(T)}
Dsel={e:v for e,v in Dsel.items() if v}
assert len(Dsel)==32953
assert proj_fraction(j,oldtau)==F(57662897161,58691166114)
assert proj_fraction(j,Dsel)==F(236083225,52408729416)
# Source CMP98(125) at zero background Q(1)=Q0: mean straight L-bond
# connection path from each x to x+Le1; scalar source prefactor irrelevant
# for kernel projection. Retain raw PATH MULTIPLICITY, not only bridges.
q=defaultdict(int)
for x in product(range(L),repeat=4):
    for ell in range(L):
        q[(x[0]+ell,x[1],x[2],x[3],0)]+=1
assert len(q)==(2*L-1)*L**3==54925
assert min(q.values())==1 and max(q.values())==13
assert dot(q,q)==3227393
assert dot(q,j)==0
assert proj_fraction(j,q)==0
assert F(dot(j,j),312**2)==F(523953742,3)
assert F(dot(new,new),312**2)==F(3165877)
# Alternative comparison Dnew-Dsel is not the gauge-covariant tau deficit.
raw_delta={e:new.get(e,0)-Dsel.get(e,0) for e in set(new)|set(Dsel)}
raw_delta={e:v for e,v in raw_delta.items() if v}
assert proj_fraction(raw_delta,Dsel)==F(12065484649,13015488612)
print("PASS: CMP99 Q1 source-crosswalk differs from introductory selected path")
print("PASS: qsrc 54925 straight path bonds, square norm 3227393")
print("PASS: <qsrc, Dnew−Dsel−T> = 0 exactly; qsrc projector removes 0%")
print("PASS: selected transported model removes 98.248%; untransported selected only 0.4505%")
print("PASS: original 98.248% arithmetic retained, SOURCE-Q1 applicability withdrawn")
print("NOT full source regional Q1 / matched gauge Hessian / YM mass gap")
