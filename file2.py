"""Example file 2."""

from typing import Generator


def do_something_else() -> Generator[int, int, str]:
    """I need a better docstring."""
    yield 123
    yield 345
    return "Done"
