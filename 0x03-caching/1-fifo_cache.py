#!/usr/bin/env python3
"""  Basic dictionary """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system
        This is a FIFO caching system with item limit """

    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data)[0]
                print('DISCARD: {}'.format(first_key))
                self.cache_data.pop(first_key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
