#!/usr/bin/env python3
"""
Annotating an existing function
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a tuple of element with the element and length of each element
    """
    return [(i, len(i)) for i in lst]
