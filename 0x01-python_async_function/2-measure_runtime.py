#!/usr/bin/env python3
""" Return measure """

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Return measure """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return time.time() - start_time
