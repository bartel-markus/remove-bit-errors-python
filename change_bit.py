import sys
from bitstring import BitArray

def invert_bit(filename_in, filename_out, offset):
    bit_array = BitArray(open(filename_in, 'rb'))
    bit_array.invert(offset)
    open(filename_out, 'wb').write(bit_array.bytes)
