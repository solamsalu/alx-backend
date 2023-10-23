#!/usr/bin/env python3
"""Task 3: Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Tuple
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
        """Retrieves a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieves info about a page from a given index and with a
        specified size.
        """
        result_dataset = []
        index_data = self.indexed_dataset()
        keys_list = list(index_data.keys())
        assert index + page_size < len(keys_list)
        assert index < len(keys_list)

        if index not in index_data:
            start_index = keys_list[index]
        else:
            start_index = index

        for i in range(start_index, start_index + page_size):
            if i not in index_data:
                result_dataset.append(index_data[keys_list[i]])
            else:
                result_dataset.append(index_data[i])

        next_index: int = index + page_size

        if index in keys_list:
            next_index
        else:
            next_index = keys_list[next_index]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(result_dataset),
            'data': result_dataset
        }
