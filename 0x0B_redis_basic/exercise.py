#!/usr/bin/env python3
""" basic class redis """

import uuid
import redis
from typing import Any


class Cache:
    """ cache class """
    def __init__(self):
        """ Constructor initialized """
        self._redis = redis.Redis()
        self._redis.flushdb(asynchronous=True)

    def store(self, data: Any) -> str:
        """ methdod that store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
