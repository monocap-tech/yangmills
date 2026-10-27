"""YM-R118 exact four-edge contour/curl certificate; not a Yang-Mills proof."""
from fractions import Fraction as F

# Sites: (0,0),(1,0),(1,1),(0,1).
# Bonds: bottom, right, top (01->11), left (00->01).
grad = ((-1,1,0,0), (0,-1,1,0), (0,0,1,-1), (-1,0,0,1))
old = (F(1),F(1),F(0),F(0))
sym = (F(1,2),)*4
curl = (F(1),F(1),F(-1),F(-1))
diff = tuple(a-b for a,b in zip(sym,old))
assert diff == tuple(-x/2 for x in curl)
assert tuple(sum(curl[b]*grad[b][i] for b in range(4)) for i in range(4)) == (0,0,0,0)
assert tuple(sum(diff[b]*grad[b][i] for b in range(4)) for i in range(4)) == (0,0,0,0)
assert sum(x*x for x in old) == 2
assert sum(x*x for x in sym) == 1
test = (F(0),F(1),F(0),F(0))
assert sum(diff[b]*test[b] for b in range(4)) == F(-1,2)
assert sum(curl[b]*test[b] for b in range(4)) == 1
print("PASS R118 exact contour/curl certificate")
print("difference:",diff,"curl annihilates gradients")
print("one-row norm squared: old=2 symmetric=1")
