#!/usr/bin/env python3
""" return list """

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ Return list """
    list_random_numbers = [await wait_random(max_delay) for _ in range(n)]

    return sorted(list_random_numbers)
