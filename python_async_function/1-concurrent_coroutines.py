#!/usr/bin/env python3
"""Async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """We create a list to store the delays in ascending order"""
    delays = []

    async def helper(delay: float):
        """We add the delay to the right place in the sorted list"""
        await asyncio.sleep(delay)
        for i, d in enumerate(delays):
            if delay < d:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)

    tasks = [helper(wait_random(max_delay)) for _ in range(n)]
    await asyncio.gather(*tasks)

    return delays

if __name__ == "__main__":
    asyncio.run(main())
