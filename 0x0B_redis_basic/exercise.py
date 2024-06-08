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


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs"""
    @wraps(method)
    def h_wrap(self, *args, **kwargs):
        """Create keys for inputs and outputs"""
        in_key = method.__qualname__ + ':inputs'
        out_key = method.__qualname__ + ':outputs'
        result = method(self, *args, **kwargs)

        self._redis.rpush(in_key, str(args))
        self._redis.rpush(out_key, str(result))
        return (result)

    return (h_wrap)


class Cache:
    """Cache class"""
    def __init__(self):
        """Setuo redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        
def replay(method: Callable):
    """show calls for functions"""
    in_key = method.__qualname__ + ':inputs'
    out_key = method.__qualname__ + ':outputs'
    inputs = redis.Redis().lrange(in_key, 0, -1)
    outputs = redis.Redis().lrange(out_key, 0, -1)

    print('{} was called {} times:'.format(method.__qualname__,
                                            len(inputs)))
    for input_data, output_data in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(method.__qualname__,
                                        input_data.decode('utf-8'),
                                        output_data.decode('utf-8')))
