class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if not (self.right or self.left):
            if value < self.value:
                self.left = Node(value)
            elif value > self.value:
                self.right = Node(value)
        else:
            self.left.insert(value) if value < self.value else self.right.insert(value)