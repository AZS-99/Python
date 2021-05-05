from node import Node


class List:
    def __init__(self):
        self.head = None

    def __contains__(self, item):
        current = self.head
        while current:
            if current.value == item:
                return True
            current = current.next
        return False

    def __eq__(self, other):
        current1 = self.head
        current2 = other.head
        while current1 and current2:
            if current1.value != current2.value:
                return False
        return False if (current1 or current2) else True

    def __copy__(self):
        lst = List()
        current = self.head
        while current:
            lst.append(current.value)
            current = current.next
        return lst

    def __getitem__(self, index):
        current = self.head
        for i in range(index):
            current = current.next
            if not current:
                raise IndexError
        return current.value

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __setitem__(self, index, value):
        current = self.head
        for i in range(index):
            current = current.next
        current.value = value

    def __str__(self):
        str = ""
        current = self.head
        while current:
            str += "{} ->".format(current)
            current = current.next
        str += '|'
        return str

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

