lst = [2, 5, 1, 7, 8, 9]
def minval(lst):
    min = lst[0]
    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
    return min


def minval2(lst):
    min = lst[0]
    for i in lst:
        for j in lst:
            if i<min:
                min = i
    return min

print(minval2(lst))
