#!/usr/bin/env python3
"""
    Using type annotations in Python 3 to specify
    function signatures and variable types
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Return the first element of lst if there is any, otherwise None.
    """

    if lst:
        return lst[0]
    else:
        return None
