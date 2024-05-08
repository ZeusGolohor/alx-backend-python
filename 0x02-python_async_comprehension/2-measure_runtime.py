#!/usr/bin/env python3
"""
A script to measure async comprehenssion run time.
"""
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A function to measure async comprehenssion runtime.
    """
    start_time = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = perf_counter()
    return (end_time - start_time)
