#!/usr/bin/env python3
'''
    Function named index_range that takes two integer
    arguments page and page_size.
'''
from typing import Tuple


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
