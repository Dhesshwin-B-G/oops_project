from app.core.electrical_system import ElectricalSystem

sys = ElectricalSystem(voltage=120.0, current=10.0)
print(sys.get_status())