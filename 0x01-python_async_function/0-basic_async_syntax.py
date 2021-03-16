#!/usr/bin/env python3
""" return random number """

import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """ Return random number """
    await asyncio.sleep(max_delay)
    return random() * max_delay
