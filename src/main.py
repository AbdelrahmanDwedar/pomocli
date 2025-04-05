import click
from typing import Optional
from timers.factory import TimerFactory


@click.group()
def cli():
    """PomoCLI: A CLI tool for managing work and rest timers."""
    pass


@cli.command()
@click.option(
    "--preset",
    "-p",
    type=click.Choice(
        ["normal", "single", "half", "tripartite", "quarterly"], case_sensitive=False
    ),
    help="Choose a preset timer configuration.",
)
@click.option(
    "--work-time",
    "-w",
    type=int,
    help="Custom working time in minutes.",
)
@click.option(
    "--rest-time",
    "-r",
    type=int,
    help="Custom resting time in minutes (optional).",
)
def start(preset: Optional[str], work_time: Optional[int], rest_time: Optional[int]):
    """Start a timer with a preset or custom times."""
    try:
        timer = TimerFactory.create_timer(
            preset=preset, working_time=work_time, resting_time=rest_time
        )
        timer.start()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    cli()
