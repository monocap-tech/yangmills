#!/usr/bin/env python3
"""YM-R147 exact rational finite five-bond composite constraint/pivot certificate.
One declared L=13 source-shaped identity cell, NOT full Bałaban region or YM proof.
"""
from fractions import Fraction as F
L=13; k=F(1,L**3); eps=F(1,4*L**4); t=eps/k
assert (k,eps,t)==(F(1,2197),F(1,114244),F(1,52))
def mm(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def ident(n):return [[F(i==j) for j in range(n)] for i in range(n)]
# Ambient bonds: a,b,w1,w2,z. New chart removes b, old removes a.
Do=[[k,k,k,k,F(0)]]
Dn=[[k,k,k,k,-eps]]
h=[[1/k],[0],[0],[0],[0]]
assert mm(Do,h)==mm(Dn,h)==[[1]]
S=ident(5)
for i in range(5):
    for j in range(5):
        S[i][j]-=h[i][0]*(Do[0][j]-Dn[0][j])
Cn=[[1,0,0,0],[-1,-1,-1,t],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
Co=[[-1,-1,-1,0],[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
Pa=[[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
T=mm(Pa,Cn)
assert T==[[-1,-1,-1,t],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
assert mm(T,T)==ident(4)
assert mm(Do,Co)==mm(Dn,Cn)==[[0]*4]
assert mm(S,Cn)==mm(Co,T)
# θ=1; strict curvature-sensitive cutoff mismatch, despite same b omission.
y=[-F(207,208),F(0),F(0),F(1,2)]
x=[sum(a*b for a,b in zip(row,y)) for row in T]
new=[sum(a*b for a,b in zip(row,x)) for row in Cn]
old=[sum(a*b for a,b in zip(row,new)) for row in S]
assert new==[F(209,208),-F(207,208),0,0,F(1,2)]
assert old==[F(207,208),-F(207,208),0,0,F(1,2)]
assert sum(a*b for a,b in zip(Dn[0],new))==0
assert sum(a*b for a,b in zip(Do[0],old))==0
assert not all(abs(new[i])<1 for i in [0,2,3,4])
assert all(abs(old[i])<1 for i in [0,2,3,4])
# Distinct pivot box mismatch remains at z=0 (hypothetical old a-box).
y=[F(0),-F(3,5),-F(3,5),F(0)]
x=[sum(a*b for a,b in zip(row,y)) for row in T]
assert x[0]==F(6,5) and all(abs(q)<1 for q in y)
assert not all(abs(q)<1 for q in x)
print("PASS: t=1/52, exact composite S Cn=Co F, F^2=I, det(F)=-1")
print("PASS: strict monitored curvature shift and hypothetical pivot-box negative controls")
print("NOTE: native Ω, Hessian, partition and full YM laws NOT tested")
