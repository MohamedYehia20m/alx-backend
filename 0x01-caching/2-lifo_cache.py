#!/usr/bin/env python3
"""
This module implements a LIFO cache system using inheritance.
The LIFOCache class inherits from BaseCaching and manages the cache
using a Last-In-First-Out (LIFO) strategy for item eviction.
"""

from base_caching import BaseCaching
from typing import Any, Optional


class LIFOCache(BaseCaching):
    """
    LIFOCache class that implements a LIFO caching mechanism.
    Inherits from BaseCaching.
    """

    def __init__(self) -> None:
        """Initialize the LIFO cache with an empty cache dictionary."""
        super().__init__()

    def print_cache(self) -> None:
        """Print the current contents of the cache."""
        super().print_cache()

    def put(self, key: Optional[str], item: Optional[Any]) -> None:
        """
        Add an item to the cache.
        If the cache exceeds the maximum size, the last inserted item
        is discarded. If the key already exists, update its value.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Removae and Create the value if the key already exists
                del self.cache_data[key]
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Remove the last inserted key-value pair
                    last_key, last_value = self.cache_data.popitem()
                    print(f"DISCARD: {last_key}")  # item is discarded

                self.cache_data[key] = item
        else:
            return None

    def get(self, key: Optional[str]) -> Optional[Any]:
        """
        Retrieve an item by key from the cache.
        If the key is None or does not exist, return None.

        Args:
            key: The key to retrieve from the cache.

        Returns:
            The item stored in the cache, or None if not found.
        """
        return self.cache_data.get(key) if key is not None else None
