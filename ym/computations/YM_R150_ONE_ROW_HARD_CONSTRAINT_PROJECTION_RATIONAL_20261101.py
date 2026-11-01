#!/usr/bin/env python3
"""YM-R150 exact ONE-ROW hard-constraint projection of contour defect.
Reuses archived full source-shaped L13 enumeration, not a native CMP99 Ω/gauge
or its 1987 relative-Hessian transfer. Exact Fraction checks only.
"""
from pathlib import Path
from runpy import run_path
from fractions import Fraction as Q
from collections import defaultdict
p=run_path(str(Path(__file__).with_name("YM_R150_CONTOUR_DEFECT_DISCRETE_CURL_20261101.py")))
old=p["old"]; delta=p["delta"]; new=p["new"]
den=p["den"]; kappa=p["kappa"]; z=p["z"]; t=p["t"]
assert den==24*13**4 and den*kappa==312
old2=sum(c*c for c in old.values())
dot=sum(c*old.get(e,0) for e,c in delta.items())
delta2=sum(c*c for c in delta.values())
new2=sum(c*c for c in new.values())
assert (old2,dot,delta2,new2)==(
    17543968513344,-17118520201536,17001251020416,308179130688)
beta=Q(dot,old2)
assert beta==-Q(240131,246099)
removed=Q(dot*dot,old2*delta2)
assert removed==Q(57662897161,58691166114)
norm2=Q(delta2,1)/(den*kappa)**2
proj2=norm2*(1-removed)
assert norm2==Q(523953742,3)
assert proj2==Q(2259106889741,738297)
assert Q(new2,1)/(den*kappa)**2==3165877
assert old.get(z,0)==0
assert Q(delta[z],1)/(den*kappa)==-t
proj2u=proj2-t*t
assert proj2u==Q(6108625029121367,1996355088)
# Orthogonality in raw integer units; projected coefficient is delta-beta old.
assert sum((Q(c)-beta*old.get(e,0))*old.get(e,0)
           for e,c in delta.items()) == beta*sum(
           c*c for e,c in old.items() if e not in delta)
# Exact off-shell boundary for old and delta; projected is not gauge closed.
def bdry(coeff):
    out=defaultdict(lambda:Q(0))
    for e,c in coeff.items():
        u=e[:4];mu=e[4]
        v=tuple(u[i]+(i==mu) for i in range(4))
        out[u]-=c;out[v]+=c
    return {e:c for e,c in out.items() if c}
s=(6,6,6,6);sp=(19,6,6,6)
assert bdry(old)=={s:-den,sp:den}
assert bdry(delta)=={}
proj={e:Q(delta.get(e,0))-beta*old.get(e,0)
      for e in set(old)|set(delta)}
proj={e:c for e,c in proj.items() if c}
assert bdry(proj)=={s:beta*den,sp:-beta*den}
print("PASS old rank-one projector beta:",beta)
print("PASS squared fraction removed:",removed,"=",float(removed))
print("PASS projected normalized ||Δ/κ||²:",proj2,"=",float(proj2))
print("PASS second R149 probe projected squared norm:",proj2u)
print("PASS δ is gauge closed; hard-constrained representative generally is not")
print("NOT a CMP99 source Q1-region projection or 1987 Gaussian transfer")
