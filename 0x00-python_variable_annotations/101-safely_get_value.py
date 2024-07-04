#!/usr/bin/env python3
"""
Type-Annotated function: safely_get_value()
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None]
) -> Union[Any, T]:
    """
    Augmenting the function with type annotations Mapping, Any, Union
    """
    if key in dct:
        return dct[key]
    else:
        return default
