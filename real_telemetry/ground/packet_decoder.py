import csv
import json
from pathlib import Path

from packets.packet_definition import packet


def decode_packets(binary_file, csv_file):

    decoded = packet.load(
        str(binary_file),
        include_primary_header=True
    )

    number_of_packets = len(decoded["MET_SECONDS"])

    output_path = Path(csv_file)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    rows = []

    for i in range(number_of_packets):

        row = {

            "MET_SECONDS":
                int(decoded["MET_SECONDS"][i]),

            "APID":
                int(decoded["CCSDS_APID"][i]),

            "SEQUENCE_COUNT":
                int(decoded["CCSDS_SEQUENCE_COUNT"][i]),

            "BATTERY_VOLTAGE":
                int(decoded["BATTERY_VOLTAGE"][i]) / 1000,

            "BATTERY_CURRENT":
                int(decoded["BATTERY_CURRENT"][i]) / 1000,

            "SOLAR_CURRENT":
                int(decoded["SOLAR_CURRENT"][i]) / 1000,

            "ADCS_MODE":
                int(decoded["ADCS_MODE"][i]),

            "GYRO_X":
                int(decoded["GYRO_X"][i]) / 1000,

            "GYRO_Y":
                int(decoded["GYRO_Y"][i]) / 1000,

            "GYRO_Z":
                int(decoded["GYRO_Z"][i]) / 1000,

            "DETECTOR_TEMP":
                int(decoded["DETECTOR_TEMP"][i]) / 16,

            "IMAGE_FRAME_COUNT":
                int(decoded["IMAGE_FRAME_COUNT"][i]),

            "OBC_TEMP":
                int(decoded["OBC_TEMP"][i]) / 10,

            "THERMAL_SENSORS":
                json.dumps([
                    int(value) / 10
                    for value in decoded["THERMAL_SENSORS"][i]
                ]),

            "TANK_PRESSURE":
                int(decoded["TANK_PRESSURE"][i]),

            "VALVE_STATE":
                int(decoded["VALVE_STATE"][i]),

            "MEMORY_UTILIZATION":
                int(decoded["MEMORY_UTILIZATION"][i]) / 10,

            "MEMORY_ERRORS":
                int(decoded["MEMORY_ERRORS"][i]),

            "PREDICTED_TEMP":
                int(decoded["PREDICTED_TEMP"][i]) / 10
        }

        rows.append(row)

    if rows:

        with output_path.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=rows[0].keys()
            )

            writer.writeheader()
            writer.writerows(rows)

    return decoded, rows