#!/usr/bin/env python3
"""Function that takes an integer and returns asyncio.Task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function task_wait_random that takes an integer
    max_delay and returns a asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))
