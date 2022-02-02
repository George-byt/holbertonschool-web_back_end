#!/usr/bin/env python3
""" Python file that contains an asynchronous coroutine """
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    <<task_wait_n>> function
    The code is nearly identicalto
    wait_n except task_wait_random is being called.
    """
    new_list: List[float] = []
    new_list2: List[float] = []

    for i in range(n):
        new_list.append(task_wait_random(max_delay))

    for i in asyncio.as_completed(new_list):
        num: float = await i
        new_list2.append(num)

    return new_list2
