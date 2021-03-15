#!/usr/bin/env python3
""" Return a funtion that multiplies a float """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return function """
    return lambda num: multiplier * num
