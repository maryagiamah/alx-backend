#!/usr/bin/python3
"""Create a class LIFOCache that inherits from"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    k = ""

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.values()) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.k)
                print(f"DISCARD: {self.k}")
            self.k = key

    def get(self, key):
        """Return the value in self.cache_data"""
        return self.cache_data.get(key, None)
