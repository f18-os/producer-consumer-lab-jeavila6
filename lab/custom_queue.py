from threading import Condition


# custom queue class to explicitly add synchronization (instead of using Python's Queue)
class CustomQueue:
    def __init__(self, buff_size):
        self.queue = []
        self.buff_size = buff_size
        self.condition = Condition()

    def put(self, item):
        self.condition.acquire()  # acquire lock
        # if queue is full, wait for room in queue
        if len(self.queue) == self.buff_size:
            self.condition.wait()
        # add item to queue, wake up other thread and release lock
        self.queue.append(item)
        self.condition.notify()
        self.condition.release()

    def get(self):
        self.condition.acquire()  # acquire lock
        if not self.queue:  # if queue is empty, wait for something to appear in queue
            self.condition.wait()
        # get item, wake up other thread and release lock
        item = self.queue.pop()
        self.condition.notify()
        self.condition.release()
        return item
