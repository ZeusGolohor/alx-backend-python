#!/usr/bin/env python3
"""
A script to use async compression.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A function to return a comprehension list.
    """
    return [i async for i in async_generator()]
