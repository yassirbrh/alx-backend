#!/usr/bin/env python3
'''
    Method named get_page that takes two integer arguments page
    with default value 1 and page_size with default value 10.
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
