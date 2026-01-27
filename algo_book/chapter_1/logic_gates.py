class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None
    
    def get_label(self):
        return self.label

    def get_output(self):
        #perform the operation
        if self.output == None:
            self.output = self.gate_logic()
            return self.output
        else:
            return self.output

class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return (int(input(f'Enter the pin A value for {self.get_label()}: ')))
        else:
            return self.pin_a.get_fromgate().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return (int(input(f'Enter the pin B value for {self.get_label()}: ')))
        else:
            output_gate =  self.pin_b.get_fromgate()
            if self.pin_b.get_fromgate().output == None:
                return output_gate.get_output()
            else:
                return output_gate.output

    def hook_connection(self, source):
        """This save any connection the gate is part of"""
        if self.pin_a == None:
            self.pin_a = source
        elif self.pin_b == None:
            self.pin_b = source
        else:
            raise RuntimeError('Error: Both pins are already hooked')

class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin = None

    def hook_connection(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError('Error : Available  pin is already hooked')

    def get_pin(self):
        if self.pin == None:
            return (int(input(f'Enter Value of the pin of gate {self.get_label()}: ')))
        else:
            return self.pin.get_fromgate().get_output()



class AndGate(BinaryGate):

    def gate_logic(self):
        #implement truth table
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def gate_logic(self):
        #implement truth table
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a==0 and b==0:
            return 0
        else:
            return 1
class NandGate(AndGate):
    
    def gate_logic(self):
        return int (not super().gate_logic()) # super() create a proxy object of the Parent class
    
class NorGate(OrGate):
    
    def gate_logic(self):
        return int (not super().gate_logic())

class NotGate(UnaryGate):
    def __init__(self, label):
        super().__init__(label)

    def gate_logic(self):
        a = self.get_pin()
        if a==1:
            return 0
        else:
            return 1



class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        #Connection info is saved in the togate
        tgate.hook_connection(self)

    def get_fromgate(self):
        return self.fromgate

def main():
    g1 = NandGate('G1')
    g2 = NandGate('G2')
    c1 = Connector(g1, g2)
    c2 = Connector(g1, g2)
    print(g2.get_output())
if __name__ == '__main__':
    main()


