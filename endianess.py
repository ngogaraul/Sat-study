
from bitstring import BitArray, pack
data=BitArray('0xABCD')
#print big-endian hexadecimal representation
print(data.hex)  # Output: 'abcd'
#print little-endian hexadecimal representation
print(data.bytes[::-1].hex())  # Output: 'cdab'
#how many bits are represented by those two bytes? 2 bytes = 16 bits
print("Bits represented:", len(data))
#Big-endian unsigned decimal value
print("Big-endian unsigned decimal value:", data.uint)  # Output: 43981