#!/usr/bin/env python3
"""Createing class LIFOCache"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Using LIFO to create a cache system"""
    def __init__(self):
        """Starting Cache"""
        super().__init__()
        self.queue = []
        self.counter = 0

    def put(self, key, item):
        """Adding keys and items or overwriting items starting oldest"""
        if key is None or item is None:
            return ()

        if key in self.cache_data and self.cache_data[key] != item:
            self.cache_data[key] = item

        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.queue:
                    old_key = self.queue.pop(-1 - self.counter)
                    print("DISCARD:", old_key)
                    del self.cache_data[old_key]
                    self.counter += 1
                    if self.counter == self.MAX_ITEMS:
                        self.counter = 0

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """If key is in cache returns item else None"""
        if key:
            return (self.cache_data.get(key))

        elif key not in self.cache_data:
            return (None)

        return (None)
