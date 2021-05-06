from node import Node

if __name__ == '__main__':
    n = Node(10)
    print(n.insert(11))
    print(n.insert(9))
    print(n.insert(0))
    print(n.insert(20))

    print(len(n))