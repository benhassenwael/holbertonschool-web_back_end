#!/usr/bin/env python3
"""
    Using type annotations in Python 3 to specify
    function signatures and variable types
"""


def concat(str1: str, str2: str) -> str:
    """
        Args:
            str1: The first string parameter
            str1: The second string parameter
        Return:
            Concatenated string
    """

    return (str1 + str2)
