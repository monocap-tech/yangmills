"""YM-R121 exact affine lattice cell and two-stage path-cocycle certificate.

Source-typed combinatorial test, NOT a source-renormalization-law comparison.
Finite periodic one-step lattice grids, L=13, d=4; finest spacing h=1.
"""
from itertools import product, combinations
from fractions import Fraction as F

L = 13
r = (L - 1) // 2
d = 4
old = set(product(range(L), repeat=d))
# Coordinates in units h/2: translated old fine sites = 2*i + 1.
translated = {tuple(2*i+1 for i in x) for x in old}
# CMP109 new centered block centered at L/2, offsets [-r,+r]h.
centered = {tuple(L + 2*(i-r) for i in x) for x in old}
assert translated == centered and len(old) == L**d
assert tuple(F(L,2) - F(1,2) for _ in range(d)) == (r,)*d

# Embeddings at scales h_j=L^j h: old fine grid + h_j/2 (in physical units).
for j in range(3):
    h_j = L**j
    old_to_new = F(h_j, 2)
    assert old_to_new + r*h_j == F(L*h_j, 2)
    if j < 2:
        assert F(L*h_j-h_j, 2) == r*h_j

# Lifts of successive affine displacements to FINEST-bond paths, all positive.
t0 = (r,)*d
t1 = (L*r,)*d
total = ((L+1)*r,)*d

def descending(start, steps):
    pos = list(start)
    out = []
    for axis in reversed(range(d)):
        for _ in range(steps[axis]):
            before = tuple(pos)
            pos[axis] += 1
            out.append((before,axis))
    return out, tuple(pos)

p0,end0 = descending((0,)*d,t0)
p1,end1 = descending(end0,t1)
pdir,enddir = descending((0,)*d,total)
staged = p0+p1
assert end1 == enddir == (84,)*d
assert len(staged) == len(pdir) == 336

# For each i<j, integral x_i dx_j measures the signed projected area
# between paths with the same endpoints (discrete Stokes).
areas = {}
for i,j in combinations(range(d),2):
    area = sum(pos[i] for pos,ax in staged if ax==j) - sum(pos[i] for pos,ax in pdir if ax==j)
    areas[(i+1,j+1)] = area
    assert area == r*L*r == 468
swap_count = sum(abs(a) for a in areas.values())
assert swap_count == 2808 == (d*(d-1)//2)*L*r*r

print('PASS YM-R121: exact one-step site bijection',len(old),'at L=13')
print('PASS YM-R121: affine shift telescoping across scales')
print('PASS YM-R121: staged vs direct projected plaquette areas',areas)
print('PASS YM-R121: swap count / holonomy Lipschitz factor',swap_count)
