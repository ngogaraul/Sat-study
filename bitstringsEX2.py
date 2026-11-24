import bitstring
from bitstring import BitArray ,pack


#data = BitArray('0b11010110')  # Example bitstring representing some data
'''
satellite_ID=12
Temperature=25.5
Voltage=3.7 
status=1


#rint(data.bin)  # Display the bitstring in binary format
print(data.uint)  # Display the unsigned integer representation of the bitstring
print(len(data))  # Display the length of the bitstring in bits
print(data.hex)  # Display the bitstring in hexadecimal format


##data= BitArray(uint=100,length=11)  # Create a bitstring representing the unsigned integer 5 with a length of 3 bits
#print(data.bin)  # Display the bitstring in binary format
#print(len(data))  # Display the length of the bitstring in bits
print((2**10)-1)# find the maximum value that can be represented with 10 bits (unsigned integer) general formula for unsigned integer is 2^n-1 where n is the number of bits
print(2**(12-1)-1)# find the maximum value that can be represented with 12 bits (signed integer) general formula for signed integer is 2^(n-1)-1 where n is the number of bits

#-------extracting fields from packet (slicing)----------------
data=BitArray('0b10110110')

print(data[0:3].bin)
print(data[3:6].bin)


#-----extracting APID from satellite header packet----------------
header = BitArray('0b0100110000010101')
version = header[0:3]
packet_type = header[3:4]
secondary_header=header[4:5]
apid = header[5:16]

print("Version",version.uint)
print("Packet Type",packet_type.uint)
print("Secondary Header",secondary_header.uint)
print("APID",apid.uint)
'''
#----------------contructing apacket header----------------
''' we have already extracted info from header now let's reverse by contructing header from individual values'''

'''
header=pack('uint:3,uint:1,uint:1,uint:11',2,1,1,500)
print(header.bin)
print(len(header))
print(header.bytes)

data=BitArray('0b1010101010101010')
print(len(data))
print(len(data.bytes) )
print(data.hex)
print(data.bytes)
'''
#--------------usigned and signed integers----------------
''' both represnt the same bitstring but the interpretation is different for signed and unsigned integers
unsigned integers are always positive and the range is from 0 to 2^n-1 where n is the number of bits
signed integers can be positive or negative and the range is from -2^(n-1)

for same bit to represent signed and unsigned integers we can use the same number of bits but the interpretation is different for signed and unsigned integers for signed to recognize negative number we use technique called two's complement representation where the most significant bit is used as a sign bit 0 for positive and 1 for negative numbers
for example if we have 8 bits and the bitstring is 11111111 for unsigned integer it represents 255 but for signed integer it represents -1 because the most significant bit is 1 which indicates negative number and the remaining bits represent the magnitude of the number in two's complement representation
for example if we have 8 bits and the bitstring is 10000000 for unsigned integer it represents 128 but for signed integer it represents -128 because the most significant bit is 1 which indicates negative number and the remaining bits represent the magnitude of the number in two's complement representation
'''
#example decoding a complete satellite packet
header=pack('uint:3,uint:1,uint:1,uint:11,int:8',0,0,1,100,-7)
print("Binary:",header.bin)
print("Hex: ",header.hex)
print("Bytes: ",header.bytes)
print("Total bits: ",len(header))

recieved_packet = BitArray(header.bytes)
version = recieved_packet[0:3]
packet_type = recieved_packet[3:4].uint
secondary_header = recieved_packet[4:5].uint
apid = recieved_packet[5:16].uint
temperature = recieved_packet[16:28].int

print("---------after decoding the packet-----------")
print("Version:", version)
print("Packet Type:", packet_type)
print("Secondary Header:", secondary_header)
print("APID:", apid)
print("Temperature:", temperature)