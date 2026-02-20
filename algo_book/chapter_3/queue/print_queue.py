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


