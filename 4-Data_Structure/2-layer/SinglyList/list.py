from node import Node


class List:
    def __init__(self):
        self.head = self.tail = None

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

    def __reversed__(self):
        current = self.head
        prev = None
        while current != self.tail:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.tail.next = prev
        self.head, self.tail = self.tail, self.head

    def __setitem__(self, index, value):
        current = self.head
        for i in range(index):
            current = current.next
        current.value = value

    def __str__(self):
        str = ""
        current = self.head
        while current:
            str += "{} -> ".format(current)
            current = current.next
        str += '|'
        return str

    def append(self, value):
        if not self.head:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def merge(self, other):
        """
        Merge this list with the passed one by taking node alternatively
        :param other: any
        :return: None
        """
        current1 = self.head
        current2 = other.head
        while current1 and current2:
            old_current2_nxt = current2.next
            current1.next, current2.next = current2, current1.next
            current1 = current2.next
            current2 = old_current2_nxt
        self.tail.next = current2
        self.tail = other.tail

    def pop(self, index=-1):
        if index == 0:
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next

    def prepend(self, value):
        node = Node(value, self.head)
        self.head = node

    def remove_duplicates(self):
        current = self.head
        s = {current.value}
        while current.next:
            if current.next.value in s:
                current.next = current.next.next
            else:
                s.add(current.next.value)
                current = current.next





