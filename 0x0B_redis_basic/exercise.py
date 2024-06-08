#!/usr/bin/env python3
"""Redis Caching"""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Making a decorator to count method calls"""
    @wraps(method)
    def wrap(self, *arg, **kwargs):
        """the logic"""
        self._redis.incr(method.__qualname__)
        return (method(self, *arg, **kwargs))
    return (wrap)


class Cache:
    """Cache class"""
    def __init__(self):
        """Setuo redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    bytes,
                                                                    int,
                                                                    float,
                                                                    None]:
        """gets data and can convert the data back to the desired format."""
        data = self._redis.get(key)

        if data is None:
            return (None)

        if not fn:
            return (data)
        else:
            return fn(data)

    def decode(self, data: bytes) -> str:
        """Decode UTF-8 string."""
        return (data.decode('utf-8'))

    def get_str(self, key: str) -> Optional[str]:
        """Gets str from redis"""
        return (self.get(key, self.decode))

    def get_int(self, key: str) -> Optional[int]:
        """Gets int from redis"""
        return (self.get(key, int))
