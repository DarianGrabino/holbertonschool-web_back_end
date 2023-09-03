#!/usr/bin/env python3
"""Asynchronous routine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """that takes an argument and waits for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
