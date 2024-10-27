#!/usr/bin/env python3
"""Write a function named index_range that takes two integer arguments"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return Tuple of start_index and end_index"""

    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """paginate the dataset correctly and return the appropriate page"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        self.dataset()

        try:
            return self.__dataset[start_idx:end_idx]
        except Exception:
            return []
