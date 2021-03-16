#!/usr/bin/env python3
""" return random number """

import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """ Return random number """
    rand_number = random() * max_delay
    await asyncio.sleep(rand_number)
    return rand_number
