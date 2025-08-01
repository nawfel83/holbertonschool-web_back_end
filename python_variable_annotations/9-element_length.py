#!/usr/bin/env python3
"""Module for getting the length of elements in an iterable."""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with elements and their lengths."""
    return [(i, len(i)) for i in lst]