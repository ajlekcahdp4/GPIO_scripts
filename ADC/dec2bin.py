def dec2bin (val):
    return [int (bit) for bit in bin(val)[2:].zfill(8)]