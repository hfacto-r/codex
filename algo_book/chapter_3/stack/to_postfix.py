"""Convert fully parenthesised infix expressions into postfix
Assumes that the operands are limited to ABCDEFGHIJKLMNOPQRSTUVWXYZ
Assumes the operators are limited to +,-,*,/
"""
from stack import Stack

def par_checker(expr):
    s = Stack()
    for char in expr:
        if char == '(':
            s.push(char)
        elif char == ')':
            if s.is_empty():
                return False
            else:
                s.pop()
    return (s.is_empty())

def to_postfix(expr):
    s = Stack()
    operands = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    operators = '+-*/'
    result = ''
    for char in expr:
        if char in operands:
            result += char
        elif char in operators:
            s.push(char)
        elif char == ')':
            result += s.pop()
    return result

def main():
    expr_b = '((A+(B*C))+D)'
    print(par_checker(expr_b))
    print(to_postfix(expr_b))

if __name__ == '__main__':
    main()
