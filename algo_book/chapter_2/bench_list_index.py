# Experiment to verify that list index operator is O(1)
import random
import timeit
from matplotlib import pyplot as plt

lst_size = []
lst_time =[]
lst_rand = []
for i in range(1000, 1000000, 10000):
    lst_size.append(i)
    idx = random.randrange(i)
    lst_rand.append(idx)
    lst = list(range(i))
    tl = timeit.timeit(stmt = lambda: lst[idx], number =1000)
    lst_time.append(tl)

fig, ax =plt.subplots()
plt.xlabel('Size of List')
plt.ylabel('Time for 1000 List indexing')
ax.scatter(lst_size, lst_time, label = 'List index')
plt.legend()
plt.show()
