#!/usr/bin/env python3
"""Async function sintax"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """Take wait_n and modify it into a new function task_wait_n""""
    tasks = []
    delays = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
