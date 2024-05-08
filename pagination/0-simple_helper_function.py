#!/usr/bin/env python3
"""Creating a function that returnes a tuple of start and end indexs"""


def index_range(page: int, page_size: int) -> tuple:
    """Math to zero the page index and to calculate start and end indexs"""
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)
