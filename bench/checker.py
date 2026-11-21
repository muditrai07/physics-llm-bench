import math
import re
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


def extract_final(text):
    """Return what follows the LAST 'FINAL:' line in a model response, or None if there isn't one."""
    matches = re.findall(r"FINAL:\s*(.+)", text)
    if not matches:
        return None
    return matches[-1].strip(" *`")


def parse_quantity(s):
    """Turn a string like '4.1 MeV' into a pint Quantity. Return None if it can't be parsed."""
    try:
        return Q_(s)
    except Exception:
        # Model output can be malformed in many ways (unknown units, stray words, bad syntax).
        # Any failure to parse counts as 'unparseable'.
        return None


def check(response_text, answer_value, answer_unit, rel_tol):
    """Grade one model response. Returns one of:
    'correct', 'wrong_value', 'wrong_units', 'no_answer', 'unparseable'."""
    final = extract_final(response_text)
    if final is None:
        return "no_answer"

    q = parse_quantity(final)
    if q is None:
        return "unparseable"

    try:
        got = q.to(answer_unit).magnitude
    except pint.DimensionalityError:
        return "wrong_units"

    if not math.isfinite(got):            # catches nan and inf
        return "wrong_value"
    if math.isclose(got, answer_value, rel_tol=rel_tol):
        return "correct"
    return "wrong_value"