class CircularBuffer(object):
    
    def __init__(self, size = 5):
        self.buffer = [None] * (size + 1)
        self.head = 0
        self.tail = 0
        self.size = size + 1
        
    def __str__(self):
        items = ['{!r}'.format(item) for item in self.buffer]
        return '[' + ', '.join(items) + ']'
    
    def lenght(self):
        if self.tail >= self.head:
            return self.tail - self.head
        return self.size - self.head + self.tail

    def front(self):
        return self.buffer[self.head] 
    
    def add(self, item):
        if self.lenght() == self.size - 1:
            self.head = (self.head + 1) % self.size
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        
    def pop(self):
        if self.lenght() == 0:
            self.tail = (self.tail + 1) % self.size
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.size
        return item