"""YM-R124 finite SU2 flat torus and winding-retention certificate.

Exact math in pass; numerical SU2 diagonal exponentials here tested with
floating tolerance. Native source cutoff/normalization NOT inferred.
"""
from cmath import exp
from math import pi, cos, isclose
L, N = 13, 13**3
theta = pi/3
assert N % L == 0

def dplus(angle):
    return exp(1j*angle)
u = dplus(theta / N)
# Constant commuting e1 links, all other directions identity:
# any e1/transverse plaquette: u*1*u^{-1}*1=1.
plaquette = u*u.conjugate()
assert abs(plaquette-1) < 1e-12
winding = u**N
coarse_link = u**L
coarse_winding = coarse_link**(N//L)
assert abs(winding - exp(1j*theta)) < 1e-11
assert abs(coarse_winding - winding) < 1e-11
assert isclose(winding.real, .5, abs_tol=1e-11)
assert not isclose(winding.real, 1, abs_tol=1e-11)
# With zero plaquette curvature the true M of CMP109 equals straight U(c)
# on every eligible contractible source ribbon, not the identity connection.
assert abs(coarse_link-1) > 0
assert abs(u**6-1) < .003

# Explicit telescoping on a winding chain: the norm of product error
# cannot exceed sum of norms of differences between unitary factors.
epsilon_edge = 1e-6
perturbed_coarse = coarse_link*exp(1j*epsilon_edge)
left = abs(perturbed_coarse**(N//L)-coarse_winding)
right = (N//L)*abs(perturbed_coarse-coarse_link)
assert left <= right+1e-11

# R122 constant one-step curvature chart: declared sample eta only.
C = 31878/169
eta=1e-7
assert 666*eta < 1
delta=C*eta/(1-666*eta)
assert 0 < delta < 1
print("PASS R124 flat plaquette=I with winding trace",winding.real)
print("PASS R124 nonlinear CMP109 flat coarse winding retention",coarse_winding.real)
print("PASS R124 n-link SU2 product telescoping",left,right)
print("PASS R124 conditional winding upper n*delta",(N//L)*delta)
print("NO source epsilon, Omega coverage, actual UV probability law or gap proved")
