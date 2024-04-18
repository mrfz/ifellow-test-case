"""test for task3"""

import pytest

from ifellow_test_case.task3_temp_converter import BaseConverter


@pytest.mark.parametrize(
    ("temperature", "from_unit", "to_unit", "expected_result"),
    (
        (32, "f", "c", 0),
        (0, "c", "f", 32),
        (0, "c", "k", 273.15),
        (273.15, "k", "c", 0),
        (32, "f", "k", 273.15),
        (273.15, "k", "f", 32),
        (0, "a", "f", 0),
    ),
)
def test_task3(temperature, from_unit, to_unit, expected_result):
    """Тестируем класс BaseConverter"""
    test_class: BaseConverter = BaseConverter()
    assert test_class.c_to_f == 9 / 5
    assert test_class.f_to_c == 5 / 9
    assert test_class.c_to_k == 273.15

    assert (
        test_class.convert(
            temperature=temperature, from_unit=from_unit, to_unit=to_unit
        )
        == expected_result
    )
