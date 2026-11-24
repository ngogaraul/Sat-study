import bitstring
from bitstring import BitArray
import math
#--------------intro on displaying the bitstring in different formats----------------
#s=bitstring.BitArray('0x4f8e220')
# print(s.unpack('u12,hex8,bin'))

a=BitArray('0xff01')
b=BitArray('0b110')

#print(a.bin)
#print(b.oct)
#print(a.hex)
#print(b.i)
# print(a.bytes)
#--------------intro on MODIFYING BITSTRINGS---------------
"""
print(a.bin[3:9])#printing the bits from index 3 to 8 (6 bits)
print(a.bin)#printing the entire bitstring in binary format
del a[-6:]#deleting the last 6 bits from the bitstring
print(a)#printing the bitstring after deleting the last 6 bits

print (a[8]) #printing the first bit of the bitstring
print (a[-1]) #printing the last bit of the bitstring
#key take a way indexing starts from left to right and -1 is the last bit of the bitstring

a.prepend('0b01')#prepending 2 bits to the bitstring
print(a.bin)#printing the bitstring after prepending bits
a.append('0o7')#appending 3 bits to the bitstring
print(a.bin)#printing the bitstring after prepending and appending bits
a+=('0x06')  #adding 8 bits to the bitstring
print(a.bin)#printing the bitstring after prepending, appending and adding bits
"""

#---finding and replacing bits in the bitstring

#=BitArray('0xa9f')
#rint(a.find('0x4f')  )#finding the index of the first occurrence of the bitstring '0x4f' in the bitstring a

#rint(a== '0b101,0x4f,0b1')

#----------Constructing a bitstring--------------------------
'''
width, height = 352, 288
s = BitArray('0x000001b3, u12=352, u12=288')
print(s.hex)  # Display the packed bitstring in hexadecimal format
'''
data = BitArray('0b100000110010011')  # Create a bitstring representing the unsigned integer 100 with a length of 11 bits
print(data.uint)  # Display the bitstring in binary format