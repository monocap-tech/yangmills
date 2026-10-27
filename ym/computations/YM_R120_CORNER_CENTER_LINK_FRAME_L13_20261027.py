"""R120 exact rational source-shaped L13 corner-to-center coarse-link test.

This is a DECLARED COMMON INTEGER CELL, not proof that CMP95/CMP98/CMP109
physical fine-lattice offsets, block endpoints, collars and normalizers match.
Old axial path is the CMP95 (1.7) descending order (4,3,2,1), used by
CMP98 (14)-(15). New centered paths average active-axis permutations.
"""
from fractions import Fraction as F
from itertools import product, permutations

L = 13
D = 4
corner = (0, 0, 0, 0)
corner_right = (13, 0, 0, 0)
center = (6, 6, 6, 6)
center_right = (19, 6, 6, 6)
tail = (0, 1, 0, 0)
axis = 2                       # e3 positive edge from tail

def edge_path_coefficient(start, end, order):
    """Signed coefficient of one unit directed e3 bond on a monotone path."""
    if axis not in order:
        return 0
    direction = 1 if end[axis] > start[axis] else -1
    if direction > 0 and not start[axis] <= tail[axis] < end[axis]:
        return 0
    if direction < 0 and not end[axis] <= tail[axis] < start[axis]:
        return 0
    before = order[:order.index(axis)]
    for j in range(D):
        if j == axis:
            continue
        position = end[j] if j in before else start[j]
        if position != tail[j]:
            return 0
    return direction

old_sum = 0
new_sum = F(0)
nonzero_new_sites = []
for x in product(range(L), repeat=D):
    xr = (x[0] + L, x[1], x[2], x[3])
    old_active = tuple(i for i in range(D) if x[i] != corner[i])
    descending = tuple(sorted(old_active, reverse=True))
    old_left = edge_path_coefficient(corner, x, descending)
    old_right = edge_path_coefficient(corner_right, xr, descending)
    old_sum += old_left - old_right

    new_active = tuple(i for i in range(D) if x[i] != center[i])
    options = tuple(permutations(new_active))
    left = sum(edge_path_coefficient(center, x, order) for order in options)
    right = sum(edge_path_coefficient(center_right, xr, order) for order in options)
    contribution = F(left - right, len(options))
    new_sum += contribution
    if contribution:
        nonzero_new_sites.append((x, contribution))

tau_order = (3, 2, 1, 0)
tau_left = edge_path_coefficient(corner, center, tau_order)
tau_right = edge_path_coefficient(corner_right, center_right, tau_order)
old_transported = -tau_left + F(old_sum, L**D) + tau_right
new_full = new_sum / L**D
difference = new_full - old_transported

assert old_sum == 0, old_sum
assert tau_left == 0 and tau_right == 0
assert nonzero_new_sites == [((0, 1, 0, 0), F(-1, 4))]
assert new_sum == F(-1, 4)
assert difference == F(-1, 114244), difference

# A gauge gradient is the difference of endpoint site values.
# Old corner coarse link plus fine transport from corner to center
# has exactly the same gauge signature as new center coarse link.
values = tuple(F(a, b) for a, b in ((1, 7), (2, 9), (-3, 11), (5, 13)))
cy, cp, sy, sp = values
old_coarse_gradient = cp - cy
left_tau_gradient = sy - cy
right_tau_gradient = sp - cp
assert -left_tau_gradient + old_coarse_gradient + right_tau_gradient == sp - sy

print("PASS R120 complete integer cell site enumeration", L**D)
print("PASS R120 old (descending) transported response", old_transported)
print("PASS R120 new (symmetric centered) response", new_full)
print("PASS R120 new minus transported old", difference)
print("PASS R120 pure-gauge endpoint transport covariance")
