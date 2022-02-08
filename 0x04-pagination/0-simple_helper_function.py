#!/usr/bin/env python3
""" Python file that contain a index_range function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function should return a tuple of size two containing
    a start index an end index conrresponding to the range of
    indexes to return in a list for those particular pagination
    parameters.
    """
    start_index = (page - 1) * page_size
    page_range = start_index + page_size
    return (start_index, page_range)
