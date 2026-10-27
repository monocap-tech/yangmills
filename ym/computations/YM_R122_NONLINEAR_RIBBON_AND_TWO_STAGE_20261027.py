"""YM-R122 exact source-weighted L13 ribbon and deterministic M iteration gate.
Certified exact combinatorics only; conditional small-field thresholds, not a YM proof.
"""
from fractions import Fraction as F
from itertools import product

L, r, d = 13, 6, 4
total = 0
count = 0
max_area = 0

for n in product(range(-r, r+1), repeat=d):
    a = tuple(abs(x) for x in n)
    # Both endpoint uniform permutations: expected two inversions = 1 per pair.
    canonical_strip = L * sum(a[1:])
    pair_area = sum(a[i]*a[j] for i in range(d) for j in range(i+1,d))
    mean_area = canonical_strip + pair_area
    conservative_max = canonical_strip + 2*pair_area
    total += mean_area
    max_area = max(max_area, conservative_max)
    count += 1

assert count == L**d == 28561
average_area = F(total,count)
assert average_area == F(31878,169)
assert max_area == 666
mean_abs = F(r*(r+1),L)
assert mean_abs == F(42,13)
assert L*3*mean_abs + 6*mean_abs**2 == average_area

C = average_area
eta0 = F(1,10**7)  # Deliberately stronger test condition; not a source threshold.
assert 666*eta0 < 1
delta0 = C*eta0/(1-666*eta0)
eta1_upper = L*L*eta0 + 4*delta0
assert 666*eta1_upper < 1
delta1 = C*eta1_upper/(1-666*eta1_upper)
two_stage_upper = L*delta0 + delta1
assert delta0 > 0 and delta1 > 0 and two_stage_upper > delta1
print("PASS R122 28561 site expected ribbon area",average_area)
print("PASS R122 maximum conservative ribbon area",max_area)
print("PASS R122 conditional chart feasibility at eta0=1e-7")
print("delta0=",float(delta0),"eta1 upper=",float(eta1_upper))
print("two-stage deterministic upper=",float(two_stage_upper))
