#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''
            get_hyper_index: function
            @self: the class instance identifier
            @index: the current start of the page.
            @pge_size: the current page size.
            return: a dictionary containing some data.
        '''
        assert index >= 0 and index <= len(self.dataset())
        data = self.indexed_dataset()
        if index:
            start_index = index
        else:
            start_index = 0
        page_data = []
        page_data_len = 0
        next_index = None
        for i, item in data.items():
            if i >= start_index and page_data_len < page_size:
                page_data.append(item)
                page_data_len += 1
            elif page_data_len == page_size:
                next_index = i
                break
        return {
            'index': index,
            'data': page_data,
            'page_size': page_data_len,
            'next_index': next_index,
        }
