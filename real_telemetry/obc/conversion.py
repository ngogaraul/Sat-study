from config.telemetry_config import SCALES


def convert_sample(raw):

    telemetry = {

        "MET_SECONDS": raw["MET_SECONDS"],

        # EPS
        "BATTERY_VOLTAGE":
            raw["BATTERY_VOLTAGE"] / SCALES["BATTERY_VOLTAGE"],

        "BATTERY_CURRENT":
            raw["BATTERY_CURRENT"] / SCALES["BATTERY_CURRENT"],

        "SOLAR_CURRENT":
            raw["SOLAR_CURRENT"] / SCALES["SOLAR_CURRENT"],

        # ADCS
        "ADCS_MODE": raw["ADCS_MODE"],

        "GYRO_X": raw["GYRO_X"] / SCALES["GYRO_X"],
        "GYRO_Y": raw["GYRO_Y"] / SCALES["GYRO_Y"],
        "GYRO_Z": raw["GYRO_Z"] / SCALES["GYRO_Z"],

        # Payload
        "DETECTOR_TEMP":
            raw["DETECTOR_TEMP"] / SCALES["DETECTOR_TEMP"],

        "IMAGE_FRAME_COUNT": raw["IMAGE_FRAME_COUNT"],

        # Thermal
        "OBC_TEMP": raw["OBC_TEMP"] / SCALES["OBC_TEMP"],

        "THERMAL_SENSORS": [
            value / SCALES["THERMAL_SENSORS"]
            for value in raw["THERMAL_SENSORS"]
        ],

        # Propulsion
        "TANK_PRESSURE": raw["TANK_PRESSURE"],

        "VALVE_STATE": raw["VALVE_STATE"],

        # Memory
        "MEMORY_UTILIZATION":
            raw["MEMORY_UTILIZATION"] /
            SCALES["MEMORY_UTILIZATION"],

        "MEMORY_ERRORS": raw["MEMORY_ERRORS"]
    }

    return telemetry