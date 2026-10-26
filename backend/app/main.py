from app.core.electrical_system import ElectricalSystem
from app.core.sensor import TemperatureSensor, VoltageSensor, CurrentSensor
from app.core.detector import FaultDetector
from app.core.circuit_breaker import CircuitBreaker
from app.core.protection import ProtectionSystem


def main():

    voltage = int(input("Enter the voltage (V): "))
    current = int(input("Enter the current (A): "))
    temperature = int(input("Enter the temperature (°C): "))

    system = ElectricalSystem(
        voltage=voltage,
        current=current,
        temperature=temperature
    )

    voltage_sensor = VoltageSensor(system)
    current_sensor = CurrentSensor(system)
    temperature_sensor = TemperatureSensor(system)

    detector = FaultDetector(
        voltage_limit=250,
        current_limit=10,
        temperature_limit=70
    )

    breaker = CircuitBreaker()

    protection = ProtectionSystem(breaker)

    voltage = voltage_sensor.read()
    current = current_sensor.read()
    temperature = temperature_sensor.read()
    print("----- ELECTRICAL SYSTEM -----\n----- FAULT DETECTION (input values) -----")
    print(f"Voltage: {voltage} V")
    print(f"Current: {current} A")
    print(f"Temperature: {temperature} °C")

    print("\n----- THRESHOLD VALUES -----")
    print(f"Voltage Limit: {detector.voltage_limit} V")
    print(f"Current Limit: {detector.current_limit} A") 
    print(f"Temperature Limit: {detector.temperature_limit} °C")

    voltage_fault = detector.check_voltage(voltage)
    current_fault = detector.check_current(current)
    temperature_fault = detector.check_temperature(temperature)

    protection.respond_to(voltage_fault)
    protection.respond_to(current_fault)
    protection.respond_to(temperature_fault)
    print("\n----- PROTECTION SYSTEM STATUS -----")
    print("Circuit Breaker:", breaker.get_status())
    print("Reason:", breaker.get_reason())


if __name__ == "__main__":
    main()