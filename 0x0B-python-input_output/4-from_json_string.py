#!/usr/bin/python3
"""
A function that returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Returns a Python data structure (object) represented by the JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
