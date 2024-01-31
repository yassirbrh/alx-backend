#!/usr/bin/env python3
'''
    Class LFUCache that inherits from BaseCaching and is a caching system
'''

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''
        Class LFUCache.
    '''
    def __init__(self):
        '''
            LFUCache Constructor.
        '''
        super().__init__()
        self.cache_arr = []
        self.cache_data_freq = {}

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
                self.cache_data_freq[key] += 1
            else:
                self.cache_data_freq[key] = 1
            self.cache_arr.append(key)
        if len(self.cache_data) > LFUCache.MAX_ITEMS:
            data_freq = {}
            for k, v in self.cache_data_freq.items():
                if k != key:
                    data_freq[k] = v
            min_v = min(data_freq.values())
            min_ks = [k for k, v in self.cache_data_freq.items() if v == min_v]
            if len(min_ks) == 1:
                key_to_delete = min_ks[0]
            else:
                min_index = min(self.cache_arr.index(k) for k in min_ks)
                key_to_delete = self.cache_arr[min_index]
            self.cache_data.pop(key_to_delete)
            self.cache_data_freq.pop(key_to_delete)
            print('DISCARD: {}'.format(key_to_delete))
            self.cache_arr.remove(key_to_delete)

    def get(self, key):
        '''
            get: instance method
            @self: Class instance
            @key: The key to look for the item corresponding to it.
            return: The item corresponding to the key.
        '''
        if key is not None and key in self.cache_data:
            self.cache_arr.remove(key)
            self.cache_data_freq[key] += 1
            self.cache_arr.append(key)
            return self.cache_data[key]
        return None
