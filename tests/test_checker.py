from bench.checker import check
import math
import re
import pint
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

def test_exact_answer_is_correct():
    assert check("blah blah\nFINAL: 2.85 MeV", 2.85, "MeV", 0.02) == "correct"

def test_wrong_dimension():
    assert check("FINAL: 2.85 cm", 2.85, "MeV", 0.02) == "wrong_units"


def test_other_units():
    assert check("FINAL: 0.0041 GeV", 4.1, "MeV", 0.02) == "correct"

def test_within_tolerance():
    # 2.88 is ~1% above 2.85; tolerance is 2% → should pass
    assert check("FINAL: 2.88 MeV", 2.85, "MeV", 0.02) == "correct"

def test_outside_tolerance():
    # 2.99 is ~5% above 2.85; tolerance is 2% → should fail
    assert check("FINAL: 2.99 MeV", 2.85, "MeV", 0.02) == "wrong_value" 



def test_no_final_line():
    response = "The width is about 2.85 MeV, from the beta^3 suppression."
    assert check(response, 2.85, "MeV", 0.02) == "no_answer"


def test_garbage_after_final():
    assert check("FINAL: about four MeV", 4.0, "MeV", 0.02) == "unparseable"


def test_last_final_line_counts():
    response = (
        "First attempt.\n"
        "FINAL: 3.5 MeV\n"
        "Wait, I forgot the beta^3 factor. Correcting:\n"
        "FINAL: 2.85 MeV"
    )
    assert check(response, 2.85, "MeV", 0.02) == "correct"


def test_scientific_notation():
    assert check("FINAL: 4.1e-3 GeV", 4.1, "MeV", 0.02) == "correct"