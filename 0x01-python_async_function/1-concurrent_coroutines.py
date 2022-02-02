#!/usr/bin/env python3
""" Python file that contains an asynchronous coroutine """
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n:  int, max_delay: int) -> List[float]:
    """
    Async routine that takes in 2 int arguments (in this order):
    => <n>
    => << max_delay >>
    << wait_n >> should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency
    """
    delay_list = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]
    return [await delay_list
            for delay_list in asyncio.as_completed(delay_list)]