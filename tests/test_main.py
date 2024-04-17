"""Tests for typer application"""

from typer.testing import CliRunner

from ifellow_test_case.__main__ import app

runner = CliRunner()


def test_app():
    """Test typer application"""
    result = runner.invoke(app)
    assert result.exit_code == 0
