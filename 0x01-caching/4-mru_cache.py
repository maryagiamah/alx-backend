#!/usr/bin/python3
"""Create a class MRUCache that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""
    access_check = []

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_data[key] = item
            if key in self.access_check:
                self.access_check.append(
                        self.access_check.pop(
                            self.access_check.index(key)
                        )
                    )
            else:
                self.access_check.append(key)
            if len(self.access_check) > BaseCaching.MAX_ITEMS:
                k = self.access_check.pop(-2)
                self.cache_data.pop(k)
                print(f"DISCARD: {k}")

    def get(self, key):
        """Return the value in self.cache_data"""
        if key in self.cache_data:
            self.access_check.append(
                        self.access_check.pop(
                            self.access_check.index(key)
                        )
                    )
        return self.cache_data.get(key, None)
