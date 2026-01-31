class LogicGate:
    def __init__(self, label):
        self.label = label

class BinaryGate(LogicGate):
    self.pin_a = None
    self.pin_b = None

class Connector:
    def __init__(self, fromgate, togate):
        pass

