#Anagram Checking

def check_anagram(s1, s2):
    if len(s1) != len(s2):
        state = False
    alist = list(s2)
    for letter in s1:
        if letter in alist:
            alist.remove(letter)
        else:
            return False
    if alist:
        return False
    return True

# Solution without any procedural abstraction

def check_anagram2(s1, s2):
    state = True
    if len(s1) != len(s2):
        state = False

    slist = list(s2)
    pos1 = 0
    while pos1 < len(s1) and state:
        pos2 = 0
        found = False
        while pos2<len(s2) and not found:
            if s1[pos1] == slist[pos2]:
                found = True
            else:
                pos2 += 1
        if found == True:
            slist[pos2] = None
        else:
            state  =False
        pos1 += 1
    return state
print(check_anagram2('abcde', 'dcabe'))
