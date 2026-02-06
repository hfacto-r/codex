import timeit
x = list(range(100000))

time_pop = timeit.timeit(stmt = 'x.pop()', setup = 'from __main__ import x', number = 10000)
time_popi = timeit.timeit(stmt = 'x.pop(0)', setup = 'from __main__ import x', number = 10000)
print(f'Time. list.pop() {time_pop}')
print(f'Time. list.pop() {time_popi}')
