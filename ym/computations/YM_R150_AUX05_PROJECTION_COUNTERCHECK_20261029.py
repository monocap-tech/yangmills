#!/usr/bin/env python3
"""YM-R150 direct image correction: AUX05 finite projector is NOT original CMP99 R.
Printed CMP99 (3.21): ran R = Delta_U ker Qprime. This script tests the
modelled one-step centered-block U=1 discrepancy; no source K is constructed.
"""
from fractions import Fraction as F
L=13; N=169
def rho(s):
    return F(1,L*L) if 7<=s<=19 else (F(-1,L*L) if 20<=s<=32 else F(0))
def lap(s):
    return 2*rho(s)-rho((s-1)%N)-rho((s+1)%N)
assert rho(5)==rho(6)==0 and rho(7)==F(1,169)
assert lap(5)==0 and lap(6)==F(-1,169)
# psi = delta_(6,0) - delta_(5,0); both sites belong to centered L-block origin 0
# so Qprime_site psi=0. The source-shaped range includes Delta psi.
inner=lap(6)-lap(5)
assert inner==F(-1,169)
print("PASS Qprime_site psi=0, <D*a,Delta psi>=",inner)
print("PASS AUX05 field fails the corrected CMP99-like R D*a=0 condition")
