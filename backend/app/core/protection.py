from .circuit_breaker import CircuitBreaker

class ProtectionSystem:

    def __init__(self, circuit_breaker):
        self.circuit_breaker = circuit_breaker
        self.protection_active = True

    def respond_to(self, fault):
        if fault is None:
            return "No fault detected"

        if not self.protection_active:
            return "Protection system disabled"

        self.circuit_breaker.open(reason=fault.name)

        return f"Protection triggered for: {fault.name}"