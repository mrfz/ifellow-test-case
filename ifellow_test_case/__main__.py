import typer
from rich.console import Console

from ifellow_test_case import version
from ifellow_test_case.task1_random_array import max_min_mean, random_array
from ifellow_test_case.task2_hello import hello

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


if __name__ == "__main__":
    app()
