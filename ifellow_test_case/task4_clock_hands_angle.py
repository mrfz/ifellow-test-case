"""Решение задачи 4"""

"""
Задание:
Напишите метод, который будет вычислять угол между часовой и минутной стрелками
часов. На вход функции подаётся время в виде двух переменных: `hours` и `minutes`.
Расчет угла производить относительно реального поведения стрелок часов.

Описание решения задачи:
В функции hands_angle() расчитаем угол каждой из стрелок по отдельности:
- угол часовой стрелки изменяется на  360/12=30 за каждый час и на 360/12/60 = 0.5 за каждую минуту
- угол минутной стрелки изменяется на 360/60=6 за каждую минуту

угол между часовой и минутной стрелками часов расчитаем по ходу движения часовой стрелки
"""


def hands_angle(hours: int, minutes: int) -> float:
    """Возвращает угол между часовой и минутной стрелками часов.

    Args:
        hours (int): часы
        minutes (int): минуты

    Raises:
        ValueError: ошибка ввода времени

    Returns:
        float: угол между часовой и минутной стрелками по ходу движения часовой стрелки
    """

    if hours < 0 or minutes < 0 or hours > 23 or minutes > 59:
        raise ValueError("Неправильно указано время")

    hours_hand_angle = (hours * 30 + minutes * 0.5) % 360
    minutes_hand_angle = minutes * 6

    if hours_hand_angle < minutes_hand_angle:
        hands_angle = minutes_hand_angle - hours_hand_angle
    elif hours_hand_angle > minutes_hand_angle:
        hands_angle = 360 - hours_hand_angle + minutes_hand_angle
    else:
        hands_angle = 0

    return hands_angle
