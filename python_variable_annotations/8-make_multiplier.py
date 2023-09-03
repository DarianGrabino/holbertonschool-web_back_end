#!/usr/bin/env python3
"""type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function of type that takes a float multiplier as an argument
      and returns a function that multiplies."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
