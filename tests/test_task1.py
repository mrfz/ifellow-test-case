"""Tests for task1"""

import pytest

from ifellow_test_case.task1_random_array import max_min_mean, random_array


def test_random_array():
    """Тестируем функцию random_array"""
    test_array: list[float] = random_array()
    assert isinstance(test_array, list)
    assert len(test_array) > 0
    assert all(isinstance(x, float) for x in test_array)


@pytest.mark.parametrize(
    ("array", "expected_max", "expected_min", "expected_mean"),
    (
        ([0.1, 0.2, 0.3], 0.3, 0.1, sum([0.1, 0.2, 0.3]) / 3),
        ([0.1], 0.1, 0.1, 0.1),
    ),
)
def test_max_min_mean(array, expected_max, expected_min, expected_mean):
    """Тестируем функцию max_min_mean"""
    test_dict: dict[str, float] = max_min_mean(array)
    assert isinstance(test_dict, dict)
    assert len(test_dict) == 3
    assert test_dict == {
        "max": expected_max,
        "min": expected_min,
        "mean": expected_mean,
    }
