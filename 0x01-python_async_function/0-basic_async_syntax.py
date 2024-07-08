#!/usr/bin/env python3
"""
Async coroutine that waits for a random delay and returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns
    it

    Args:
        max_delay (int): The maximu delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay time in seconds.
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)

    return rand


# asyncio.run(wait_random())
