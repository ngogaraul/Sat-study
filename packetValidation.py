from bitstring import BitArray
'''
def validate_packet(packet):
    if len(packet) != 24:
        raise ValueError("Invalid packet length")

    return True
packet = BitArray('0b000010000011001001111001')

print(validate_packet(packet))
packet = BitArray('0b0000100000110010')

print(validate_packet(packet))

#-------------validating application identifier (APID)----------------
def validate_apid(apid,expected_apid):
    if apid != expected_apid:
        raise ValueError(f"Unexpected APID: {apid}.")
    return True
print(validate_apid(100, 100))  # True
print(validate_apid(101, 100))  # Error

''
#-------combined validation function for packet and APID----------------
def validate_temperature_packet(packet, apid, temperature):

    if len(packet) != 24:
        raise ValueError("Invalid packet length")

    if apid != 100:
        raise ValueError("Unexpected APID")

    if temperature < -40 or temperature > 85:
        raise ValueError("Temperature outside permitted range")

    return True
packet = BitArray('0b000010000011001001111001')
try:
    validate_temperature_packet(packet, 100, 25)
    print("Packet accepted")

except ValueError as error:
    print("Packet rejected:", error)
    '''
#-----------complete packet decoder-----------------
#from bitstring import BitArray

def decode_temperature_packet(packet):

    if len(packet) != 24:
        raise ValueError("Invalid packet length")

    version = packet[0:3].uint
    packet_type = packet[3:4].uint
    secondary_header = packet[4:5].uint
    apid = packet[5:16].uint
    raw_temperature = packet[16:24].int

    if apid != 50:
        raise ValueError("Unexpected APID")

    temperature = raw_temperature * 0.5

    if temperature < -40 or temperature > 85:
        raise ValueError("Invalid temperature")

    return {
        "version": version,
        "packet_type": packet_type,
        "secondary_header": secondary_header,
        "apid": apid,
        "temperature": temperature
    }

#-----------example usage-----------------
packet = BitArray('0b000010000011001001111001')

result = decode_temperature_packet(packet)

print(result)