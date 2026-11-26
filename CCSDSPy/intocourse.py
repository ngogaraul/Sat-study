import ccsdspy
from ccsdspy import PacketField ,PacketArray
from io import BytesIO

#print(ccsdspy.__version__)

#------------start learning packetField----------------
#it defines an individual packet field, which is a part of a packet. It has the following attributes:

#packetField1 =packetField(name="TEMPERATURE", data_type="int", bit_length=12)
packet=ccsdspy.FixedLength([PacketField(name="TEMPERATURE", data_type='int', bit_length=12),
                            PacketField(name="BATTERY_VOLTAGE", data_type='uint', bit_length=12),
                            PacketField(name="OPERATING_MODE",data_type='uint',bit_length=3),
                            PacketField(name="RESERVED",data_type='fill',bit_length=5),
                            PacketArray(name='SENSOR_TEMPERATURES',data_type='int',bit_length=12,array_shape=(4,))]) #---defining packetArray




#creating sample packet
raw_packet = bytes.fromhex(
    "00 64 C0 01 00 09 "
    "01 9E 74 40 FF B0 0A 00 F0 14"
)

#decoding the packet
result = packet.load(
    BytesIO(raw_packet),
    include_primary_header=True
)

#extracting the telementry

print("Temperature: ",result['TEMPERATURE'])
print("Battery : ",result['BATTERY_VOLTAGE'])
print("Operating mode: ",result['OPERATING_MODE'])
print("Sensor temperatures: ",result['SENSOR_TEMPERATURES'])

# 5. Inspect the primary header
print("APID:", result['CCSDS_APID'])
print("Sequence count:", result['CCSDS_SEQUENCE_COUNT'])
print("Packet length:", result['CCSDS_PACKET_LENGTH'])