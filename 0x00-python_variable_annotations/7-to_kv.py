#!/usr/bin/env python3
'''Task 7.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts key and its value to tuple of key and
     square of its value.
    '''
    return (k, float(v**2))
