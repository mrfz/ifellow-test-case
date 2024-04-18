# ifellow-test-case

[![Build status](https://github.com/mrfz/ifellow-test-case/workflows/build/badge.svg?branch=master&event=push)](https://github.com/mrfz/ifellow-test-case/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/ifellow-test-case.svg)](https://pypi.org/project/ifellow-test-case/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/mrfz/ifellow-test-case/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/mrfz/ifellow-test-case/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/mrfz/ifellow-test-case/releases)
[![License](https://img.shields.io/github/license/mrfz/ifellow-test-case)](https://github.com/mrfz/ifellow-test-case/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Тестовое задание для поступления на курс  iFellow QA Automation

## 📖 Список задач

- [ ] Задача 1. Случайный массив
- [ ] Задача 2. Hello
- [ ] Задача 3. Конвертер температуры
- [ ] Задача 4. Угол между стрелками часов

## Описание задач

### Задача 1. Случайный массив

#### Условие

Сформировать и заполнить массив случайным числами и вывести максимальное,
минимальное и среднее значение.
Для генерации случайного числа использовать метод `Math.random()`, который возвращает
значение в промежутке [0, 1].

#### Реализация

В файле `ifellow_test_case\task1_random_array.py` реализовано две функции, для решения задачи:
`random_array` для создания массива случайных элементов от 0 до 1.  
`max_min_mean` - для нахождения максимального, минимального и среднего значения.

Вызов функций реализован в командой строке модуля `ifellow-test-case random-array-stats`.

### Задача 2. Hello

#### Условие

Написать программу, которая должна найти и вывести повторяющийся символ в слове
«Hello»

### Задача 3. Конвертер температуры

#### Условие

Напишите класс BaseConverter для конвертации из градусов по Цельсию в
Кельвины, Фаренгейты, и так далее. У метода должен быть метод convert, который
и делает конвертацию.
При запуске кода должна быть возможность ввести градусы Цельсия и выбора
конвертации в Кельвины или Фаренгейты

### Задача 4. Угол между стрелками часов

#### Условие

Напишите метод, который будет вычислять угол между часовой и минутной стрелками
часов. На вход функции подаётся время в виде двух переменных: `hours` и `minutes`.
Расчет угла производить относительно реального поведения стрелок часов.

## 🛡 Лицензия

[![License](https://img.shields.io/github/license/mrfz/ifellow-test-case)](https://github.com/mrfz/ifellow-test-case/blob/master/LICENSE)

Этот проект лицензирован в рамках лицензии `MIT`. Подробности указаны в файле [Лицензии](https://github.com/mrfz/ifellow-test-case/blob/master/LICENSE)
This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/mrfz/ifellow-test-case/blob/master/LICENSE) for more details.

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

Шаблон этого проекта сгенерирован [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) с помощью шалона  [`python-package-template`](https://github.com/TezRomacH/python-package-template)
