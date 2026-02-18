#Implementing a hot potato game . (Josephus Problem)
from queue import Queue

def hot_potato(namelist, num):
    gq = Queue()
    for name in namelist:
        gq.enqueue(name)
    while gq.size() > 1:
        for i in range(num):
            gq.enqueue(gq.dequeue())
        gq.dequeue()

    return gq.dequeue()

numlist = ['Josh', 'Amity', 'Prince', 'Matia']
print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))
