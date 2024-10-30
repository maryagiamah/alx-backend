#!/usr/bin/python3
"""Create a class BasicCache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Call Base Class"""
        super().__init__()

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data"""
        if item and key:
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked to key"""
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
