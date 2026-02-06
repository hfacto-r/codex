# Benchmark get and set operation of Dict and verify that it is O(1)
import random, timeit
from matplotlib import pyplot as plt

dctget_time = []
dctset_time = []
dct_size = []
for i in range(10000, 1000000, 2000):
    num = random.randrange(i)
    dct = {j:None for j in range(i)}
    td = timeit.timeit(stmt = lambda: dct.get(i), number = 1000)
    ts = timeit.timeit(stmt = f'dct[{num}] = None',setup = 'from __main__ import dct', number = 1000)
    dctget_time.append(td)
    dctset_time.append(ts)
    dct_size.append(i)
fig, ax = plt.subplots()
plt.xlabel('Size of Dictionary')
plt.ylabel('Time for 1000 get operations')
ax.scatter(dct_size, dctget_time, label = 'dict get', marker = '.')
ax.scatter(dct_size, dctset_time, label = 'dict set', marker ='*')
plt.legend()
plt.show()
