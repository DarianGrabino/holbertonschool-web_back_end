#!/usr/bin/env python3
"""String and int/float to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string and an int or float, returns a tuple,
    int on the first element and square on the second"""
    return (k, (v * v))
