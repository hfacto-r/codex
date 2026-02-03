lst = [2, 5, 1, 7, 8, 9]
#O(n) Function
def minval(lst):
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min

#O(n^2) Function.
#else can be used with for. else block runs only when loop completed without breaking.
def minval2(lst):
    min = None
    for i in lst:
        for j in lst:
            if i>j:
                break
        else:
            min = i
    return min   
            
            

print(minval2(lst))
