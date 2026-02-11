from stack import Stack
o_symbols = '[{('
c_symbols = ']})'

def par_checker(astr):
    s = Stack()
    pos = 0
    while pos < len(astr):
        char = astr[pos]
        if char in o_symbols:
            s.push(char)
        elif char in c_symbols:
            if s.is_empty():
                return False
            else:
                top = s.pop()
                if not _checker(top, char):
                    return False

        pos += 1
    return (s.is_empty())

def _checker(astr, bstr):
    return (o_symbols.index(astr) == c_symbols.index(bstr)) 




