#!/usr/bin/python3
"""
Contains the "from_json_string" function
"""

import json


def from_json_string(my_str):
    """returns an object representation of a JSON string"""
    return json.loads(my_str)
