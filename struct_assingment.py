import struct

#let's create data to be packed into a binary format
company = 'Google'
day,month,year = 1,1,2024
awesome = True
data= struct.pack('10s 3i ?', company.encode('utf-8'), day, month, year, awesome)

print(f"Packed Data: {data}")
print(struct.unpack('10s 3i ?', data))  # Unpacking the data to verify