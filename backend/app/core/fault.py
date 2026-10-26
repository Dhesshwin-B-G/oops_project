class Fault:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_details(self):
        return {
            "name": self.name,
            "description": self.description
        }

class OverVoltageFault(Fault):

    def __init__(self, voltage):
        super().__init__(
            "Overvoltage",
            f"Voltage is too high: {voltage} V"
        )
        self.voltage = voltage


class OverCurrentFault(Fault):

    def __init__(self, current):
        super().__init__(
            "Overcurrent",
            f"Current is too high: {current} A"
        )
        self.current = current


class OverTemperatureFault(Fault):

    def __init__(self, temperature):
        super().__init__(
            "Overtemperature",
            f"Temperature is too high: {temperature} °C"
        )
        self.temperature = temperature