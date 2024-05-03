#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function’s parameters and return values with the appropriate types.
    """
    return [(i, len(i)) for i in lst]
