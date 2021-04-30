from Node import Node
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = Node(10)
    n.append(11)
    n.prepend(9)
    n.append(10)

    print(n)
    print(11 in n)
    n.remove_duplicates()
    print(n)

