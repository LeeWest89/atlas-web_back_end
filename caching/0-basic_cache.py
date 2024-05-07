#!/usr/bin/env python3
"""Creating BasicCache the inherits from BaseCaching"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """No limit on cache system"""
    def put(self, key, item):
        """Adds to cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves items from key"""
        if key:
            return (self.cache_data.get(key))
        else:
            return (None)
