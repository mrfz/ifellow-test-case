"""Tests for task1"""

import pytest

from ifellow_test_case.task1_random_array import max_min_mean, random_array


def test_random_array():
    """Тестируем функцию random_array"""
    test_array: list[float] = random_array()
    assert isinstance(test_array, list)
    assert len(test_array) > 0
    assert all(isinstance(x, float) for x in test_array)


def test_max_min_mean():
    """Тестируем функцию max_min_mean"""
    assert type(max_min_mean()) is dict
