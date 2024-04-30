#!/usr/bin/env python3
"""
Making a function that returns asyncio.Task
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes in max+delay and pass it to task function
    """
    async def task():
        """
        runs wait_randon function
        """
        return (await wait_random(max_delay))

    return (asyncio.create_task(task()))
