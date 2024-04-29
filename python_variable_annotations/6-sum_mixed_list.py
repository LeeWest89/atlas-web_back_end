#!/usr/bin/env python3
"""takes a list of floats as argument and returns their sum as a float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """iterating through list and adding as I go
    """
    return (sum(mxd_lst))
