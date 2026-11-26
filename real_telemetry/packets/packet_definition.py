import ccsdspy


packet = ccsdspy.FixedLength([

    # Mission elapsed time
    ccsdspy.PacketField(
        name="MET_SECONDS",
        data_type="uint",
        bit_length=32
    ),

    # Original OBC telemetry
    ccsdspy.PacketField(
        name="OBC_TEMP",
        data_type="int",
        bit_length=16
    ),

    # EPS
    ccsdspy.PacketField(
        name="BATTERY_VOLTAGE",
        data_type="uint",
        bit_length=16
    ),

    ccsdspy.PacketField(
        name="BATTERY_CURRENT",
        data_type="uint",
        bit_length=16
    ),

    ccsdspy.PacketField(
        name="SOLAR_CURRENT",
        data_type="uint",
        bit_length=16
    ),

    # ADCS
    ccsdspy.PacketField(
        name="ADCS_MODE",
        data_type="uint",
        bit_length=3
    ),

    ccsdspy.PacketField(
        name="GYRO_X",
        data_type="int",
        bit_length=16
    ),

    ccsdspy.PacketField(
        name="GYRO_Y",
        data_type="int",
        bit_length=16
    ),

    ccsdspy.PacketField(
        name="GYRO_Z",
        data_type="int",
        bit_length=16
    ),

    # Payload
    ccsdspy.PacketField(
        name="DETECTOR_TEMP",
        data_type="uint",
        bit_length=16
    ),

    ccsdspy.PacketField(
        name="IMAGE_FRAME_COUNT",
        data_type="uint",
        bit_length=16
    ),

    # Thermal array
    ccsdspy.PacketArray(
        name="THERMAL_SENSORS",
        data_type="int",
        bit_length=16,
        array_shape=(4,)
    ),

    # Propulsion
    ccsdspy.PacketField(
        name="TANK_PRESSURE",
        data_type="uint",
        bit_length=16
    ),

    ccsdspy.PacketField(
        name="VALVE_STATE",
        data_type="uint",
        bit_length=1
    ),

    # Memory
    ccsdspy.PacketField(
        name="MEMORY_UTILIZATION",
        data_type="uint",
        bit_length=16
    ),

    ccsdspy.PacketField(
        name="MEMORY_ERRORS",
        data_type="uint",
        bit_length=16
    ),

    # OBC AI/ML
    ccsdspy.PacketField(
        name="PREDICTED_TEMP",
        data_type="int",
        bit_length=16
    ),

    # Four padding bits to complete the byte
    ccsdspy.PacketField(
        name="RESERVED",
        data_type="uint",
        bit_length=4
    )
])