from pathlib import Path

from packets.packet_definition import packet

from config.telemetry_config import (
    APID,
    PACKET_TYPE,
    SECONDARY_HEADER_FLAG,
    SEQUENCE_FLAG,
    PACKET_SEQUENCE_START
)


def encode_packets(packet_data, output_file):

    output_path = Path(output_file)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    packet.to_file(
        file=str(output_path),
        pkt_type=PACKET_TYPE,
        apid=APID,
        sec_header_flag=SECONDARY_HEADER_FLAG,
        seq_flag=SEQUENCE_FLAG,
        data=packet_data,
        seq_count=PACKET_SEQUENCE_START
    )

    number_of_packets = len(packet_data["MET_SECONDS"])

    expected_packet_size = 45

    expected_file_size = (
        number_of_packets * expected_packet_size
    )

    actual_file_size = output_path.stat().st_size

    if actual_file_size != expected_file_size:
        raise ValueError(
            f"Unexpected binary size: {actual_file_size} bytes. "
            f"Expected {expected_file_size} bytes."
        )

    return actual_file_size