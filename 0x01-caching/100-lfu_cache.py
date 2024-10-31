#!/usr/bin/python3
"""Create a class LFUCache that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    access_check = {}

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                k = min(self.access_check, key=self.access_check.get)
                self.cache_data.pop(k)
                self.access_check.pop(k)
                print(f"DISCARD: {k}")

            self.access_check[key] = self.access_check.get(key, 0) + 1

    def get(self, key):
        """Return the value in self.cache_data"""
        if key in self.cache_data:
            self.access_check[key] = self.access_check.get(key, 0) + 1
        return self.cache_data.get(key, None)
