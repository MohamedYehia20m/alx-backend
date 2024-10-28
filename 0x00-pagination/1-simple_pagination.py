#!/usr/bin/env python3
"""Server module for paginating a database of popular baby names."""

import csv
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The file path to the dataset.
        __dataset (List[List]): The cached dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server instance and dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Returns:
            List[List]: The dataset as a list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a specific page of the dataset.

        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows for the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        res = index_range(page, page_size)
        dataset = self.dataset()

        if 0 <= int(res[0]) < len(dataset):
            return dataset[res[0]:res[1]]
        else:
            return []
