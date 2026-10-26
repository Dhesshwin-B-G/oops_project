from .fault import (
    OverVoltageFault,
    OverCurrentFault,
    OverTemperatureFault
)


class FaultDetector:
    def __init__(
        self,
        voltage_limit=250,
        current_limit=10,
        temperature_limit=80
    ):
        self.voltage_limit = voltage_limit
        self.current_limit = current_limit
        self.temperature_limit = temperature_limit
    
    def check_voltage(self, voltage):
        if voltage > self.voltage_limit:
            return OverVoltageFault(voltage)
        return None

    def check_current(self, current):
        if current > self.current_limit:
            return OverCurrentFault(current)
        return None

    def check_temperature(self, temperature):   
        if temperature > self.temperature_limit:
                return OverTemperatureFault(temperature)
        return None