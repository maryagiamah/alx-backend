#!/usr/bin/python3
"""Create a class FIFOCache that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.values()) > BaseCaching.MAX_ITEMS:
                key = next(iter(self.cache_data))
                self.cache_data.pop(key)
                print(f"DISCARD: {key}")

    def get(self, key):
        """Return the value in self.cache_data"""
        return self.cache_data.get(key, None)
