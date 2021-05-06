from node import Node

if __name__ == '__main__':
    n = Node(10)
    print(n.insert(11))
    print(n.insert(7))
    print(n.insert(0))
    print(n.insert(20))
    n.insert(8)
    n.insert(30)
    n.insert(9)

    print(n)
    n.remove_root()
    print(n)