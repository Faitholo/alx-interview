#!/usr/bin/python3
"""
A method that determines if a given data set represents
a valid UTF-8 encoding 
"""


def validUTF8(data):
    """
    function to validate utf-8 encoding
    Args:
        data(list): data set containing multiple characters
    Returns:
        boolean: true if the data is valid utf-8 encoded, 
        otherwise false
    """
    utf8valid = 0
    for val in data:
        byte = val & 255
        if utf8valid:
            if byte >> 6 != 2:
                return False
            utf8valid -= 1
            continue
        while (1 << abs(7 - utf8valid)) & byte:
            utf8valid += 1
        if utf8valid == 1 or utf8valid > 4:
            return False
        utf8valid = max(utf8valid - 1, 0)
    return utf8valid == 0

