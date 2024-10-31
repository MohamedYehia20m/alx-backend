#!/usr/bin/env python3
"""
This module implements an LFU cache system using inheritance.
The LFUCache class inherits from BaseCaching and manages the cache
using a Least Frequently Used (LFU) strategy for item eviction.
"""

from base_caching import BaseCaching
from collections import OrderedDict
from typing import Any, Optional, Dict


class LFUCache(BaseCaching):
    """
    LFUCache class that implements a LFU caching mechanism.
    Inherits from BaseCaching.
    """

    def __init__(self) -> None:
        """Initialize the LFU cache with an empty ordered cache dictionary
        and a frequency dictionary."""
        super().__init__()
        self.cache_data: OrderedDict[str, Any] = OrderedDict()
        self.frequency: Dict[str, int] = {}

    def print_cache(self) -> None:
        """Print the current contents of the cache."""
        super().print_cache()

    def put(self, key: Optional[str], item: Optional[Any]) -> None:
        """
        Add an item to the cache.
        If the cache exceeds the maximum size, the least frequently used
        item is discarded. If the key already exists, update its value.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove and update the item if the key already exists
                del self.cache_data[key]
                self.cache_data[key] = item  # re-Create the element
                self.frequency[key] += 1  # Update frequency count
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Remove the least frequently used key-value pair
                    min_frequency = min(self.frequency.values())
                    # Get items with the minimum frequency
                    min_items = [
                        k for k, v in self.frequency.items()
                        if v == min_frequency
                    ]

                    # If there's a tie, discard the first inserted (FIFO)
                    lfu_key = min_items[0]  # FIFO: the first inserted
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    print(f"DISCARD: {lfu_key}")  # Print discarded key

                # Insert the new item
                self.cache_data[key] = item
                self.frequency[key] = 1  # Initialize frequency count

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
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1  # Update frequency count
            return self.cache_data[key]
        return None
