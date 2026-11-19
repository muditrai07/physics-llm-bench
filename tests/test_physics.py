from math import isclose
from bench.physics import two_body_momentum

def test_massless_daughters():
    # each massless daughter carries M/2
    assert isclose(two_body_momentum(10, 0, 0), 5)

def test_at_threshold():
    # no phase space when m1 + m2 = M
    assert two_body_momentum(10, 5, 5) == 0
