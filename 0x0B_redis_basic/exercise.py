#!/usr/bin/env python3
"""Redis Caching"""


import redis
import uuid
from typing import Union


class Cache:
    """Cache class"""
    def __init__(self):
        """Setuo redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)