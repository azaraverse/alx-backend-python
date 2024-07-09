#!/usr/bin/env python3
"""Async Comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that collects 10 random numbers using an async and
    comprehensing over an async generator.

    Returns:
        List[float]: 10 random numbers.
    """
    result: List = [i async for i in async_generator()]

    return result
