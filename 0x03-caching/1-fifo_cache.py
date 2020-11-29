#!/usr/bin/python3
""" FIFO """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Class FIFO """
    def __init__(self):
        """ Initialization """
        super().__init__()

    def put(self, key, item):
        """ Inset a values in dictionary """

        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            dequeue = list(self.cache_data)[0]
            self.cache_data.pop(dequeue)
            print("DISCARD: {}".format(dequeue))

    def get(self, key):
        """ Return the values of dictionary """
        try:
            if key:
                return self.cache_data[key]
        except KeyError:
            return None
