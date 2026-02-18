#Evaluate a postfix expression
from stack import Stack

def postfix_eval(expr):
    opstack = Stack()
    tokenlst = expr.split()
    for token in tokenlst:
        if token in '0123456789':
            opstack.push(int(token))
        else: 
            op_2 = opstack.pop()
            op_1 = opstack.pop()
            result = do_math(op_1, op_2, token)
            opstack.push(result)
    return opstack.pop()

def do_math(numa, numb, op):
    if op == '+':
        return numa + numb
    elif op == '-':
        return numa - numb
    elif op == '*':
        return numa * numb
    elif op == '/':
        return numa / numb 

print(postfix_eval('7 8 + 3 2 + /'))
