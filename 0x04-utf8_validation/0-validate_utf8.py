#!/usr/bin/env python3
"""
UTF-8 Validation
"""

def validUTF8(data) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else returns False.
    :param data: List of integers representing bytes of the data.
    :return: Boolean indicating whether the data is valid UTF-8.
    """
    num_bytes = 0

    for byte in data:
        # Get the 8-bit binary representation of the byte
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Count the number of leading 1's in the first byte
            if byte & 0x80 == 0:
                continue  # 1-byte character
            elif byte & 0xE0 == 0xC0:
                num_bytes = 1  # 2-byte character
            elif byte & 0xF0 == 0xE0:
                num_bytes = 2  # 3-byte character
            elif byte & 0xF8 == 0xF0:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid first byte
        else:
            # Check that the byte starts with '10'
            if byte & 0xC0 != 0x80:
                return False
        num_bytes -= 1

    return num_bytes == 0
