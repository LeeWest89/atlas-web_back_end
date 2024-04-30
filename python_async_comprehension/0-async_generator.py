#!/usr/bin/env python3
"""
loop that yeilds a random number between 0 and 10
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Waits 1 second between each loop
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
