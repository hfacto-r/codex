class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None
    
    def get_label(self):
        return self.label

    def ip_prompter(self, pin_label):
        while True:
            try:
                user_ip = int(input(f'Enter the pin {pin_label} value for {self.get_label()}: '))
            except ValueError:
                print('ERROR: Enter a Valid Input')
            else:
                if user_ip == 1 or user_ip == 0:
                    return user_ip
                else:
                    print('ERROR : Only Binary Values are accepted')


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
            return self.ip_prompter('A')
        else:
            return self.pin_a.get_fromgate().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return self.ip_prompter('B')
        else:
            return self.pin_b.get_fromgate().get_output()

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
            return self.ip_prompter('')
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

class XorGate(BinaryGate):

    def gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        return int(a != b)

class NotGate(UnaryGate):

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
    g2 = XorGate('G2')
    g3 = NotGate('G3')
    c1 = Connector(g1, g2)
    c2 = Connector(g2, g3)
    print(g3.get_output())
if __name__ == '__main__':
    main()


