class Sensor:

    def __init__(self, name):
        self.name = name


class VoltageSensor(Sensor):

    def __init__(self, electrical_sys):
        super().__init__("Voltage Sensor")
        self.electrical_sys = electrical_sys

    def read(self):
        return self.electrical_sys.voltage


class CurrentSensor(Sensor):

    def __init__(self, electrical_sys):
        super().__init__("Current Sensor")
        self.electrical_sys = electrical_sys

    def read(self):
        return self.electrical_sys.current

class TemperatureSensor(Sensor):

    def __init__(self, electrical_sys):
        super().__init__("Temperature Sensor")
        self.electrical_sys = electrical_sys

    def read(self):
        return self.electrical_sys.temperature