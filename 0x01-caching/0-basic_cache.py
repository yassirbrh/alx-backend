#!/usr/bin/env python3
'''
    Class BasicCache that inherits from BaseCaching and is a caching system
'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
        BasicCache Class that inherits from the BaseCaching class.
    '''
    def __init__(self):
        '''
            BasicCache constructor
        '''
        super().__init__()

    def put(self, key, item):
        '''
            put: method
            @self: Object constructor.
            @key: Key to add the item to it.
            @item: Item to add to the dictionary.
            return: No return
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
            get: method
            @self: Object constructor.
            @key: Key to search in the dictionary.
            return: The item corresponding to the key.
        '''
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
