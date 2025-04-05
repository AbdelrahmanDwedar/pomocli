import pytest
from timers.factory import TimerFactory


def test_create_timer_with_preset():
    timer = TimerFactory.create_timer(preset="normal")
    assert timer.working_time == 25 * 60
    assert timer.resting_time == 5 * 60


def test_create_timer_with_custom_times():
    timer = TimerFactory.create_timer(working_time=45, resting_time=15)
    assert timer.working_time == 45 * 60
    assert timer.resting_time == 15 * 60


def test_create_timer_invalid_preset():
    with pytest.raises(ValueError, match="Invalid preset: invalid"):
        TimerFactory.create_timer(preset="invalid")


def test_create_timer_missing_arguments():
    with pytest.raises(
        ValueError, match="Either a preset or working_time must be provided."
    ):
        TimerFactory.create_timer()
