#!/usr/bin/env python3
""" Python file that contains an asynchronous coroutine """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    <<task_wait_n>> function The code is nearly identical
    to wait_n except task_wait_random is being called.
    """
    delay_list = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay_list
            for delay_list in asyncio.as_completed(delay_list)]
