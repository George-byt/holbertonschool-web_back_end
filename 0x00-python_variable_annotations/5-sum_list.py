#!/usr/bin/env python3
""" Python file that contains a type-annotated function <sum_list> """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Type-annotated function <sum_list> that
    takes a list of floats as argument and
    returns their sum as a float
    """
    return sum(input_list)
