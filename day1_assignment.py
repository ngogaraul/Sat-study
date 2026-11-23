class SatellitePacket:
    """Represents a basic satellite telemetry packet."""

    def __init__(self, satellite_id: int, temperature: float, voltage: float, current: float):
        self.satellite_id = satellite_id
        self.temperature = temperature
        self.voltage = voltage
        self.current = current

    def display_info(self) -> None:
        """Displays all telemetry fields in the packet."""
        print(f"--- Telemetry Packet [SAT-{self.satellite_id}] ---")
        print(f"Temperature : {self.temperature:.1f}°C")
        print(f"Voltage     : {self.voltage:.2f} V")
        print(f"Current     : {self.current:.2f} A")
        print(f"Temp Status : {'NOMINAL' if self.is_temperature_nominal() else 'WARNING (Out of Range)'}")
        print("-" * 35)

    def is_temperature_nominal(self) -> bool:
        """Checks if the temperature is within the acceptable range (-40°C to 85°C)."""
        return -40.0 <= self.temperature <= 85.0

    def update_temperature(self, new_temperature: float) -> None:
        """Updates the packet's temperature measurement."""
        if not isinstance(new_temperature, (int, float)):
            raise TypeError("Temperature must be a numeric value.")
        self.temperature = float(new_temperature)


if __name__ == "__main__":
    # Task 3: Create two satellite packet objects with different measurements
    packet_1 = SatellitePacket(satellite_id=101, temperature=35.7, voltage=5.2, current=1.4)
    packet_2 = SatellitePacket(satellite_id=102, temperature=92.4, voltage=4.9, current=2.1)

    # Display initial states
    packet_1.display_info()
    packet_2.display_info()

    # Demonstrate updating temperature and re-checking range
    print("\nUpdating SAT-102 temperature after thermal radiator activation...")
    packet_2.update_temperature(68.0)
    packet_2.display_info()