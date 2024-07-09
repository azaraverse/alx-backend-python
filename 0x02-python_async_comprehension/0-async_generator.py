#!/usr/bin/env python3
"""Async Generator"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields a random number between 0 and 10
    after asynchronously waiting for 1 second, a total of 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
