#!/usr/bin/env python3
"""Creating a asynchronous coroutine that is a random timer
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Making random_delay to hold random sleep amount
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return (random_delay)
