#!/usr/bin/env python3
""" Python file that contains an asynchronous coroutine """
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    <<task_wait_n>> function
    The code is nearly identicalto
    wait_n except task_wait_random is being called.
    """
    i: List[float] = []
    for _ in range(n):
        i.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(i)]
