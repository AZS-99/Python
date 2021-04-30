class Node:

    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def __str__(self):
        if not self.next:
            return "{} --> |".format(self.value)
        return "{} --> {}".format(self.value, self.next)

    def __contains__(self, item):
        if not self:
            return False
        return self.value or (item in self.next)

    def append(self, value):
        if self.next is None:
            self.next = Node(value)
        else:
            self.next.append(value)

    def prepend(self, value): # why not just self = new node?
        node = Node(value, self.next)
        self.next = node
        self.value, self.next.value = self.next.value, self.value

    def remove_duplicates(self):
        if not self.next:
            return
        self.next.remove_duplicates()
        current = self
        while current.next is not None:
            if current.next.value == self.value:
                current.next = current.next.next
            else:
                current = current.next








