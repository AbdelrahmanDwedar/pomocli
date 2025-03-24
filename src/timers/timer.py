from time import sleep
from typing import Optional


class Timer:
    def __init__(self, working_time: int, resting_time: Optional[int] = None):
        """Initialize a Timer with working and optional resting times."""
        self.working_time = working_time * 60  # Convert to seconds
        self.resting_time = resting_time * 60 if resting_time else None

    def start(self) -> None:
        """Start the timer with working and optional resting periods."""
        self._start_working_timer()
        if self.resting_time:
            self._start_resting_timer()

    def _start_working_timer(self) -> None:
        """Start the working timer."""
        print(f"Working for {self.working_time} seconds...")
        sleep(self.working_time)

    def _start_resting_timer(self) -> None:
        """Start the resting timer."""
        print(f"Resting for {self.resting_time} seconds...")
        if self.resting_time is not None:
            sleep(self.resting_time)
