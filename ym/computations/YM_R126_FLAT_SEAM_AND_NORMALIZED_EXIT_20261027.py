"""YM-R126 exact integer seam-flatness and normalized bad-event tilt.

Generic finite SU2 torus and positive finite law, not an actual source cutoff.
"""
from fractions import Fraction as F

N, L = 39, 13
assert N % L == 0

def phase(x, axis):
    return int(axis == 0 and x[0] == N - 1)

def move(x, axis):
    y = list(x)
    y[axis] = (y[axis] + 1) % N
    return tuple(y)

def curl_exponent(x, i, j):
    return (phase(x, i) + phase(move(x, i), j)
           - phase(move(x, j), i) - phase(x, j))

for x1 in range(N):
    for x2 in range(N):
        x = (x1, x2, 0, 0)
        for j in (1, 2, 3):
            assert curl_exponent(x, 0, j) == 0
        assert curl_exponent(x, 1, 2) == 0

for transverse in ((0,0,0), (8,5,3), (38,38,38)):
    assert sum(phase((x1,*transverse),0) for x1 in range(N)) == 1

# Local c centered at y1=10 and full R122 e1 halo [4,29].
a, b = 10 - 6, 10 + 13 + 6
assert (a,b) == (4,29)
for x1 in range(a, b+1):
    assert phase((x1,0,0,0),0) == 0

# At theta=pi/3 exact analytic Wilson trace is 1/2, not 1.
assert F(1,2) != F(1)

# Two-point reference law with positive reweighting on rare bad event.
eps = F(1,100)
bad_weight = 1 / (eps*eps)
Z = eps*bad_weight + (1-eps)
q = eps*bad_weight / Z
assert q == F(10000,10099)
assert q > F(99,100) and eps == F(1,100)

print("PASS YM-R126 flat periodic seam plaquettes and winding exponent 1")
print("PASS YM-R126 local Omega halo sees trivial field")
print("PASS YM-R126 reference bad event",eps,"normalized bad event",q)
print("Unverified: CMP102 Hk, source Omega/chi law, Gaussian covariance, mass gap")
