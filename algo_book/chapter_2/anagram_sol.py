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

def check_anagram3(s1, s2):
    state = True
    if len(s1) != len(s2):
        state = False
    alist = list(s1)
    blist = list(s2)
    alist.sort()
    blist.sort()
    pos1 = 0
    while pos1 < len(s1) and state:
        if alist[pos1] == blist[pos1]:
            pos1 += 1
        else:
            state = False
    return state

def check_anagram4(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    count_lista = [0] * 26
    count_listb = [0] * 26
    pos1 = 0
    while pos1 < len(s1):
        pos = ord(s1[pos1]) - ord('a')
        count_lista[pos] += 1
        pos1 += 1
    pos1 = 0
    while pos1 < len(s2):
        pos = ord(s2[pos1]) - ord('a')
        count_listb[pos] += 1
        pos1 += 1
    pos1 = 0
    while pos1  < len(count_lista):
        if count_lista[pos1] == count_listb[pos1]:
            pos1 += 1
        else:
            return False
    return True

print(check_anagram4('hearp','earTh'))
