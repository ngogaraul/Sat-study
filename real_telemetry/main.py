import logging
from pathlib import Path

from config.telemetry_config import NUMBER_OF_SAMPLES

from sensors.sensor_simulator import generate_sensor_samples

from obc.telemetry_manager import process_all_samples

from packets.packet_encoder import encode_packets

from ground.packet_decoder import decode_packets


# --------------------------------
# 1. Project directories
# --------------------------------

ROOT = Path(__file__).parent

RAW_DIRECTORY = ROOT / "data" / "raw"

PROCESSED_DIRECTORY = ROOT / "data" / "processed"

LOG_DIRECTORY = ROOT / "logs"

RAW_DIRECTORY.mkdir(parents=True, exist_ok=True)
PROCESSED_DIRECTORY.mkdir(parents=True, exist_ok=True)
LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)


# --------------------------------
# 2. Logging
# --------------------------------

logging.basicConfig(
    filename=LOG_DIRECTORY / "telemetry.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    print("\nSATELLITE TELEMETRY PROJECT")
    print("===========================\n")

    # --------------------------------
    # STAGE 1: Generate sensor samples
    # --------------------------------

    print("1. Generating sensor measurements...")

    sensor_samples = generate_sensor_samples(
        NUMBER_OF_SAMPLES
    )

    print(f"Generated {len(sensor_samples)} samples.")


    # --------------------------------
    # STAGE 2: OBC acquisition,
    # conversion and validation
    # --------------------------------

    print("\n2. OBC processing telemetry...")

    packet_data, engineering_records, warnings = (
        process_all_samples(sensor_samples)
    )

    print(
        f"OBC processed {len(engineering_records)} samples."
    )


    # --------------------------------
    # STAGE 3: Save warnings
    # --------------------------------

    print("\n3. Checking telemetry warnings...")

    if warnings:

        for warning in warnings:

            print("WARNING:", warning)

            logging.warning(warning)

    else:

        print("No telemetry warnings detected.")

        logging.info("Telemetry checks passed.")


    # --------------------------------
    # STAGE 4: CCSDS encoding
    # --------------------------------

    print("\n4. Encoding CCSDS packets...")

    binary_file = RAW_DIRECTORY / "housekeeping.bin"

    binary_size = encode_packets(
        packet_data,
        binary_file
    )

    print("CCSDS packets created.")
    print("Binary file:", binary_file)
    print("Binary size:", binary_size, "bytes")


    # --------------------------------
    # STAGE 5: Ground decoding
    # --------------------------------

    print("\n5. Decoding packets on ground...")

    csv_file = (
        PROCESSED_DIRECTORY /
        "housekeeping_telemetry.csv"
    )

    decoded, ground_records = decode_packets(
        binary_file,
        csv_file
    )

    print("Ground decoding completed.")

    print("Decoded packets:", len(ground_records))


    # --------------------------------
    # STAGE 6: Verify packet header
    # --------------------------------

    print("\n6. CCSDS header inspection")

    print(
        "APID:",
        decoded["CCSDS_APID"]
    )

    print(
        "Sequence count:",
        decoded["CCSDS_SEQUENCE_COUNT"]
    )

    print(
        "Sequence flags:",
        decoded["CCSDS_SEQUENCE_FLAG"]
    )

    print(
        "Packet length field:",
        decoded["CCSDS_PACKET_LENGTH"]
    )


    # --------------------------------
    # STAGE 7: Show one decoded sample
    # --------------------------------

    print("\n7. First decoded telemetry sample")

    first = ground_records[0]

    for key, value in first.items():

        print(f"{key}: {value}")


    # --------------------------------
    # STAGE 8: Verify binary size
    # --------------------------------

    expected_size = NUMBER_OF_SAMPLES * 45

    assert binary_size == expected_size

    assert len(ground_records) == NUMBER_OF_SAMPLES

    print("\nAll project checks completed.")

    print("Expected binary size:", expected_size)
    print("Actual binary size:", binary_size)

    print("\nTelemetry project finished successfully.")


if __name__ == "__main__":
    main()