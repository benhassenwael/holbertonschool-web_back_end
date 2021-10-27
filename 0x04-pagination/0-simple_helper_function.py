#!/usr/bin/python3
""" Simple Pagination
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Range of the page
    """
    return ((page - 1) * page_size, page * page_size)
