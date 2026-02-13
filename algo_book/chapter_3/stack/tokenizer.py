#Implement a tokenizer for a infix expression
#Later implement a cleaner function. 
def tokenizer(expr):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    token_lst = []
    temp_str =''
    expr = expr.replace(' ','')
    for char in expr:
        if char.isalpha():
            temp_str += char
        else:
            if temp_str != '':
                token_lst.append(temp_str)
                temp_str =''
            token_lst.append(char)
    if temp_str != '':
        token_lst.append(temp_str)
    return token_lst

expr = "( Apqw BCD1   F + B* ) * ( C + D))D"

print(tokenizer(expr))
