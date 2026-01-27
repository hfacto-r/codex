class Fraction:
    def __init__(self, num, denom):
        self.num = num//gcd(num, denom)
        self.denom = denom//gcd(num, denom)

    def __str__(self):
        if self.denom == 1:
            return f'{self.num}'
        else:
            return f'{self.num}/{self.denom}'

    def __add__(self, other):
        new_num = (self.num * other.denom) + (self.denom * other.num)
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __sub__(self, other):
        new_num = (self.num * other.denom) - (self.denom * other.num)
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __mul__(self, other):
        new_num = (self.num * other.num) 
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __truediv__(self, other):
        new_num = (self.num * other.denom) 
        new_denom = (self.denom * other.num)
        return Fraction(new_num, new_denom)


def gcd(m,n):
    while (m%n) != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

def main():
    f1 = Fraction(1,4)
    f2 = Fraction(1, 4)
    print(f1/f2)

if __name__=='__main__':
    main()
