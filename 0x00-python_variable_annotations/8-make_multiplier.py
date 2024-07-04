#!/usr/bin/env python3
"""
Type-Annotated function: make_multiplier()
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-Annotated function: make_multiplier()

    Takes a float as argument and returns a function that multiplies a
    float by the argument.

    Args:
            multiplier (float): Argument serving as multiplier
    Return:
            A function that multiplies a float by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Callable function: multiplier_function()

        Takes a float and returns the product of the float and the
        multiplier

        Args:
                value (float): To be multiplied by multiplier
        Return:
                Product of value and multiplier.
        """
        return value * multiplier
    return multiplier_function
