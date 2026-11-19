import numpy as np

def two_body_momentum(M, m1, m2):
    """Daughter momentum in the rest frame for the decay M -> m1 + m2 (natural units)."""
    return np.sqrt((M**2 - (m1 + m2)**2) * (M**2 - (m1 - m2)**2)) / (2 * M)



def width_scalar_to_fermions(m_phi, m_f, y):
    """Width of a real scalar decaying to a Dirac fermion pair via the Yukawa coupling y."""
    beta = np.sqrt(1 - 4 * m_f**2 / m_phi**2)
    return y**2 * m_phi * beta**3 / (8 * np.pi)

def breit_wigner(s, M, Gamma):
    """Relativistic Breit-Wigner line shape: 1 / ((s - M^2)^2 + M^2 Gamma^2).
    s in GeV^2; M and Gamma in GeV. Unnormalized."""
    return 1 / ((s - M**2)**2 + (M * Gamma)**2)


def relic_abundance(sigma_v):
    """Rough thermal-relic estimate: Omega h^2 ~ 0.1 * (3e-26 cm^3/s) / <sigma v>.
    sigma_v in cm^3/s."""
    return 0.1 * 3e-26 / sigma_v