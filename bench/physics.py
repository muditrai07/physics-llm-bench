from math import sqrt

def two_body_momentum(M, m1, m2):
    """Daughter momentum in the rest frame for the decay M -> m1 + m2 (natural units)."""
    return sqrt((M**2 - (m1 + m2)**2) * (M**2 - (m1 - m2)**2)) / (2 * M)
