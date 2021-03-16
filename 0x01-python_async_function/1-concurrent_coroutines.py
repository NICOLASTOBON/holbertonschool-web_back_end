#!/usr/bin/env python3
""" return list """

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Return list """
    list_random_numbers = [await wait_random(max_delay) for _ in range(n)]

    return sorted(list_random_numbers)
