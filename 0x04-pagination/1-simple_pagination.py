#!/usr/bin/env python3
""" Python file that contain code about simple pagination """
import csv
import math
from typing import Tuple, List
index_range = __import__('0-simple_helper_function').index_range


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
        """
        => Verify that both arguments are integers great than 0
        => Find the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset.
        """
        assert(type(page_size) == int and type(page) == int)
        assert(page > 0 and page_size > 0)
        beginning, end = index_range(page, page_size)
        return self.dataset()[beginning:end]
