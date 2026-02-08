from stack import Stack
# Implementing balanced parenthesis checker using stack. - Solution One

def checker(astr):
    s = Stack()
    for char in astr:
        if char == '(':
            s.push(char)
        elif char == ')':
            s.pop()
        else:
            pass
    return (s.is_empty())

print(checker('((())'))
