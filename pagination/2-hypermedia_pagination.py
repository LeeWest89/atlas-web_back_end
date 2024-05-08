#!/usr/bin/env python3
"""Creating a function that returnes a tuple of start and end indexs"""


import csv
import math
from typing import List, Dict, Union


def index_range(page: int, page_size: int) -> tuple:
    """Math to zero the page index and to calculate start and end indexs"""
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)


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
        """Return page based pagination"""
        assert isinstance(page, int) and page > 0 and isinstance(page, int)
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        if start >= len(self.dataset()):
            return ([])

        return (self.dataset()[start:end])

    def get_hyper(self,
                  page: int = 1,
                  page_size: int = 10
                  ) -> Dict[str, Union[int, List[List], None]]:
        """Returns hypermedia pagination"""
        pages = math.ceil(len(self.dataset()) / page_size)
        n_page = page + 1 if page < pages else None
        p_page = page - 1 if page > 1 else None

        return ({
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": n_page,
            "prev_page": p_page,
            "total_pages": pages
        })
