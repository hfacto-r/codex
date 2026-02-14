from stack import Stack
from tokenizer import tokenizer

def to_postfix(expr):
    expr = tokenizer(expr)
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    p_dict = {'*':3, '/':3, '+':2, '-':2, '(':1}
    postfixlst = []
    opstack = Stack()

    for char in expr:
        if char in alph:
            postfixlst.append(char)
        elif char==')':
            top = opstack.pop()
            while top !='(':
                postfixlst.append(top)
                top = opstack.pop()
        else:
            while (not opstack.is_empty()) and p_dict[opstack.peek()] >= p_dict[char]:
                top = opstack.pop()
                if top != '(':
                    postfixlst.append(top)
            opstack.push(char)
    while (not opstack.is_empty()):
        postfixlst.append(opstack.pop())
    return ''.join(postfixlst)
exp = ' A+ B*C'
print(to_postfix(exp))

