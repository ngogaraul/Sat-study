# Satellite telemetry configuration

APID = 100

NUMBER_OF_SAMPLES = 10

SAMPLE_PERIOD_SECONDS = 1

START_MISSION_ELAPSED_TIME = 0

PACKET_SEQUENCE_START = 0

# CCSDS primary header settings
PACKET_TYPE = 0             # Telemetry
SECONDARY_HEADER_FLAG = 0   # No secondary header
SEQUENCE_FLAG = 3           # CCSDS unsegmented packet

# Sensor scaling factors
SCALES = {
    "BATTERY_VOLTAGE": 1000,
    "BATTERY_CURRENT": 1000,
    "SOLAR_CURRENT": 1000,

    "GYRO_X": 1000,
    "GYRO_Y": 1000,
    "GYRO_Z": 1000,

    "DETECTOR_TEMP": 16,

    "OBC_TEMP": 10,
    "THERMAL_SENSORS": 10,

    "TANK_PRESSURE": 1,

    "MEMORY_UTILIZATION": 10,

    "PREDICTED_TEMP": 10
}

# Demonstration operating limits.
# Replace these with approved mission requirements.
LIMITS = {
    "BATTERY_VOLTAGE": (20.0, 35.0),
    "BATTERY_CURRENT": (0.0, 10.0),
    "SOLAR_CURRENT": (0.0, 10.0),
    "DETECTOR_TEMP": (-20.0, 80.0),
    "OBC_TEMP": (-20.0, 80.0),
    "TANK_PRESSURE": (0.0, 5000.0),
    "MEMORY_UTILIZATION": (0.0, 100.0)
}