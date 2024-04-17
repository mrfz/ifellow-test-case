import typer
from rich.console import Console

from ifellow_test_case import version

app = typer.Typer(
    name="ifellow-test-case",
    help="Test case for iFellow QA Automation junior course",
    add_completion=True,
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


if __name__ == "__main__":
    app()
