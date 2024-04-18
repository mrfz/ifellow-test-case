"""Test for task2"""

import pytest

from ifellow_test_case.task2_hello import hello


def test_hello():
    """Тестируем функцию hello"""
    test_value = hello()
    assert len(test_value) == 1
    assert test_value == "l"
