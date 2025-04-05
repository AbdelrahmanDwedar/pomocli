import pytest
from timers.timer import Timer


def test_timer_with_rest(mocker):
    mock_sleep = mocker.patch(
        "timers.timer.sleep", return_value=None
    )  # Mock sleep to avoid delays
    timer = Timer(working_time=1, resting_time=1)
    timer.start()
    mock_sleep.assert_has_calls(
        [mocker.call(60), mocker.call(60)]
    )  # 1 minute = 60 seconds


def test_timer_without_rest(mocker):
    mock_sleep = mocker.patch("timers.timer.sleep", return_value=None)
    timer = Timer(working_time=1)
    timer.start()
    mock_sleep.assert_called_once_with(60)
