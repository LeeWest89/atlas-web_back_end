#!/usr/bin/env python3
"""Making function that creates multiple delays using wait_random
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ calling wait-random n number of times then sort the return
    """
    delays = [wait_random(max_delay) for i in range(n)]
    delay_list = await asyncio.gather(*delays)

    return (sorted(delay_list))
