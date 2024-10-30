#!/usr/bin/env python3
"""
This module implements a FIFO cache system using inheritance.
The FIFOCache class inherits from BaseCaching and manages the cache
using a First-In-First-Out (FIFO) strategy for item eviction.
"""

from base_caching import BaseCaching
from typing import Any, Optional


class FIFOCache(BaseCaching):
    """
    FIFOCache class that implements a FIFO caching mechanism.
    Inherits from BaseCaching.
    """

    def __init__(self) -> None:
        """Initialize the FIFO cache with an empty cache dictionary."""
        super().__init__()

    def print_cache(self) -> None:
        """Print the current contents of the cache."""
        super().print_cache()

    def put(self, key: Optional[str], item: Optional[Any]) -> None:
        """
        Add an item to the cache.
        If the cache exceeds the maximum size,
        the first inserted item is discarded.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get and remove the first inserted key-value pair
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)

                print(f"DISCARD: {first_key}")  # item is discarded

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
