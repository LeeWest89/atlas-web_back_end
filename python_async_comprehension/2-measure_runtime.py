#!/usr/bin/env python3
"""
Measuring the runtime of 4 async_comprehensions running in parallel
"""


import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Determining the measurement
    """
    start = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = asyncio.get_event_loop().time()
    measurement = end - start
    return (measurement)
