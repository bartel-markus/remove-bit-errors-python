import sys
from bitstring import BitArray

def invert_bit(filename_in, filename_out, offset):
    with open(filename_in, 'rb') as inf:
        bit_array = BitArray(inf)
        bit_array.invert(offset)
        with open(filename_out, 'wb') as out:
            out.write(bit_array.bytes)
