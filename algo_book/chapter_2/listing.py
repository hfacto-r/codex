import timeit
def test1():
    l = []
    for i in range(1000):
        l = l+ [i]
    return l

def test2():
    l = []
    for i in range(1000):
        l.append(i)
    return l

def test3():
    l = [x for x in range(1000)]
    return l

def test4():
    l = list(range(1000))
    return l

def test0():
    pass

t0 = timeit.timeit(stmt = 'test0()', setup = 'from __main__ import test0', number = 1000)
t1 = timeit.timeit(stmt = 'test1()', setup = 'from __main__ import test1', number = 1000)
t2 = timeit.timeit(stmt = 'test2()', setup = 'from __main__ import test2', number = 1000)
t3 = timeit.timeit(stmt = 'test3()', setup = 'from __main__ import test3', number = 1000)
t4 = timeit.timeit(stmt = 'test4()', setup = 'from __main__ import test4', number = 1000)

print(f'Execution time without the function calling overhead are')
print(f'Function test_1 : {t1-t0} millisecond')
print(f'Execution time with the function calling overhead are')
print(f'Function test_1 : {t1} millisecond')

