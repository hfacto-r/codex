class Counter:

    def __init__(self, num):
        if not isinstance(num, int) or num < 0:
            raise ValueError('Error : Expected a positive integer ')
        self.num_initial = num
        self.num = num
        self._history = []
        self._log(f'init({num})')

    def value(self):
        return self.num

    def inc(self):
        self.num += 1
        self._log('inc')

    def dec(self):
        if self.num >= 1:
            self.num -= 1
            self._log('dec')
        else:
            self._log('dec(blocked)')

    def reset(self):
        self.num = self.num_initial
        self._log('reset')

    def history(self):
        return self._history


    def _log(self, message):
        self._history.append(message)

