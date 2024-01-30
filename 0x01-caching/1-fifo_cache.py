#!/usr/bin/env python3
'''
    Class FIFOCache that inherits from BaseCaching and is a caching system
'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
        Class FIFOCache.
    '''
    def __init__(self):
        '''
            FIFOCache Constructor.
        '''
        super().__init__()

    def put(self, key, item):
        '''
            put: instance method.
            @self: Class instance.
            @key: The key to insert the item into.
            @item: The item to insert corresponding the key.
            return: No return
        '''
        if key is not None and item is not None:
            if len(self.cache_data) > FIFOCache.MAX_ITEMS:
                self.cache_data.popitem()
            self.cache_data[key] = item

    def get(self, key):
        '''
            get: instance method
            @self: Class instance
            @key: The key to look for the item corresponding to it.
            return: The item corresponding to the key.
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
