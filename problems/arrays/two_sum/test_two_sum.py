import pytest
from .solution import two_sum

def test_nominal_target_match() -> None:
    """Verify standard positive integers map correctly."""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_negative_integer_elements() -> None:
    """Verify system computes correctly with negative integer parameters."""
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]

def test_duplicate_element_values() -> None:
    """Verify indices return appropriately when duplicate matching values exist."""
    assert two_sum([3, 2, 4], 6) == [1, 2]
