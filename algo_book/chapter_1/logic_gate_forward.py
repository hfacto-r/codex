class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None
        self.conns = []

    def get_label(self):
        return self.label

    def trigger(self):
        self.output = self.gate_logic()
        if not self.conns:
            print(f'Output of {self.label} is {self.output}')
        for conn in self.conns:
            gate = conn.get_togate()
            gate.set_input(self.output)
            gate.execute_gate()



class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pina(self):
        return self.pin_a

    def get_pinb(self):
        return self.pin_b

    def set_input(self, val):
        if self.pin_a == None:
            self.pin_a = val
        elif self.pin_b == None:
            self.pin_b = val
        else:
            raise RuntimeError(f'Pin A and Pin B of {self.label} is already attached')

    def execute_gate(self):
        if self.pin_a != None and self.pin_b != None:
            self.trigger()




class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin = None

    def get_pin(self):
        return self.pin

    def set_input(self, val):
        if self.pin == None:
            self.pin = val
        else:
            raise RuntimeError(f'Input Pin of {self.label} is already attached')

    def execute_gate(self):
        if self.pin != None:
            self.trigger()

class InputGate(UnaryGate):
    def __init__(self, label, ipval):
        super().__init__(label)
        self.pin = ipval

    def gate_logic(self):
        return self.pin

class NotGate(UnaryGate):

    def gate_logic(self):
         pin = self.get_pin()
         return int (not pin)

class AndGate(BinaryGate):

    def gate_logic(self):
        a = self.get_pina()
        b = self.get_pinb()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    
    def gate_logic(self):
        a = self.get_pina()
        b = self.get_pinb()
        if a == 0 and b == 0:
            return 0
        else:
            return 1

class XorGate(BinaryGate):
    
    def gate_logic(self):
        a = self.get_pina()
        b = self.get_pinb()
        return int(a != b)

class NandGate(AndGate):

    def gate_logic(self):
        a = super().gate_logic()
        return int( not a)
    
class NorGate(OrGate):

    def gate_logic(self):
        a = super().gate_logic()
        return int( not a)

class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        self.from_gate.conns.append(self)

    def get_togate(self):
        return self.to_gate

def main():
    a = InputGate('A', 1)
    b = InputGate('B', 1)
    c = InputGate('C', 1)
    g1 = XorGate('X1')
    g2 = XorGate('X2')
    g3 = AndGate('A1')
    g4 = AndGate('A2')
    g5 = OrGate('O1')
    Connector(a, g1)
    Connector(b, g1)
    Connector(a, g4)
    Connector(b, g4)
    Connector(g1, g2)
    Connector(c, g2)
    Connector(c, g3)
    Connector(g1, g3)
    Connector(g3, g5)
    Connector(g4, g5)
    a.trigger()
    b.trigger()
    c.trigger()


if __name__ == '__main__':
    main()
