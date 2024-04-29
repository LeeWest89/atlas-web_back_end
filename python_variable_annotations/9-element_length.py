#!/usr/bin/env python3
"""Annotate Version: gets length
"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Figures the length of the elements
    """
    return [(i, len(i)) for i in lst]
