class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        height = self.height()
        string = ""
        for _ in range(height):
            string += self.print_level(_)
            string += '\n'
        return string

    def __len__(self):
        if not (self.left or self.right):
            return 1
        return (len(self.left) if self.left else 0) + (len(self.right) if self.right else 0) + 1

    def find_far_right_leaf(self):
        if not self.right:
            return None, self
        elif not self.right.right:
            return self, self.right
        else:
            return self.right.find_far_right_leaf()

    # Note that Python pointers are all of type (void*), so once self.left/self.right is None, its pointer doesn't hold
    # the type "Node", and the interpreter wouldn't know what "height" to look into, so we need the ternary
    def height(self):
        if not (self.right or self.left):
            return 1
        return max(self.left.height() if self.left else 0, self.right.height() if self.right else 0) + 1

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = Node(value)
                return True
            else:
                return self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = Node(value)
                return True
            else:
                return self.right.insert(value)
        return False

    def print_level(self, level):
        if level == 0:
            return str(self.value)
        return (self.left.print_level(level - 1) if self.left else "\u03C6") + " " + \
               (self.right.print_level(level - 1) if self.right else "\u03C6")

    def remove_root(self):
        if not self.left:
            parent, node = self.find_far_right_leaf()
            node.value, self.value = self.value, node.value
            parent.right = None
        elif not self.left.right:
            self.left.value, self.value = self.value, self.left.value
            self.left = self.left.left
        else:
            parent, node = self.left.find_far_right_leaf()
            node.value, self.value = self.value, node.value
            parent.right = None





