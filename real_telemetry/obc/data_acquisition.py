def read_unsigned(data):
    return int.from_bytes(
        data, byteorder="big", signed=False
    )


def read_signed(data):
    return int.from_bytes(
        data, byteorder="big", signed=True
    )


def acquire_sample(sample):

    registers = sample["REGISTERS"]

    raw_counts = {

        "MET_SECONDS": sample["MET_SECONDS"],

        # EPS
        "BATTERY_VOLTAGE": read_unsigned(
            registers["BATTERY_VOLTAGE"]
        ),

        "BATTERY_CURRENT": read_unsigned(
            registers["BATTERY_CURRENT"]
        ),

        "SOLAR_CURRENT": read_unsigned(
            registers["SOLAR_CURRENT"]
        ),

        # ADCS
        "ADCS_MODE": read_unsigned(
            registers["ADCS_MODE"]
        ),

        "GYRO_X": read_signed(registers["GYRO_X"]),
        "GYRO_Y": read_signed(registers["GYRO_Y"]),
        "GYRO_Z": read_signed(registers["GYRO_Z"]),

        # Payload
        "DETECTOR_TEMP": read_unsigned(
            registers["DETECTOR_TEMP"]
        ),

        "IMAGE_FRAME_COUNT": read_unsigned(
            registers["IMAGE_FRAME_COUNT"]
        ),

        # Thermal
        "OBC_TEMP": read_signed(
            registers["OBC_TEMP"]
        ),

        "THERMAL_SENSORS": [
            read_signed(value)
            for value in registers["THERMAL_SENSORS"]
        ],

        # Propulsion
        "TANK_PRESSURE": read_unsigned(
            registers["TANK_PRESSURE"]
        ),

        "VALVE_STATE": read_unsigned(
            registers["VALVE_STATE"]
        ),

        # Memory
        "MEMORY_UTILIZATION": read_unsigned(
            registers["MEMORY_UTILIZATION"]
        ),

        "MEMORY_ERRORS": read_unsigned(
            registers["MEMORY_ERRORS"]
        )
    }

    return raw_counts