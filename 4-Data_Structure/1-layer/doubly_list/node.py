class Node:
    def __init__(self, value, nxt=None, prev=None):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __str__(self):
        if not self.next:
            return "{} -> |".format(self.value)
        return "{} -> {}".format(self.value, self.next)

    def __getitem__(self, index):
        return self.value if index == 0 else self.next[index - 1]

    def __len__(self):
        return 1 if not self.next else len(self.next) + 1

    def append(self, value):
        if not self.next:
            node = Node(value, None, self)
            self.next = node
        else:
            self.next.append(value)

    def cut(self, value):
        """
        front and tail are the first and last Nodes in a doubly-linked list.
        cut_point is a Node somewhere in the list. Move all the Nodes
        before cut_point to the end of the list (keeping their order the same),
        making cut_point the new front. Return a tuple containing the first and
        last Nodes in the resulting doubly-linked list. Precondition: the list
        is not empty. Example: if the list contains the data 1, 2, 3, 4 and
        cut_point points to the node containing 3, then the resulting list
        should contain the data 3, 4, 1, 2.
        :param value:
        :return:
        """
        # if not self.next:
        #     return
        # penultimate = self.penultimate()
        # tmp = penultimate.next
        # penultimate.next = None
        # depth = self.depth(value)
        # self.cut(value)
        # self.insert(len(self) - depth, value)




    def depth(self, value):
        if not self:
            return 0
        return 1 if self.value == value else self.next.depth(value) + 1

    def insert(self, index, value):
        if index == 1:
            node = Node(value, self.next, self)
            self.next = node
            node.next.prev = node
        else:
            self.next.insert(index - 1, value)


    def penultimate(self):
        if not self.next:
            return None
        return self if not self.next.next else self.next.penultimate()




