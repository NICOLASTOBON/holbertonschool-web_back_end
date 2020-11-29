#!/usr/bin/python3
""" FIFO """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Class FIFO """
    def __init__(self):
        """ Initialization """
        super().__init__()

    def put(self, key, item):
        """ Setter method """
        if key is None or item is None:
            return None
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = list(self.cache_data.keys())[0]
            self.cache_data.pop(last)
            print("DISCARD: {}".format(last))

    def get(self, key):
        """ Return the values of dictionary """
        try:
            if key:
                return self.cache_data[key]
        except KeyError:
            return None
