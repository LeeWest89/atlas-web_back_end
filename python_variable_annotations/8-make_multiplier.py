#!/usr/bin/env python3
"""takes a float multiplier as argument and returns a function that multiplies
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that takes the float multipler and calls multi_function
    """
    def multi_function(multi: float) -> float:
        """Get the result of float times float
        """
        return (multi * multiplier)
    return (multi_function)
