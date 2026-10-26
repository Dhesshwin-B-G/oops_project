class ElectricalSystem:

    def __init__(self, voltage=230.0, current=0.0, temperature=25.0):
        self.voltage = voltage
        self.current = current
        self.temperature = temperature
        self.is_active = True

    def calculate_power(self):
        return self.voltage * self.current

    def turn_off(self):
        self.is_active = False

    def turn_on(self):
        self.is_active = True

    def get_status(self):
        return {
            "voltage": self.voltage,
            "current": self.current,
            "power": self.calculate_power(),
            "temperature": self.temperature,
            "active": self.is_active
        }