#!/usr/bin/env python3
"""
Main file
"""
from exercise import Cache

cache = Cache()

# Store some data
cache.store("foo")
cache.store("bar")
cache.store(42)

# Replay the history of calls for the store method
Cache.replay(cache.store)
