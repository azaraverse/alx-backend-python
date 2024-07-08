#!/usr/bin/env python3
"""Measuring async runtime"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n module and returns
    total time elapsed / n

    Args:
        n (int): Number of times wait_random is spawned in wait_n.
        max_delay (int): The maximum delay time for wait_random

    Returns:
        float: Average delay time
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start

    return elapsed/n


# n = 5
# max_delay = 9
# print(measure_time(n, max_delay))
