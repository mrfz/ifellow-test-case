"""Tests for task1"""

import pytest

from ifellow_test_case.task1_random_array import max_min_mean, random_array


def test_random_array():
    """Тестируем функцию random_array"""
    assert type(random_array()) is list


def test_max_min_mean():
    """Тестируем функцию max_min_mean"""
    assert type(max_min_mean()) is dict
