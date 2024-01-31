#!/usr/bin/env python3
'''
    Class MRUCache that inherits from BaseCaching and is a caching system
'''

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''
        Class MRUCache.
    '''
    def __init__(self):
        '''
            MRUCache Constructor.
        '''
        super().__init__()
        self.cache_arr = []

    def put(self, key, item):
        '''
            put: instance method.
            @self: Class instance.
            @key: The key to insert the item into.
            @item: The item to insert corresponding the key.
            return: No return
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.cache_arr:
                self.cache_arr.remove(key)
            self.cache_arr.append(key)
        if len(self.cache_data) > MRUCache.MAX_ITEMS:
            self.cache_data.pop(self.cache_arr[-2])
            print('DISCARD: {}'.format(self.cache_arr[-2]))
            self.cache_arr.pop(-2)

    def get(self, key):
        '''
            get: instance method
            @self: Class instance
            @key: The key to look for the item corresponding to it.
            return: The item corresponding to the key.
        '''
        if key is not None and key in self.cache_data:
            if key in self.cache_arr:
                self.cache_arr.remove(key)
            self.cache_arr.append(key)
            return self.cache_data[key]
        return None
