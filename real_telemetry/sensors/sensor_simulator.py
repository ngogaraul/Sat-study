import numpy as np


def encode_unsigned(value, byte_length):
    return int(value).to_bytes(
        byte_length,
        byteorder="big",
        signed=False
    )


def encode_signed(value, byte_length):
    return int(value).to_bytes(
        byte_length,
        byteorder="big",
        signed=True
    )


def generate_sensor_samples(number_of_samples=10):

    rng = np.random.default_rng(seed=42)

    samples = []

    for i in range(number_of_samples):

        # -------------------------
        # EPS measurements
        # -------------------------

        battery_voltage = 28.1 + rng.normal(0, 0.05)
        battery_current = 2.35 + rng.normal(0, 0.03)
        solar_current = 1.82 + rng.normal(0, 0.04)

        # -------------------------
        # ADCS measurements
        # -------------------------

        adcs_mode = 2

        gyro_x = 0.120 + rng.normal(0, 0.005)
        gyro_y = -0.040 + rng.normal(0, 0.005)
        gyro_z = 0.080 + rng.normal(0, 0.005)

        # -------------------------
        # Payload measurements
        # -------------------------

        detector_temp = 72.5 + rng.normal(0, 0.1)

        image_frame_count = 1284 + (i * 4)

        # -------------------------
        # Thermal measurements
        # -------------------------

        obc_temp = 42.6 + (i * 0.1)

        thermal_sensors = [
            25.6 + (i * 0.1),
            31.4 + (i * 0.1),
            28.1 + (i * 0.1),
            34.0 + (i * 0.1)
        ]

        # -------------------------
        # Propulsion measurements
        # -------------------------

        tank_pressure = 1850 + (i * 2)

        valve_state = 1

        # -------------------------
        # Memory measurements
        # -------------------------

        memory_utilization = 67.5 + (i * 0.2)

        memory_errors = 0

        # -------------------------
        # Convert engineering
        # values into raw counts
        # -------------------------

        raw = {

            # EPS: unsigned 16-bit registers

            "BATTERY_VOLTAGE": encode_unsigned(
                round(battery_voltage * 1000), 2
            ),

            "BATTERY_CURRENT": encode_unsigned(
                round(battery_current * 1000), 2
            ),

            "SOLAR_CURRENT": encode_unsigned(
                round(solar_current * 1000), 2
            ),

            # ADCS

            "ADCS_MODE": encode_unsigned(adcs_mode, 1),

            "GYRO_X": encode_signed(round(gyro_x * 1000), 2),
            "GYRO_Y": encode_signed(round(gyro_y * 1000), 2),
            "GYRO_Z": encode_signed(round(gyro_z * 1000), 2),

            # Payload

            "DETECTOR_TEMP": encode_unsigned(
                round(detector_temp * 16), 2
            ),

            "IMAGE_FRAME_COUNT": encode_unsigned(
                image_frame_count, 2
            ),

            # Thermal

            "OBC_TEMP": encode_signed(
                round(obc_temp * 10), 2
            ),

            "THERMAL_SENSORS": [
                encode_signed(round(t * 10), 2)
                for t in thermal_sensors
            ],

            # Propulsion

            "TANK_PRESSURE": encode_unsigned(
                tank_pressure, 2
            ),

            "VALVE_STATE": encode_unsigned(
                valve_state, 1
            ),

            # Memory

            "MEMORY_UTILIZATION": encode_unsigned(
                round(memory_utilization * 10), 2
            ),

            "MEMORY_ERRORS": encode_unsigned(
                memory_errors, 2
            )
        }

        # Mission elapsed time is maintained by the OBC.
        samples.append({
            "MET_SECONDS": i,
            "REGISTERS": raw
        })

    return samples