#!/usr/bin/env python3
""" Python file about 0x05. Personal data project """
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Arguments:
    => fields: A list of strings representing all fields to abfuscate
    => redaction: A string representing by what the field will be obfuscated
    => message: A string representing the log line
    => separator: A string representing by which character is separating all fields in the log line (message)
    """
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message
