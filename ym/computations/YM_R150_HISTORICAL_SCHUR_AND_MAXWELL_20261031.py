#!/usr/bin/env python3
"""YM-R150: source theorem 3.15 -> geometric Schur constant verification.
This checks ONLY the elementary lattice sum; B0,delta0 remain UNSPECIFIED
source constants, no numerical Bałaban precision or mass-gap claim.
"""
from itertools import product
from math import exp,erfc,sqrt,pi
for delta in (0.25,1.0,2.0):
    q=exp(-delta/2)
    series=((1+q)/(1-q))**4
    truncated=sum(q**sum(abs(v) for v in z) for z in product(range(-3,4),repeat=4))
    assert truncated < series
    B0=1.0 # DEMONSTRATION ONLY, not source value
    M=12*B0*exp(delta)*series
    assert M>12*B0
    print(f"CHECK delta={delta:.2f}: finite lattice sum {truncated:.6f} < infinite {series:.6f}; M_demo={M:.6f}")
def Q3(r): return erfc(r/sqrt(2))+sqrt(2/pi)*r*exp(-r*r/2)
assert Q3(0)==1
assert 0<Q3(4)<Q3(2)<Q3(1)<1
print("PASS: 4D lattice Schur series and Maxwell survival monotonicity; symbolic source constants only")
