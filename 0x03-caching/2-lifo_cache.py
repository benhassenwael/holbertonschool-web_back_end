#!/usr/bin/env python3
"""  Basic dictionary """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system
        This is a LIFO caching system with item limit """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        last_key = None

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:

            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in self.cache_data):
                print('DISCARD: {}'.format(self.last_key))
                self.cache_data.pop(self.last_key)

            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
