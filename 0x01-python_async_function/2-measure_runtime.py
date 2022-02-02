#!/usr/bin/env python3
""" Python file that contains an asynchronous coroutine """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    << measure_time >> function with integers <n> and
    <max_delay> as arguments that measures the total
    execution time for wait_n(n, max_delay), and
    returns total_time / n. Your function should
    return a float
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_process = time.perf_counter() - start_time
    return time_process / n
