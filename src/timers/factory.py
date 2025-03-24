from typing import Optional
from .timer import Timer


class TimerFactory:
    PRESETS = {
        "normal": {"working_time": 25, "resting_time": 5},
        "single": {"working_time": 60, "resting_time": 12},
        "half": {"working_time": 30, "resting_time": 6},
        "tripartite": {"working_time": 180, "resting_time": 36},
        "quarterly": {"working_time": 15, "resting_time": 3},
    }

    @staticmethod
    def create_timer(preset: Optional[str] = None, working_time: Optional[int] = None, resting_time: Optional[int] = None) -> Timer:
        """Create a Timer instance based on a preset or custom times."""
        if preset:
            if preset not in TimerFactory.PRESETS:
                raise ValueError(f"Invalid preset: {preset}")
            config = TimerFactory.PRESETS[preset]
            return Timer(working_time=config["working_time"], resting_time=config["resting_time"])
        elif working_time is not None:
            return Timer(working_time=working_time, resting_time=resting_time)
        else:
            raise ValueError("Either a preset or working_time must be provided.")
