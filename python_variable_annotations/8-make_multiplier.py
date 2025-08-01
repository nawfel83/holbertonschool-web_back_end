#!/usr/bin/env python3
"""Module for creating a multiplier function."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiply(n: float) -> float:
        """Multiply a float by the multiplier."""
        return n * multiplier
    return multiply
