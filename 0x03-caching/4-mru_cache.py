#!/usr/bin/env python3
"""  Basic dictionary """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system
        This is a MRU caching system with item limit """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data.pop(key)

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print('DISCARD: {}'.format(self.cache_data.popitem()[0]))

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        value = self.cache_data.get(key)

        if value:
            self.cache_data.pop(key)
            self.cache_data[key] = value

        return value
