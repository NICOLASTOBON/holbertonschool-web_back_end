#!/usr/bin/env python3
""" return random number """

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10):
    """ Return random number """
    await asyncio.sleep(max_delay)
    return uniform(0, max_delay)
