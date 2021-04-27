#!/usr/bin/env python3
""" basic class redis """

import uuid
import redis
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        """ return the the value """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, data: str) -> str:
        """
        Convert data to string
        """
        return self._redis.get(data).decode('utf-8')

    def get_int(self, data: str) -> int:
        """
        Convert data to int
        """
        return int(self._redis.get(data))
