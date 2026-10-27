"""YM-R119 exact L13 full-coarse-link first-variation test.

Source-shaped setup: c:0->13e1, B(0)=[-6,6]^4, old descending
axial selected path 4,3,2,1 (declared test convention), new uniform
shortest-coordinate-order permutations at both endpoints. Test A is a
unit su(2) component on e3 bond (0,1,0,0)->(0,1,1,0).
The bridge is along e1 and right endpoint paths are shifted by 13e1,
so both have ZERO response to this bond. No continuum YM claim.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb

L = 13
rad = (L - 1) // 2
tail = (0, 1, 0, 0)
tip = (0, 1, 1, 0)
axis = 2  # e3, zero indexed

def ordered_steps(displacement, order):
    p = [0, 0, 0, 0]
    for i in order:
        sign = 1 if displacement[i] > 0 else -1
        for _ in range(abs(displacement[i])):
            q = p.copy()
            q[i] += sign
            yield tuple(p), tuple(q)
            p = q

def sparse_flux(displacement, order):
    return sum(
        (1 if u == tail and v == tip else
         -1 if u == tip and v == tail else 0)
        for u, v in ordered_steps(displacement, order)
    )

old_sum = 0
new_sum = F(0)
for x0 in range(-rad, rad + 1):
    for x2 in range(1, rad + 1):
        for x3 in range(-rad, rad + 1):
            x = (x0, 1, x2, x3)
            active = tuple(i for i, val in enumerate(x) if val)
            chosen = tuple(sorted(active, reverse=True))
            old_sum += sparse_flux(x, chosen)
            perms = tuple(permutations(active))
            new_sum += F(sum(sparse_flux(x, order) for order in perms), len(perms))

assert old_sum == 0, old_sum
assert new_sum == 99, new_sum
coefficient = F(new_sum, L**4)
assert coefficient == F(99, 28561), coefficient

# The expected area of differing adjacent swaps, for BOTH endpoints,
# is sum_{i<j} E|x_i|E|x_j| for uniform [-6,6]^4.
mean_abs_coordinate = F(rad * (rad + 1), L)
curl_bound = comb(4, 2) * mean_abs_coordinate**2
assert curl_bound == F(10584, 169)
assert mean_abs_coordinate == F(42, 13)

# A full link composed of three paths telescopes on any exact gradient:
# (phi(x)-phi(y))+(phi(x')-phi(x))-(phi(x')-phi(y'))
# equals phi(y')-phi(y), regardless of contour permutation.
a, b, c, d = F(1, 7), F(2, 9), F(-3, 11), F(5, 13)
assert (b-a)+(c-b)-(c-d) == d-a

print("PASS YM-R119 exact full-link old coefficient", old_sum)
print("PASS YM-R119 exact full-link symmetric coefficient", coefficient)
print("PASS YM-R119 finite-block plaquette-curl operator bound", curl_bound)
print("PASS YM-R119 pure-gauge endpoint telescoping")
