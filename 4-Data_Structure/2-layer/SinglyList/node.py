class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def __str__(self):
        return '{}'.format(self.value)

    def __eq__(self, other):
        return self.value == other.value
