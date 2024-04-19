"""Решение задачи 3 - "Конвертер температуры"""

"""
Задание:
Напишите класс BaseConverter для конвертации из градусов по Цельсию в
Кельвины, Фаренгейты, и так далее. У метода должен быть метод convert, который
и делает конвертацию.
При запуске кода должна быть возможность ввести градусы Цельсия и выбора
конвертации в Кельвины или Фаренгейты

Описание решения задачи:
Создадим класс BaseConverter с методом convert, который будет делать конвертацию.
При инициализации создадим атрибуты f_to_c, c_to_f, c_to_k в которых будут константы для перевода значений

При ошибочном задании едениц измерения функция напечататет в консоль "неверное значение" и вернет входное значение

Логику выбора реализуем в консоли, для проверки входных данных там и возможности интерактивного использования

"""


class BaseConverter:
    """Конвертер температуры"""

    def __init__(self):
        self.f_to_c = 5 / 9
        self.c_to_f = 9 / 5
        self.c_to_k = 273.15

    def convert(self, temperature: float, from_unit: str, to_unit: str) -> float:
        """Конвертация температуры


        Args:
            temperature (float): температура
            from_unit (str): из какой единицы, можно выбрать: f, c, k
            to_unit (str): в какую единицу, можно выбрать: f, c, k

        Raises:
            ValueError: неверное значение единицы измерения
            ValueError: Температура не может быть меньше абсолютного нуля 0 k

        Returns:
            float: конвертированная температура
        """

        if from_unit not in ["f", "c", "k"] or to_unit not in ["f", "c", "k"]:
            raise ValueError("Неверное значение единицы измерения")

        if (
            (temperature < -273.15 and from_unit == "c")
            or (temperature < -119.75 and from_unit == "f")
            or (temperature < 0 and from_unit == "k")
        ):
            raise ValueError("Температура не может быть меньше абсолютного нуля 0 k")

        if from_unit == "f" and to_unit == "c":
            return (temperature - 32) * self.f_to_c
        elif from_unit == "f" and to_unit == "k":
            return (temperature - 32) * self.f_to_c + self.c_to_k
        elif from_unit == "c" and to_unit == "f":
            return temperature * self.c_to_f + 32
        elif from_unit == "c" and to_unit == "k":
            return temperature + self.c_to_k
        elif from_unit == "k" and to_unit == "c":
            return temperature - self.c_to_k
        elif from_unit == "k" and to_unit == "f":
            return (temperature - self.c_to_k) * self.f_to_c + 32
        else:

            return temperature
