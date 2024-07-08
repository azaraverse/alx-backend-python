#!/usr/bin/env python3
"""Returning an async task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int):
    """"""
    return asyncio.create_task(wait_random(max_delay))
