#!/usr/bin/env python3
"""
    Using type annotations in Python 3 to specify
    function signatures and variable types
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Args:
            k: a string
            v: int or float
        Return:
            A tuple with k as first elem and v squared as second elem
    """

    return (k, v**2)
