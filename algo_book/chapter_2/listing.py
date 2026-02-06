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


t1 = timeit.Timer('test1()', 'from __main__ import test1')
print('concat', t1.timeit(number = 1000))
t2 = timeit.Timer('test2()', 'from __main__ import test2')
print('concat', t2.timeit(number = 1000))
t3  =timeit.Timer('test3()', 'from __main__ import test3')
print('comphrension', t3.timeit(number =1000))
t4 = timeit.Timer('test4()', 'from __main__ import test4')
print('convert', t4.timeit(number =1000))

