import copy
from node import Node

if __name__ == '__main__':

    n = Node(10)
    n.append(11)
    n.prepend(9)
    n.append(12)
    print(n)
    reversed(n)
    print(n)


