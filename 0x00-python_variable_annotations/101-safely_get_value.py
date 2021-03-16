#!/usr/bin/env python3
""" return dict """

from typing import Mapping, Any, Union, T


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None,
        ) -> Union[Any, T]:
    """ return value of dict """
    if key in dct:
        return dct[key]
    else:
        return default
