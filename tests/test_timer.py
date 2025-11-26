"""Tests for the Timer class."""
import pytest
from timers.timer import Timer


def test_timer_with_rest(mocker):
    mock_sleep = mocker.patch(
        "timers.timer.sleep", return_value=None
    )  # Mock sleep to avoid delays
    timer = Timer(working_time=1, resting_time=1)
    timer.start()
    # Timer uses sleep(1) in a loop: 60 times for work + 60 times for rest = 120 calls
    assert mock_sleep.call_count == 120
    # Verify all calls are with 1 second
    for call in mock_sleep.call_args_list:
        assert call == mocker.call(1)


def test_timer_without_rest(mocker):
    mock_sleep = mocker.patch("timers.timer.sleep", return_value=None)
    timer = Timer(working_time=1)
    timer.start()
    # Timer uses sleep(1) in a loop 60 times for 1 minute
    assert mock_sleep.call_count == 60
    # Verify all calls are with 1 second
    for call in mock_sleep.call_args_list:
        assert call == mocker.call(1)
