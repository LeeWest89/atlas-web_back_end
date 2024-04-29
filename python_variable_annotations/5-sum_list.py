#!/usr/bin/env python3
"""takes a list of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: float) -> float:
    """iterating through list and adding as I go
    """
    amount = 0
    for i in input_list:
        amount += i
    return (amount)
