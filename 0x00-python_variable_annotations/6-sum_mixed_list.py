#!/usr/bin/env python3
"""
Typed-Annotated function: sum_mixed_list()
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Type-Annotated function: sum_mixed_list().

    Takes a list of integers and floats and returns their sum as a float

    Args:
            mxd_list (list of int, float): List of integers and floats

    Return:
            Sum of mxd_list as a float.
    """
    return sum(mxd_lst)
