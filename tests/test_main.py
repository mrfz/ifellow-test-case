"""Tests for typer application"""

from typer.testing import CliRunner

from ifellow_test_case.__main__ import app

runner = CliRunner()


def test_app():
    """Test typer application"""
    result = runner.invoke(app)
    assert result.exit_code == 2


def test_app_task1():
    """Test typer application with task 1"""
    result = runner.invoke(app, ["random-array-stats"])
    assert result.exit_code == 0
