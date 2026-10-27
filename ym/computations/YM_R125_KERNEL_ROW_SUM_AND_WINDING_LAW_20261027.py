"""YM-R125 exact kernel row sum and scalar winding-law negative control.

Arithmetic checks for a CONDITIONAL theorem, not CMP102 theorem extraction.
"""
from fractions import Fraction as F
from itertools import product

rho=F(1,2)
d=4
m=4
infinite_row=((1+rho)/(1-rho))**d
assert infinite_row==81
CH_example=m*infinite_row
assert CH_example==324

# Truncated l1 convolution sum must lie below the infinite-row bound.
R=4
finite_row=sum((rho**sum(map(abs,z)) for z in product(range(-R,R+1),repeat=d)),F(0))
assert F(0)<finite_row<infinite_row

# Two laws centered at one prescribed Wilson scalar v=0.
eps=F(1,100)
v=F(0)
nu0=-eps
nu1=+eps
e0=e1=eps
q0=q1=F(0)
w1=abs(nu0-nu1)
assert w1==2*eps==e0+e1+2*(q0+q1)
# Distinct point masses: total variation (sup_A) is exactly 1.
TV=1
assert TV==1 and w1<F(1,10)

# General bounded-good-event expectation inequality with rational trial.
q0,q1=F(1,100),F(3,100)
e0,e1=F(1,1000),F(2,1000)
bound=e0+e1+2*(q0+q1)
assert bound==F(83,1000)
assert bound<2

print("PASS R125 exact d4 row sum", infinite_row, "oriented m=4 bound", CH_example)
print("PASS R125 finite row sum", finite_row)
print("PASS R125 W1 of disjoint near-coarse-point masses",w1,"TV",TV)
print("PASS R125 good-event winding law bound example",bound)
print("CMP102 source A/kappa, real Yang-Mills q_i and normalized cutoff laws OPEN")
