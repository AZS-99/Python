import copy


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def __str__(self):
        if not self.next:
            return "{} --> |".format(self.value)
        return "{} --> {}".format(self.value, self.next)

    def __eq__(self, other):
        return self.value == other.value and self.next == other.next

    def __add__(self, other):
        """
        Return a copy of this list with a copy of 'other' attached to its end.
        :param other: Node
        :return: Node
        """
        if not (self or other):
            return None
        # Uses __copy__
        node1 = copy.copy(self)
        node2 = copy.copy(other)
        node1.tail().next = node2
        return node1

    def __contains__(self, item):
        if not self:
            return False
        return (self.value == item) or (item in self.next)

    def __copy__(self):
        """
        Return a copy of this list
        :return: Node
        """
        if not self.next:
            return Node(self.value)
        node = self.next.__copy__()
        return Node(self.value, node)

    def __getitem__(self, i):
        if i == 0:
            return self
        return self.next[i - 1]

    def __len__(self):
        return 1 if not self.next else len(self.next) + 1

    def __reversed__(self):
        """
        Reverse the order of values in the list.
        :return: None
        """
        if not self.next:
            return
        penultimate = self.penultimate()
        node = penultimate.next
        penultimate.next = None
        reversed(self)
        node.next = self.next
        self.next = node
        self.value, node.value = node.value, self.value

    def __setitem__(self, index, value):
        """
        Insert a node holding the passed value at the specified index
        :param index: int
        :param value: any
        :return: None
        """
        if index == 0:
            self.prepend(value)
        elif index == 1:
            node = Node(value, self.next)
            self.next = node
        else:
            self.next[index - 1] = value

    def append(self, value):
        if self.next is None:
            self.next = Node(value)
        else:
            self.next.append(value)

    def count(self, value):
        """
        Count the number of occurrences of the passes value
        :param value: any
        :return: None
        """
        if not self.next:
            return 1 if self.value == value else 0
        return self.next.count(value) + (1 if self.value == value else 0)

    def merge(self, other):
        """
        Merge this list with the passed one by taking nodes alternatively
        :param other: Node
        :return: None
        """
        if not other:
            return
        self.next.merge(other.next)
        other.next = self.next
        self.next = other

    def penultimate(self):
        if not self.next:
            return None
        return self if self.next.next is None else self.next.penultimate()

    def pop(self, index=0):
        if index == 0:
            if self.next:
                self.value = self.next
                self.next = self.next.next
            else:
                self.value = None
        else:
            self.next.pop(index - 1)

    def prepend(self, value): # why not just self = new node?
        """
        Add a node to the front of the list with the passed value
        :param value:
        :return:
        """
        node = Node(value, self.next)
        self.next = node
        self.value, self.next.value = self.next.value, self.value

    def remove_duplicates(self):
        """
        Let only one occurrence of each value remain in the list
        :return: None
        """
        if not self.next:
            return
        self.next.remove_duplicates()
        current = self
        while current.next is not None:
            if current.next.value == self.value:
                current.next = current.next.next
            else:
                current = current.next

    def swap_after(self, value):
        """
        Swap the two nodes which come right after the first occurrence of the passed value
        :param value: any
        :return: None
        """
        if not (self.next and self.next.next):
            return
        if self.value == value:
            self.next.value, self.next.next.value = self.next.next.value, self.next.value
        else:
            self.next.swap_after(value)

    def tail(self):
        if not self.next:
            return self
        return self.next.tail()

