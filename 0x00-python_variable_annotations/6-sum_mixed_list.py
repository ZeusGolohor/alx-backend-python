#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list which takes a list mxd_lst
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Type-annotated function sum_mixed_list which takes a list mxd_lst.
    """
    return sum(mxd_lst)
