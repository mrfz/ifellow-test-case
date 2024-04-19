"""Tests for typer application"""

from typer.testing import CliRunner

from ifellow_test_case.__main__ import app

runner = CliRunner()


def test_app():
    """Test typer application"""
    result = runner.invoke(app)
    assert result.exit_code == 0


def test_app_task1():
    """Test typer application with task 1"""
    result = runner.invoke(app, ["random-array-stats"])
    assert result.exit_code == 0


def test_app_task2():
    """Test typer application with task 2"""
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert result.output == 'Повтороющийся символ в слове "Hello": l\n'


# TODO реализовать тесты для ввода параметров.
# Пока не получается передать input для нескольких значений
def test_app_task3():
    """Test typer application with task 3"""
    pass
