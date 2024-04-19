from typing import Annotated

import typer
from rich.console import Console

from ifellow_test_case import version
from ifellow_test_case.task1_random_array import max_min_mean, random_array
from ifellow_test_case.task2_hello import hello
from ifellow_test_case.task3_temp_converter import BaseConverter

app = typer.Typer(
    name="ifellow-test-case",
    help="Test case for iFellow QA Automation junior course",
    add_completion=True,
    no_args_is_help=True,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]ifellow-test-case[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command()
def main(
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the ifellow-test-case package.",
    ),
) -> None:
    """Тестовое задание для поступления на курс  iFellow QA Automation"""


@app.command()
def random_array_stats(
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Выводит детальную информацию о массиве"
    )
) -> None:
    """
    Вывод  максимального, минимального и среднего значения массива сгенерированного случайным образом
    """
    array = random_array()
    array_stats = max_min_mean(array)
    if verbose:
        console.print(
            f"Сгенерированный массив: {array}"
            + "\n"
            + f"содержит {len(array)} значений."
        )

    console.print(f"Статистические данные массива: {array_stats}")


@app.command(name="hello")
def cli_hello() -> None:
    """Поиск повторяющегося символа в слове «Hello»"""
    console.print('Повтороющийся символ в слове "Hello":', hello())


def unit_callback(value: str) -> str:
    """Проверка на корректность единицы измерения"""
    if value not in ["f", "c", "k"]:
        raise typer.BadParameter("Недопустимая еденица измерения")
    return value


@app.command(name="convert-temperature")
def cli_convert_temperature(
    temperature: Annotated[
        float,
        typer.Option(
            "--degree",
            "-d",
            prompt="Задайте температуру для конвертации:",
            help="Значение для конвертации",
        ),
    ],
    from_unit: Annotated[
        str,
        typer.Option(
            "--from",
            "-f",
            prompt="Начальная еденица измерения:\n f - Фаренгейт\n c - Цельсий\n k - Кельвин\n",
            callback=unit_callback,
            help="Начальная еденица измерения, доступны: f, c, k",
        ),
    ],
    to_unit: Annotated[
        str,
        typer.Option(
            "--to",
            "-t",
            prompt="Начальная еденица измерения:\n f - Фаренгейт\n c - Цельсий\n k - Кельвин\n",
            callback=unit_callback,
            help="Конечная еденица измерения, доступны: f, c, k",
        ),
    ],
) -> None:
    """Конвертация температуры

    :param degree: температура
    :param from_unit: из какой единицы
    :param to_unit: в какую единицу

    :return: конвертированная температура
    """
    converter = BaseConverter()
    console.print(
        f"Конвертированная температура: {converter.convert(temperature, from_unit, to_unit)} {to_unit}"
    )


if __name__ == "__main__":
    app()
