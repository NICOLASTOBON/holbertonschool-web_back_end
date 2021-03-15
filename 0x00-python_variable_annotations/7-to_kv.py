#!/usr/bin/env python3
""" Return a tuple(str, float) """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return tuple with a string and int/float square """
    return (k, (v * v))
