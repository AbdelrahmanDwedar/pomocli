import pytest
from click.testing import CliRunner
from main import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_start_with_preset(mocker, runner):
    mock_sleep = mocker.patch("timers.timer.sleep", return_value=None)
    result = runner.invoke(cli, ["start", "--preset", "normal"])
    assert result.exit_code == 0
    assert mock_sleep.call_count == (25 * 60) + (5 * 60)


def test_start_with_custom_times(mocker, runner):
    mock_sleep = mocker.patch("timers.timer.sleep", return_value=None)
    result = runner.invoke(cli, ["start", "--work-time", "45", "--rest-time", "15"])
    assert result.exit_code == 0
    assert mock_sleep.call_count == (45 * 60) + (15 * 60)


def test_start_with_invalid_preset(runner):
    result = runner.invoke(cli, ["start", "--preset", "invalid"])
    assert result.exit_code != 0
    assert "Invalid preset" in result.output


def test_start_with_missing_arguments(runner):
    result = runner.invoke(cli, ["start"])
    assert result.exit_code != 0
    assert "Error" in result.output
