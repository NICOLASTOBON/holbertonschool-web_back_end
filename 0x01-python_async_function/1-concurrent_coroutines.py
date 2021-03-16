#!/usr/bin/env python3
""" return list """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ Return list """
    list_random_numbers = []
    for _ in range(n):
        number = await wait_random(max_delay)
        list_random_numbers.append(number)

    return sorted(list_random_numbers)
