#!/usr/bin/env python3
"""
Concurrent coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns
    the list of all delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random
        max_delay (int): The maximum delay for wait_random

    Returns:
        List[float]: A list of delays in ascending order
    """
    lst = []
    for _ in range(n):
        lst.append(wait_random(max_delay))

    delays = await asyncio.gather(*lst)

    return sorted(delays)