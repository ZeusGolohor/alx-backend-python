#!/usr/bin/env python3
"""
Type-annotated function make_multiplier that takes a float multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function make_multiplier that takes a float multiplier.
    """
    return lambda x: x * multiplier
