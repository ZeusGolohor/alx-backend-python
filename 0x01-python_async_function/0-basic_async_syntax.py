#!/usr/bin/env python3
"""
A script that uses asynchronous coroutine that takes in an integer argument.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    A function to show how async works.
    """
    ran = random.uniform(0, max_delay)
    await asyncio.sleep(ran)
    return (ran)
