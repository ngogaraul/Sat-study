from config.telemetry_config import LIMITS


def validate_sample(telemetry):

    warnings = []

    for field, (minimum, maximum) in LIMITS.items():

        value = telemetry[field]

        if not minimum <= value <= maximum:
            warnings.append(
                f"{field} outside permitted example range: {value}"
            )

    if telemetry["ADCS_MODE"] not in [0, 1, 2, 3]:
        warnings.append("Invalid ADCS mode")

    if telemetry["VALVE_STATE"] not in [0, 1]:
        warnings.append("Invalid propulsion valve state")

    if telemetry["MEMORY_ERRORS"] > 0:
        warnings.append("Memory errors detected")

    if telemetry["IMAGE_FRAME_COUNT"] < 0:
        warnings.append("Invalid payload frame count")

    return warnings