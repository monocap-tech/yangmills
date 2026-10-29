#!/usr/bin/env python3
"""YM-AUX-05 exact one-scale site-gauge / Dirichlet countermodel.
Qsite here is a DECLARED centered-block model, not CMP99's full regional Q'.
No claim of satisfying separate bond Q1B=0, native source K, or mass gap.
"""
from fractions import Fraction as F
from itertools import product
L=13
N=L**2
assert N==169
def coarse_origin(s):
    return ((s+L//2)//L*L)%N
def Qstar_lambda(x):
    y1=coarse_origin(x[0])
    return F(1,L**2) if y1==L else (F(-1,L**2) if y1==2*L else F(0))
rho=[Qstar_lambda((s,0)) for s in range(N)]
assert sum(rho)==0
assert all(Qstar_lambda((s,t))==rho[s] for s in range(N) for t in range(N))
A1=[]
running=F(0)
for s in range(N):
    running+=rho[s]
    A1.append(-running)
assert A1[-1]==0
def a(x,mu):
    return A1[x[0]] if mu==0 else F(0)
def Dstar_a(x):
    return (a(((x[0]-1)%N,x[1]),0)-a(x,0)
            +a((x[0],(x[1]-1)%N),1)-a(x,1))
assert all(Dstar_a(x)==Qstar_lambda(x)
           for x in product(range(N),repeat=2))
print("PASS projected gauge: D*a = Qsite*lambda at all",N*N,"sites")
assert all(a((s,t),0)==0
           for s in list(range(7))+list(range(32,N)) for t in range(N))
assert all(a((s,t),0)!=0
           for s in range(7,32) for t in range(N))
print("PASS strict Dirichlet zero extension outside slices 7..31")
phi=[sum((a((s,t),0) for t in range(N)),F(0)) for s in range(N)]
assert phi[0]==0 and phi[19]==-13
assert all(phi[s]-phi[(s-1)%N]==-N*rho[s] for s in range(N))
print("PASS flux is zero at s=0 but Phi(19)=",phi[19])
total=sum((a((s,t),0) for s in range(N) for t in range(N)),F(0))
assert total==-N
assert total/F(N*N)==F(-1,N)
assert total/F(25*N)==F(-1,25)
print("PASS mean full torus",F(-1,N),"mean support strip",F(-1,25))
coarse=tuple(range(0,N,L))
lam={(u,v):(F(1) if u==L else (F(-1) if u==2*L else F(0)))
     for u,v in product(coarse,repeat=2)}
assert all(Qstar_lambda((s,t))==
           lam[(coarse_origin(s),coarse_origin(t))]/L**2
           for s,t in product(range(N),repeat=2))
f=lambda x: F(x[0]+2*x[1]+1)
lhs=sum((Qstar_lambda(x)*f(x) for x in product(range(N),repeat=2)),F(0))
rhs=sum((lam[y]*sum((f(((y[0]+i)%N,(y[1]+j)%N))
                      for i in range(-6,7) for j in range(-6,7)),F(0))/L**2
         for y in lam),F(0))
assert lhs==rhs
print("PASS Qsite* exact Hilbert adjoint of normalized centered-site block average")
print("PASS all assertions (source-shaped one-scale only; Q1 bond constraint untested)")
