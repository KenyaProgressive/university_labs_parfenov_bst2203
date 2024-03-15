class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def cut(self):
        if self.is_empty():
            return None
        popped = self.top
        self.top = self.top.next
        return popped.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data


class Deque:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self):
        return self.head.next == self.tail

    def push_top(self, data):
        head_node = Node(data)
        head_node.prev = self.head
        head_node.next = self.head.next
        self.head.next.prev = head_node
        self.head.next = head_node

    def push_bottom(self, data):
        tail_node = Node(data)
        tail_node.prev = self.tail
        tail_node.next = self.tail.next
        self.tail.prev.next = tail_node
        self.tail.prev = tail_node

    def pop_top(self):
        if self.is_empty():
            return None
        new_node = self.head.next
        self.head.next = new_node.next
        new_node.next.prev = self.head
        self.head = new_node.next
        return new_node.data

    def pop_bottom(self):
        if self.is_empty():
            return None
        new_node = self.tail.prev
        self.tail.prev = new_node.prev
        new_node.prev.next = self.tail
        return new_node.data

    def peek_top(self):
        if self.is_empty():
            return None
        return self.head.next.data

    def peek_bottom(self):
        if self.is_empty():
            return None
        return self.tail.prev.data

    def show_deque(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next