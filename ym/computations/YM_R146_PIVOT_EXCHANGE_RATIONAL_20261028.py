#!/usr/bin/env python3
"""YM-R146 exact rational one-slice pivot-exchange negative control.
No CMP99-to-CMP109 theorem is asserted.
"""
from fractions import Fraction as F
from math import sqrt

def matmul(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]

T = [[F(-1),F(-1),F(-1)],[F(0),F(1),F(0)],[F(0),F(0),F(1)]]
det = (T[0][0]*(T[1][1]*T[2][2]-T[1][2]*T[2][1])
       -T[0][1]*(T[1][0]*T[2][2]-T[1][2]*T[2][0])
       +T[0][2]*(T[1][0]*T[2][1]-T[1][1]*T[2][0]))
assert det == -1
assert matmul(T,T) == [[F(int(i==j)) for j in range(3)] for i in range(3)]

theta=F(1)
a,b,z1,z2 = F(6,5),F(0),F(-3,5),F(-3,5)
assert a+b+z1+z2 == 0
assert all(abs(v)<theta for v in [b,z1,z2]) # omit a
assert not all(abs(v)<theta for v in [a,z1,z2]) # omit b
x=[b,z1,z2]
y=[sum(v*t for v,t in zip(row,x)) for row in T]
assert y == [a,z1,z2]
N=13**3
assert N==2197 and F(13,13**4)==F(1,N)
lam_plus=(N+sqrt(N*N-4))/2
sig=sqrt(lam_plus)
assert 46.87 < sig < 46.88
print("PASS: det=-1, T²=I, exact constrained cutoff mismatch, N=2197")
print("interface-only Euclidean chart norm =",format(sig,".9f"))
