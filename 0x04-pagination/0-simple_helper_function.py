#!/usr/bin/env python3
""" 0 simple helper function """


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple that contains a start
    index and end index
    """
    total_page = page_size * page
    return ((total_page - page_size), total_page)
