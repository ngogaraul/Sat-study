import numpy as np

from obc.data_acquisition import acquire_sample
from obc.conversion import convert_sample
from obc.validation import validate_sample


def process_all_samples(raw_samples):

    raw_records = []
    engineering_records = []
    all_warnings = []

    for sample in raw_samples:

        # 1. Receive sensor register data
        raw = acquire_sample(sample)

        # 2. Convert raw data to engineering units
        telemetry = convert_sample(raw)

        # 3. Simulated AI/ML prediction
        # Placeholder only; replace with trained model.
        telemetry["PREDICTED_TEMP"] = (
            telemetry["OBC_TEMP"] + 1.6
        )

        # 4. Convert prediction back to a packet integer
        raw["PREDICTED_TEMP"] = round(
            telemetry["PREDICTED_TEMP"] * 10
        )

        # 5. Validate the measurements
        warnings = validate_sample(telemetry)

        if warnings:
            for warning in warnings:
                all_warnings.append(
                    f"MET {telemetry['MET_SECONDS']}: {warning}"
                )

        raw_records.append(raw)
        engineering_records.append(telemetry)

    # 6. Build arrays for CCSDSPy
    packet_data = {

        "MET_SECONDS": np.array(
            [r["MET_SECONDS"] for r in raw_records],
            dtype=np.uint32
        ),

        "OBC_TEMP": np.array(
            [r["OBC_TEMP"] for r in raw_records],
            dtype=np.int16
        ),

        "BATTERY_VOLTAGE": np.array(
            [r["BATTERY_VOLTAGE"] for r in raw_records],
            dtype=np.uint16
        ),

        "BATTERY_CURRENT": np.array(
            [r["BATTERY_CURRENT"] for r in raw_records],
            dtype=np.uint16
        ),

        "SOLAR_CURRENT": np.array(
            [r["SOLAR_CURRENT"] for r in raw_records],
            dtype=np.uint16
        ),

        "ADCS_MODE": np.array(
            [r["ADCS_MODE"] for r in raw_records],
            dtype=np.uint8
        ),

        "GYRO_X": np.array(
            [r["GYRO_X"] for r in raw_records],
            dtype=np.int16
        ),

        "GYRO_Y": np.array(
            [r["GYRO_Y"] for r in raw_records],
            dtype=np.int16
        ),

        "GYRO_Z": np.array(
            [r["GYRO_Z"] for r in raw_records],
            dtype=np.int16
        ),

        "DETECTOR_TEMP": np.array(
            [r["DETECTOR_TEMP"] for r in raw_records],
            dtype=np.uint16
        ),

        "IMAGE_FRAME_COUNT": np.array(
            [r["IMAGE_FRAME_COUNT"] for r in raw_records],
            dtype=np.uint16
        ),

        "THERMAL_SENSORS": np.array(
            [r["THERMAL_SENSORS"] for r in raw_records],
            dtype=np.int16
        ),

        "TANK_PRESSURE": np.array(
            [r["TANK_PRESSURE"] for r in raw_records],
            dtype=np.uint16
        ),

        "VALVE_STATE": np.array(
            [r["VALVE_STATE"] for r in raw_records],
            dtype=np.uint8
        ),

        "MEMORY_UTILIZATION": np.array(
            [r["MEMORY_UTILIZATION"] for r in raw_records],
            dtype=np.uint16
        ),

        "MEMORY_ERRORS": np.array(
            [r["MEMORY_ERRORS"] for r in raw_records],
            dtype=np.uint16
        ),

        "PREDICTED_TEMP": np.array(
            [r["PREDICTED_TEMP"] for r in raw_records],
            dtype=np.int16
        ),
        "RESERVED": np.zeros(
        len(raw_records),
        dtype=np.uint8
        )
    }

    return packet_data, engineering_records, all_warnings