class Node:
    def __init__(self, value, nxt=None, prev=None):
        self.value = value
        self.next = nxt
        self.prev = prev

    def append(self, value):
        if not self.next:
            node = Node(value, None, self)
            self.next = node
        else:
            self.next.append(value)


