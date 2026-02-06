import timeit
from matplotlib import pyplot as plt
pop_lst = []
pop_x = []
popi_lst = []
for i in range(10000,100000, 10000):
    x = list(range(i))
    pop_x.append(i)
    tp = timeit.timeit(stmt='x.pop()', setup='from __main__ import x', number =1000)
    pop_lst.append(tp)
    tpi = timeit.timeit(stmt='x.pop(0)', setup='from __main__ import x', number =1000)
    popi_lst.append(tpi)
fig, ax = plt.subplots()
plt.xlabel('Length of list')
plt.ylabel('Time Required')
ax.scatter(pop_x, pop_lst, marker='*', label = 'pop()')
ax.scatter(pop_x, popi_lst, label = 'pop(i)')
plt.legend()
plt.show()


