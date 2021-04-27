#!/usr/bin/env python3
""" basic class redis """

import uuid
import redis
from typing import Union, Callable


class Cache:
    """ cache class """
    def __init__(self):
        """ Constructor initialized """
        self._redis = redis.Redis()
        self._redis.flushdb(asynchronous=True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ methdod that store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable) -> Union[
            str, bytes, int, float]:
        """ return the the value """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)
