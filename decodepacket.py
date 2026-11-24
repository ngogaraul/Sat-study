from bitstring import BitArray

recieved_packet = BitArray('0b000010000011001001111001')
#extract individual fields from the recieved packet
version = recieved_packet[0:3]
packet_type = recieved_packet[3:4].uint
secondary_header = recieved_packet[4:5].uint
apid = recieved_packet[5:16].uint
temperature = recieved_packet[16:24].int

print("Version:", version)
print("Packet Type:", packet_type)
print("Secondary Header:", secondary_header)
print("APID:", apid)
print("Temperature:", temperature)
print("Length:", len(recieved_packet))