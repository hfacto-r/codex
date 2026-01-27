class Fraction:
    def __init__(self, num, denom):
        if denom == 0:
            raise ZeroDivisionError('Zero division not permitted')
        if type(num) == int and type(denom) ==int:
            common = gcd(num, denom)
            self.num = num//common
            self.denom = denom//common
        else:
            raise ValueError('Error : Expected integer')

        if self.denom < 0:
            self.denom = - self.denom
            self.num = -self.num

    def __str__(self):
        if self.denom == 1:
            return f'{self.num}'
        else:
            return f'{self.num}/{self.denom}'

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = (self.num * other.denom) + (self.denom * other.num)
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = (self.num * other.denom) - (self.denom * other.num)
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = (self.num * other.num) 
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.num == 0:
            raise ZeroDivisionError('division by zero fraction')
        new_num = (self.num * other.denom) 
        new_denom = (self.denom * other.num)
        return Fraction(new_num, new_denom)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.num * other.denom) ==  (self.denom * other.num):

    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.num * other.denom) <=  (self.denom * other.num):

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.num * other.denom) >=  (self.denom * other.num):

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.num * other.denom) <  (self.denom * other.num):

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.num * other.denom) >  (self.denom * other.num):



def gcd(m,n):
    m = abs(m)
    n = abs(n)
    while (m%n) != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

def main():
    f1 = Fraction(1,5
    print(f1) 
if __name__=='__main__': 
    main()
