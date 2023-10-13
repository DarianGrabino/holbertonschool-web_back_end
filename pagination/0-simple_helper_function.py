#!/usr/bin/env python3
""" function that returns a tuple of size two containing
 a start index and an end index """


def index_range(page: int, page_size: int) -> tuple:
    """ Calculates start rate and end rate """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
