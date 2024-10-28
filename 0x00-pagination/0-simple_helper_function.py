#!/usr/bin/env python3
"""
Module for pagination helpers.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The page number (1-based).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes for the
        given page.
    """
    return (page - 1) * page_size, page * page_size
