import struct

def float_to_bitstring(f: float) -> str:
    """
    Convert a floating-point number to its IEEE 754-1985 binary representation.

    Parameters
    ----------
    f : `float`
        The input floating-point number.

    Returns
    -------
    `str`
        The binary representation of the input number as a string of length 64.

    Example
    -------
    >>> float_to_bitstring(3.14)
    '0100000000001001001000011111101101010100000000000000000000000000'
    """    
    b = struct.pack('!d', f)  # !d represents big-endian byte order, double-precision floating point
    # Convert the byte sequence to a hexadecimal string
    h = b.hex()
    # Convert the hexadecimal string to a binary string
    return bin(int(h, 16))[2:].zfill(64)  # zfill(64) pads to 64 bits

if __name__ == '__main__':
    print(float_to_bitstring(1.0))  # 0011111111110000000000000000000000000000000000000000000000000000
    print(float_to_bitstring(0.0))  # 0000000000000000000000000000000000000000000000000000000000000000
    print(float_to_bitstring(-1.0)) # 1011111111110000000000000000000000000000000000000000000000000000
    print(float_to_bitstring(1.5))  # 0011111111111000000000000000000000000000000000000000000000000000
    print(float_to_bitstring(0.5))  # 0011111111100000000000000000000000000000000000000000000000000000
    print(float_to_bitstring(-0.5)) # 1011111111100000000000000000000000000000000000000000000000000000
    print(float_to_bitstring(3.14)) # 0100000000001001000111101011100001010001111010111000010100011111
    print(float_to_bitstring(1.414))    # 0011111111110110100111111011111001110110110010001011010000111001
    print(float_to_bitstring(2.71828))  # 0100000000000101101111110000100110010101101010101111011110010000
