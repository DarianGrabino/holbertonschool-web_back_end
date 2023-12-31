#!/usr/bin/env python3
"""Async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """Create lists and add the delay to the right place in the sorted list"""
    tasks = []
    delays = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
