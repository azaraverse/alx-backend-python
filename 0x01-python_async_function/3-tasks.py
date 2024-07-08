#!/usr/bin/env python3
"""Returning an async task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an argument ans returns a asyncio.Task

    Args:
        max_delay (int): The maximum delay time for wait_random

    Returns:
        An asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
