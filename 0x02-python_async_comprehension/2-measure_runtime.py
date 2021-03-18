#!/usr/bin/env python3
""" run time for four parallel comprehensions """

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Return the total runtime """
    start: float = time.perf_counter()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    return time.perf_counter() - start
