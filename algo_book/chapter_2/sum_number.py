import time
def sum_a(n):
    start = time.time()
    sum = 0
    for i in range(1, n+1):
        sum += i
    end = time.time()
    return sum, end-start

def sum_b(n):
    start = time.time()
    out = (n/2)*(n+1)
    end = time.time()
    return out, end- start

for i in range(5):
    p = 10000000
    print(f'{sum_a(p)[0]} - {sum_a(p)[1]} -  {sum_b(p)[0]} - {sum_b(p)[1]}')

