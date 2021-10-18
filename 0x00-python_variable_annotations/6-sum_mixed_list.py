#!/usr/bin/env python3
"""
    Using type annotations in Python 3 to specify
    function signatures and variable types
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Args:
            mxd_lst: int and float numbers
        Return:
            Sum of the mixed list numbers
    """

    result: float = 0

    for x in mxd_lst:
        result += x

    return result
