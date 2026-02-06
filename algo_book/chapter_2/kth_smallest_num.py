def kth_number(lst):
    lst.sort()
    return lst[3]


lst =[3,5,6,1,2, 7, 8]

print(kth_number(lst))
