#!/usr/bin/env python3
"""Module for creating a tuple from a string and a squared number."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of an int or float as a float."""
    return (k, float(v ** 2))
