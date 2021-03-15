#!/usr/bin/env python3
""" Return values with the appropiate types """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return list """
    return [(i, len(i)) for i in lst]
