#!/usr/bin/env python3
"""Createing class LIFOCache"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Using LIFO to create a cache system"""
    def __init__(self):
        """Starting Cache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adding keys and items or overwriting items starting oldest"""
        if key is None or item is None:
            return ()

        if key in self.cache_data and self.cache_data[key] != item:
            self.cache_data[key] = item

        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                print("DISCARD:", self.queue[-1])
                del self.cache_data[self.queue[-1]]

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """If key is in cache returns item else None"""
        if key:
            return (self.cache_data.get(key))

        elif key not in self.cache_data:
            return (None)

        return (None)
