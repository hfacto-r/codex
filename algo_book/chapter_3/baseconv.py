#Convert Decimal number to any base
from stack import Stack

def convert_base(dec_number, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while dec_number != 0:
        rem = dec_number % base
        dec_number = dec_number // base
        s.push(digits[rem])
    result =''
    while not s.is_empty():
        result += str(s.pop())

    return result
print(convert_base(256,16))
