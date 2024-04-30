#!/usr/bin/env python3
"""
Loop that yeilds a random number between 0 and 10 and creates a list
"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    return a list of floats, iterating asynchronously
    """
    return ([delay async for delay in async_generator()])
