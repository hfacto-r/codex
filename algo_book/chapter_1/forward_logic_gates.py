"""Notes: A connection add an entry to the output_conn list.
When output of a gate calculated, the output value should be fed to all the
connected input values and trigger its ouput calculation. To provide
normal input establish a inputgate object paradigm"""



class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None
        self.output_conn = []

    def get_label(self):
        return self.label

class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None


    def get_freepin(self):
        if self.pin_a == None:
            return self.pin_a
        elif self.pin_b == None:
            return self.pin_b
        else:
            raise RuntimeError('No Pin Available')


    def set_connection(self,other):
        self.output_conn.append(other)

    def set_pinvalues(self):
        if self.output__conn:
            for conn in self.output_conn:
                free_pin = conn.get_togate().get_freepin()
                free_pin = self.output

class Connector:
    def __init__(self, fromgate, togate):
        self.from_gate = fromgate
        self.to_gate = togate
        self.from_gate.set_connection(self)

    def set_connection(self):
        self.from_gate.set_connection(self)

    def get_fromgate(self):
        return self.from_gate

    def get_togate(self):
        return self.to_gate


def main():
    c = BinaryGate('G1')
    d = BinaryGate('G2')
    conn = Connector(c, d)
    print(c.output_conn)

if __name__ == '__main__':
    main()
