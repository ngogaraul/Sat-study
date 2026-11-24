from bitstring import BitArray
def decode_scaled(field,signed,scale):
    if signed:
        raw_value = BitArray(field).int
    else:
        raw_value = BitArray(field).uint
    scaled_value = raw_value * scale
    return scaled_value