#!/usr/bin/env python3
""" Python file that contains an asynchronous coroutine """
from typing import List
from asyncio import gather

wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    <<task_wait_n>> function
    The code is nearly identicalto
    wait_n except task_wait_random is being called.
    """
    return sorted(await gather(*[wait_random(max_delay) for i in range(n)]))
