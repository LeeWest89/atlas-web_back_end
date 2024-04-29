#!/usr/bin/env python3
"""takes arguments and returns a tuple.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a Tuple of a string and an int/float
    """
    return (k, v * v)
