from app.core.fault import (
    OverVoltageFault,
    OverCurrentFault,
    OverTemperatureFault
)


voltage_fault = OverVoltageFault(280)
current_fault = OverCurrentFault(15)
temperature_fault = OverTemperatureFault(90)


print(voltage_fault.get_details())
print(current_fault.get_details())
print(temperature_fault.get_details())