#!/usr/bin/env python3
"""
This module implements an MRU cache system using inheritance.
The MRUCache class inherits from BaseCaching and manages the cache
using a Most Recently Used (MRU) strategy for item eviction.
"""

from base_caching import BaseCaching
from typing import Any, Optional
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache class implements a Most Recently Used (MRU) caching mechanism.
    Inherits from BaseCaching.
    """

    def __init__(self) -> None:
        """Initialize the MRU cache with an empty ordered cache dictionary."""
        super().__init__()
        self.cache_data = OrderedDict()

    def print_cache(self) -> None:
        """Print the current contents of the cache."""
        super().print_cache()

    def put(self, key: Optional[str], item: Optional[Any]) -> None:
        """
        Add an item to the cache.
        If the cache exceeds the maximum size, the most recently used
        item is discarded. If the key already exists, update its value.

        Args:
            key (Optional[str]): The key under which to store the item.
            item (Optional[Any]): The item to store in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove and update the item if the key already exists
                del self.cache_data[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the most recently used key-value pair
                mru_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {mru_key}")

            # Insert the new or updated item
            self.cache_data[key] = item
        else:
            return

    def get(self, key: Optional[str]) -> Optional[Any]:
        """
        Retrieve an item by key from the cache.
        If the key is None or does not exist, return None.

        Args:
            key (Optional[str]): The key to retrieve from the cache.

        Returns:
            Optional[Any]: The item stored in the cache, or None if not found.
        """
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end to mark it as recently used
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
