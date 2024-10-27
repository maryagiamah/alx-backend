#!/usr/bin/env python3
"""Write a function named index_range that takes two integer arguments"""


def index_range(page: int, page_size: int) -> tuple:
    """Return Tuple of start_index and end_index"""

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)
