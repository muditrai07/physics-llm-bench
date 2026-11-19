from math import isclose
import numpy as np
import pytest
from bench.physics import two_body_momentum,breit_wigner,width_scalar_to_fermions,relic_abundance

def test_massless_daughters():
    # each massless daughter carries M/2
    assert isclose(two_body_momentum(10, 0, 0), 5)

def test_at_threshold():
    # no phase space when m1 + m2 = M
    assert two_body_momentum(10, 5, 5) == 0


def test_breit_wigner_half_max():
    M, Gamma = 91.19, 2.50   # Z boson, GeV
    peak = breit_wigner(M**2, M, Gamma)
    assert breit_wigner(M**2 + M * Gamma, M, Gamma) == pytest.approx(peak / 2)

def test_width_massless_limit():
    # beta -> 1: Gamma = y^2 m_phi / (8 pi)
    assert width_scalar_to_fermions(100, 0, 1) == pytest.approx(100 / (8 * np.pi))

def test_width_vanishes_at_threshold():
    assert width_scalar_to_fermions(100, 50, 1) == pytest.approx(0, abs=1e-12)

def test_width_scales_as_y_squared():
    assert width_scalar_to_fermions(100, 10, 2) == pytest.approx(4 * width_scalar_to_fermions(100, 10, 1))

def test_width_decreases_with_fermion_mass():
    m_f = np.linspace(0, 49, 100)            
    widths = width_scalar_to_fermions(100, m_f, 1)
    assert np.all(np.diff(widths) < 0)
        

def test_relic_benchmark_value():
    assert relic_abundance(3e-26) == pytest.approx(0.1)

def test_relic_inverse_scaling():
    sv = np.logspace(-27, -24, 10)
    assert relic_abundance(sv) * sv == pytest.approx(0.1 * 3e-26)

def test_breit_wigner_peak_height():
    M, Gamma = 91.19, 2.50
    assert breit_wigner(M**2, M, Gamma) == pytest.approx(1 / (M * Gamma)**2)

def test_breit_wigner_symmetric():
    M, Gamma, d = 91.19, 2.50, 30.0
    assert breit_wigner(M**2 + d, M, Gamma) == pytest.approx(breit_wigner(M**2 - d, M, Gamma))