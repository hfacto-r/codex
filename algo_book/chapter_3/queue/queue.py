class Queue:
    """Implementing a Queue ADT in Python"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return (self.items == [])

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def main():
    q = Queue()
    print(q.is_empty())
    print(q.size())
    print(q.enqueue(True))
    print(q.enqueue(8.7))
    print(q.enqueue('Motion'))
    print(q.dequeue())
    print(q.size())
    print(q.items)
    print(q.is_empty())

if __name__ == '__main__':
    main()


