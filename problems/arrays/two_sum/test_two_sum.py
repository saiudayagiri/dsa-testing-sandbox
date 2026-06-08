import pytest
from .solution import two_sum

def test_nominal_target_match():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

# --- STUDENTS MUST COMPLETE THEIR MANUALLY INSIGHTFUL TEST CASES BELOW ---
