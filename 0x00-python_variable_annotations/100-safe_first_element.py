#!/usr/bin/env python3
"""
Duck-Typed Annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Augmented the function with required duct-type annotations
    """
    if lst:
        return lst[0]
    else:
        return None
