from app.core.electrical_system import ElectricalSystem
from app.core.sensor import VoltageSensor, CurrentSensor

system = ElectricalSystem(
    voltage=230,
    current=5
)

voltage_sensor = VoltageSensor(system)
current_sensor = CurrentSensor(system)

voltage = voltage_sensor.read()
current = current_sensor.read()

print("Voltage:", voltage, "V")
print("Current:", current, "A")

power = voltage * current

print("Power:", power, "W")