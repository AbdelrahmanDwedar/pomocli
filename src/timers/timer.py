"""Timer class for managing work and rest sessions."""
from time import sleep
from typing import Optional

import click


class Timer:
    def __init__(self, working_time: int, resting_time: Optional[int] = None):
        """Initialize a Timer with working and optional resting times."""
        self.working_time = working_time * 60  # Convert to seconds
        self.resting_time = resting_time * 60 if resting_time else None

    def start(self) -> None:
        """Start the timer with working and optional resting periods."""
        self._run_phase("Work", self.working_time)
        if self.resting_time:
            self._run_phase("Rest", self.resting_time)

    def _run_phase(self, label: str, total_seconds: int) -> None:
        """Render a one-second granularity countdown with visual feedback."""
        if total_seconds <= 0:
            return

        click.echo(f"Starting {label.lower()} session for {total_seconds // 60} minutes.")
        with click.progressbar(length=total_seconds, label=f"{label} progress") as progress_bar:
            for _ in range(total_seconds):
                sleep(1)
                progress_bar.update(1)
        click.echo(f"{label} session complete.")
