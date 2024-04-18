"""Решение задачи 1 - "Случайный массив"""

"""
Задание: 
Сформировать и заполнить массив случайным числами и вывести максимальное,
минимальное и среднее значение.
Для генерации случайного числа использовать метод `Math.random()`, который возвращает
значение в промежутке [0, 1].

Описание решения задачи:
Для решения создадим 2 функции: 
random_array для создания массива случайных элементов от 0 до 1.  
max_min_mean - для нахождения максимального, минимального и среднего значения.

Вызов функции производится в консоли с помощью команды random-array-stats
"""

from random import random


def random_array() -> list[float]:
    """
    Создание массива случайных элементов от 0 до 1

    Количество элементов в массиве зададим случайным образом по функции random
    """
    number_of_elements: int = int(random() * 100) + 1
    output: list[float] = list(random() for _ in range(number_of_elements))

    return output


def max_min_mean(array: list[float]) -> dict[str, float]:
    """Нахождение максимального, минимального и среднего значения

    :param array: массив случайных элементов от 0 до 1
    :return: словарь с максимальным, минимальным и средним значениями
    """
    output: dict[str, float] = {
        "max": max(array),
        "min": min(array),
        "mean": sum(array) / len(array),
    }

    return output
