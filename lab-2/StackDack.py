class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def show(self):
        print(self.items)


class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]

    def pop_front(self):
        if not self.is_empty():
            return self.items.pop(0)

    def pop_rear(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)
