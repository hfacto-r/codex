#Decimal to Binary Conversion
from stack import Stack

def dec_bin(number):
    s = Stack()
    while number != 0:
        rem = number %2
        number = number//2
        s.push(rem)
    bin_number = ''
    while not s.is_empty():
        top = s.pop()
        bin_number += str(top)
    return bin_number

print(dec_bin(233))

