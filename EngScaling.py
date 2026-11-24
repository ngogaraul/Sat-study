from bitstring import BitArray

import decoderReuse
'''
raw_data = BitArray(int=-30, length=8) # Create a bit array with an 8-bit signed integer value of -30

raw_temperature = raw_data.int

temperature = raw_temperature * 0.5 #0.5 is the scaling factor for temperature in this example

print(raw_data.bin) # Print the binary representation of the raw data
print(raw_temperature)# Print the raw temperature value
print(temperature) # Print the scaled temperature value
'''
'''
raw_temperature = BitArray('0b11110110').int # Extract the signed integer value from the bit array
raw_voltage=BitArray('0b000011001000').uint # Extract the unsigned integer value from the bit array
raw_current=BitArray('0b0000010100').uint # Extract the unsigned integer value from the bit array

raw_temperature = BitArray('0b11110110').int
raw_voltage = BitArray('0b000011001000').uint
raw_current = BitArray('0b0000010100').uint

temperature = raw_temperature * 0.5 # Apply scaling factor for temperature
voltage = raw_voltage * 0.01 # Apply scaling factor for voltage 
current = raw_current * 0.1 # Apply scaling factor for current
print("Temperature:", temperature, "°C")
print("Voltage:", voltage, "V")
print("Current:", current,  "A")
'''

#let's reuse decodeReuse.py to decode the scaled values from the raw data
from decoderReuse import decode_scaled
temperature_field=BitArray('0b000011001000')
temperature=decoderReuse.decode_scaled(temperature_field,signed=False,scale=0.01)

print("Temperature:", temperature, "°C")