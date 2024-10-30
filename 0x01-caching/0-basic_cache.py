#!/usr/bin/env python3
"""
This module provides a basic caching system using inheritance.
The BasicCache class inherits from BaseCaching and allows adding and
retrieving items from a cache dictionary.
"""

from base_caching import BaseCaching
from typing import Any, Optional


class BasicCache(BaseCaching):
    """
    BasicCache class that implements a simple caching mechanism.
    Inherits from BaseCaching.
    """

    def __init__(self) -> None:
        """Initialize the BasicCache."""
        super().__init__()

    def print_cache(self) -> None:
        """Print the current contents of the cache."""
        super().print_cache()

    def put(self, key: Optional[str], item: Optional[Any]) -> None:
        """
        Add an item to the cache.
        If key or item is None, do nothing.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
