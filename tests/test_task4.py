"""Test for task4"""

import pytest

from ifellow_test_case.task4_clock_hands_angle import hands_angle


@pytest.mark.parametrize(
    ("hours", "minutes", "expected_result"),
    (
        (0, 0, 0.0),
        (0, 30, 165.0),
        (0, 45, 247.5),
        (14, 0, 300),
    ),
)
def test_task4(hours, minutes, expected_result):
    """Тестируем функцию hands_angle()"""
    assert hands_angle(hours, minutes) == expected_result


def test_task4_exception():
    """Тестируем функцию hands_angle() с исключениями"""
    with pytest.raises(ValueError):
        hands_angle(24, 90)
