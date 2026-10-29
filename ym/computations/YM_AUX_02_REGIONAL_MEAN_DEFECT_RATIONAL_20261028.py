#!/usr/bin/env python3
"""YM-AUX-02 exact-rational CMP109 regional boundary audit.
2D L=13 full shortest-permutation average. Also 4D symbolic boundary count.
NOT the source regional CMP99 K, Ω/Λ, Dirichlet/gauge or 4D mass gap.
"""
from fractions import Fraction as F
from itertools import product, permutations
L=13;R=6;N=39;D=2
O=tuple(product(range(-R,R+1),repeat=D))
Y=tuple((0,y1) for y1 in range(0,N,L))
BLK=set((n[0]%N,(y[1]+n[1])%N) for y in Y for n in O)

def shift(x,i,j):
 t=list(x);t[i]=(t[i]+j)%N;return tuple(t)
def field(x,i):
 return F(((17*x[0]+43*x[1]+71*i)**2+5*x[0]+3*x[1])%19-9)
def path(x,n,order,a):
 total=F(0)
 for i in order:
  for _ in range(abs(n[i])):
   if n[i]>0:
    total+=a(x,i);x=shift(x,i,1)
   else:
    x=shift(x,i,-1);total-=a(x,i)
 return total
def P(y,a):
 total=F(0)
 for n in O:
  orders=tuple(permutations(i for i in range(D) if n[i]))
  total+=sum((path(y,n,p,a) for p in orders),F(0))/len(orders)
 return total/F(L**D)
def coarse(y,i,a):
 yp=shift(y,i,L);bridge=F(0)
 for n in O:
  x=tuple((y[q]+n[q])%N for q in range(D))
  for j in range(L):bridge+=a(shift(x,i,j),i)
 return P(y,a)-P(yp,a)+bridge/F(L**D)
def defect_rhs(i,a):
 end=sum((P(y,a)-P(shift(y,i,L),a) for y in Y),F(0))
 br=sum((a(shift(x,i,j),i)-a(x,i) for x in BLK for j in range(L)),F(0))/F(L**D)
 return end,br
for i in range(D):
 lhs=sum((coarse(y,i,field) for y in Y),F(0))
 baseline=F(L,L**D)*sum((field(x,i) for x in BLK),F(0))
 end,br=defect_rhs(i,field)
 assert lhs-baseline==end+br,(i,lhs,baseline,end,br)
 if i==1:assert end==br==0,(end,br)
 print('PASS REGIONAL IDENTITY mu',i,'Dsum',lhs,'baseline',baseline,'path',end,'bridge',br)
def delta(at,mu):
 return lambda x,i:F(int(x==at and i==mu))
p=(6,0);q=(7,0)
cp=coarse((0,0),0,delta(p,0))
cq=coarse((0,0),0,delta(q,0))
assert (cp,cq)==(F(13,169),F(19,169)),(cp,cq)
assert p in BLK and q not in BLK
def cancel_field(x,i):
 if i!=0:return F(0)
 return F(19)*int(x==p)-F(13)*int(x==q)
assert all(coarse(y,mu,cancel_field)==0 for y in Y for mu in range(D))
regional_mean=sum((cancel_field(x,0) for x in BLK),F(0))/len(BLK)
assert regional_mean==F(19,13*39),(regional_mean,len(BLK))
print('PASS EXPLICIT REGIONAL KERNEL with mean',regional_mean,'coarse coefficient p/q',cp,cq)
Eabs=F(R*(R+1),L)
bound_per_facepair=2*D*Eabs+L-1
assert bound_per_facepair==F(324,13)
print('PASS 2D bound per transverse coarse plane',bound_per_facepair)
assert 2*4*Eabs+L-1==F(492,13)
print('PASS 4D symbolic boundary coefficient',F(492,13))
