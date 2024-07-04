#!/usr/bin/env python3
"""
Type-Annotated function: to_kv()
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Type-Annotated function: to_kv().

    Takes a string and an int OR float as arguments and returns a tuple.

    Args:
            k (str): First return value of the tuple
            v (int | float): Second return value of the tuple

    Return:
        A tuple annotated as a str and a float.
    """
    return (k, v ** 2)
