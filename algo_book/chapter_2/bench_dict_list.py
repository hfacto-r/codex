from matplotlib import pyplot as plt
import random
import timeit
list_time = []
dict_time = []
length = []
for i in range(10000, 1000001, 20000):
    length.append(i)
    lst = list(range(i))
    dct = {j:None for j in range(i)}
    x = random.randrange(i)

    tp = timeit.timeit(stmt = lambda: x in lst,number = 1000)
    td = timeit.timeit(stmt = lambda: x in dct,number = 1000)

    list_time.append(tp)
    dict_time.append(td)

fig, ax = plt.subplots()
plt.xlabel('Size of list/Dict')
plt.ylabel('Timefor 1000 memebership check')
ax.scatter(length, list_time, marker ='*', label = 'list')
ax.scatter(length, dict_time, marker ='.', label = 'dict')
plt.legend()
plt.show()
