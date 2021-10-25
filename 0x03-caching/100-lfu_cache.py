#!/usr/bin/env python3
"""  Basic dictionary """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system
        This is a LFU caching system with item limit """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.freq:
                self.freq[key] = self.freq.pop(key) + 1

            elif len(self.freq) >= BaseCaching.MAX_ITEMS:
                lfu_key = min(self.freq, key=self.freq.get)
                print('DISCARD: {}'.format(lfu_key))
                self.cache_data.pop(lfu_key)
                self.freq.pop(lfu_key)
                self.freq[key] = 1

            else:
                self.freq[key] = 1

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        value = self.cache_data.get(key)

        if value:
            self.freq[key] = self.freq.pop(key) + 1

        return value
