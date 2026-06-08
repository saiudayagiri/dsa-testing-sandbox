import pytest

from .solution import two_sum


def test_nominal_target_match() -> None:
    """Verify standard positive integers map correctly to the target sum."""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_negative_integer_elements() -> None:
    """Ensure negative values and zero states evaluate without breaking index lookup."""
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]


def test_duplicate_element_values() -> None:
    """Verify system handles duplicate element constraints gracefully."""
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_large_array_constraints() -> None:
    """Test boundary execution constraints with maximum distance spacing."""
    large_input = [1000] * 100
    large_input[15] = 5
    large_input[85] = 10
    assert two_sum(large_input, 15) == [15, 85]
