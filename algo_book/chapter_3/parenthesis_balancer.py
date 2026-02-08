from stack import Stack
# Implementing balanced parenthesis checker using stack. - Solution One

def checker(astr):
    s = Stack()
    for char in astr:
        if char == '(':
            s.push(char)
        elif char == ')':
            if s.is_empty():
                return False
            else:
                s.pop()
        else:
            pass
    return (s.is_empty())

def checker_alt(astr):
    s= Stack()
    pos = 0
    while pos < len(astr): 
        symbol = astr[pos]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
        pos += 1
    return (s.is_empty())

print(checker_alt('()()())'))
            
