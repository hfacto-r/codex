import random
from queue import Queue

class Printer:
    def __init__(self, ppm):
        self. pagerate = ppm
        self.current_task = None
        self.time_remaining = 0
    
    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
        if self.time_remaining <= 0:
            self.current_task = None

    def busy(self):
        return (self.current_task != None)

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = self.current_task.get_pages() *60/self.pagerate

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.no_pages = random.randrange(1, 21)

    def get_timestamp(self):
        return self.timestamp

    def get_pages(self):
        return self.no_pages

    def wait_time(self, current_time):
        return current_time - self.timestamp

def simulation(num_seconds, ppm):
    labprinter = Printer(ppm)
    print_queue = Queue()
    waiting_times = []
    
    for current_second in range(num_seconds):
        if new_print_task():
            new_task = Task(current_second)
            print_queue.enqueue(new_task)

        if (not labprinter.busy()) and (not print_queue.is_empty()):
            new_task = print_queue.dequeue()
            labprinter.start_next(new_task)
            waiting_times.append(new_task.wait_time(current_second))
        labprinter.tick()

    average_wait = sum(waiting_times)/len(waiting_times)
    print(f'Average waiting time {average_wait} {print_queue.size()} tasks remaining')




def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(36000, 5)
