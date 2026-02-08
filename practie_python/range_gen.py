class Range:
    """Implementation of Python Range function"""
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start >= self.end:
                raise StopIteration
            else:
                temp = self.start
                self.start += self.step
                return temp
        elif self.step < 0:
            if self.start<= self.end:
                raise StopIteration
            else:
                temp = self.start
                self.start += self.step
                return temp
            

