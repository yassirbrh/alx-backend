#!/usr/bin/env python3
'''
    Method get_hyper that takes the same arguments (and defaults) as get_page
    and returns a dictionary containing the following key-value pairs.
'''
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
        index_range: function
        description: returns the range of indexes for a page depending
                     on its size
        @page: the starting page index.
        @page_size: the size of elements in the page.
        return: A tuple containing the starting index and the ending.
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        '''
            get_page: function
            description: returns a page content depending on the page number
                         and the page size
            @self: Object constructor.
            @page: Page number.
            @page_size: the size of page.
            return: A list containing the result of the specific page.
        '''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        number_of_lines = len(self.dataset())
        if page >= number_of_lines or page_size > number_of_lines:
            return []
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''
            get_hyper: function
            description: returns a page content depending on the page number
                         and the page size
            @self: Object constructor.
            @page: Page number.
            @page_size: the size of page.
            return: A list containing the result of the specific page.
        '''
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page + 1 > total_pages:
            next_page = None
        else:
            next_page = page + 1
        if page - 1 < 1:
            prev_page = None
        else:
            prev_page = page - 1
        if len(data) == 0:
            page_size_final = 0
        else:
            page_size_final = page_size
        return {
            'page_size': page_size_final,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
