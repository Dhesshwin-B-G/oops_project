class CircuitBreaker:

    def __init__(self):
        self.is_open = False
        self.reason = None

    def open(self, reason):
        self.is_open = True
        self.reason = reason

    def get_status(self):
        if self.is_open:
            return "OPEN"
        else:
            return "CLOSED"

    def get_reason(self):
        return self.reason