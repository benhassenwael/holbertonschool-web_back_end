#!/usr/bin/env python3
"""
    Using type annotations in Python 3 to specify
    function signatures and variable types
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Args:
            multiplier: factor
        Return:
            multiplication in float
    """

    return lambda x: x * multiplier
