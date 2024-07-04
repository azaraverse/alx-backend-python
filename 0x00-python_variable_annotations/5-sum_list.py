#!/usr/bin/env python3
"""
Type-Annotated function: sum_list()
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Type-Annotated function: sum_list().

    Takes a list of floats as arguments and returns their sum as float.

    Args:
            input_list([float]): List of floats to sum.

    Returns:
            Sum of arguments in input_list as a float.
    """
    return sum(input_list)
