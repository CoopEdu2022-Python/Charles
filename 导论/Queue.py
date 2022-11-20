class Queue:
    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = 0
        self.queue = []

    def push(self, item):
        self.queue.appened(item)
        self.size += 1
        self.rear += 1

    def pop(self):
        pop = self.queue[self.front]
        self.size -= 1
        self.front += 1
        self.queue = self.queue[self.front:]

    def len(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def get_first(self):
        return self.queue[self.front:]

    def max(self):
        max = self.queue[0]
        for i in self.queue:
            if i > max:
                max = i
        return max

    def min(self):
        min = self.queue[0]
        for i in self.queue:
            if i > min:
                min = i
        return min


