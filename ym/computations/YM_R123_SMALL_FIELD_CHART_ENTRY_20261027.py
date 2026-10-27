"""YM-R123 exact numerical threshold for conditional CMP109 nonlinear M chart.

Reads the source background regularity eta<=epsilon0*eta_k^2 as a
HYPOTHESIS. Exact arithmetic verifies the R122 TWO-STAGE SU2 sufficient
criterion, not the numerical source choice of epsilon0 or the RG law.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext

L=13
q=666
C=F(31878,169)

def get_second_stage_entry(x):
    assert 0<=x<F(1,q), "first chart condition"
    d0=C*x/(1-q*x)
    y=L*L*x+4*d0
    return d0,y, q*y<1

x1=F(1,10**6)
d1,y1,valid1=get_second_stage_entry(x1)
assert valid1 and q*y1 < 1
x2=F(2,10**6)
d2,y2,valid2=get_second_stage_entry(x2)
assert not valid2 and q*y2 > 1
assert q*x1 < 1 and q*x2<1

# Exact algebra: near zero branch of a*x^2-b*x+1>0.
a=q*q*L*L
b=F(q)*(L*L + 1 + 4*C)
assert a*x1*x1-b*x1+1>0
assert a*x2*x2-b*x2+1<0
with localcontext() as ctx:
    ctx.prec=50
    B=Decimal(b.numerator)/Decimal(b.denominator)
    A=Decimal(a)
    smaller=(B-(B*B-4*A).sqrt())/(2*A)
    assert Decimal(x1.numerator)/Decimal(x1.denominator) < smaller
    assert smaller < Decimal(x2.numerator)/Decimal(x2.denominator)
    print("two-stage epsilon0 eta_k^2 threshold:", smaller)

print("PASS source-regular background eta<=epsilon0*eta_k^2 requires additional chart gate")
print("PASS exact q*eta1_upper for x=1e-6:",q*y1)
print("PASS fails for x=2e-6:",q*y2)
print("No source cutoff constant, Omega halo or UV law proved")
