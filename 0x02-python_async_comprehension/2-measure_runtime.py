#!/usr/bin/env python3
"""Measuring Async Runtime"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Measures the total runtime of executing four async_comprehensions
    in parallel.

    Total runtime should roughly hit 10 seconds instead of 40 seconds
    due to the asychronous way of executing the tasks using asyncio.gather

    Returns:
        Float: Total runtime
    """
    start = time.perf_counter()
    execution = [
        async_comprehension() for _ in range(4)
    ]
    await asyncio.gather(*execution)
    elapsed = time.perf_counter() - start

    return elapsed
