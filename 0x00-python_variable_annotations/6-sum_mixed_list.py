#!/usr/bin/env python3
""" Python file that contains a type-annotated function <sum_mixed_list> """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Type-annotated function <sum_mixed_list>
    which takes a list <mxd_lst> of integers and floats
    and returns their sum as a float
    """
    return sum(mxd_lst)
