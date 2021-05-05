from list import List
from copy import copy

if __name__ == '__main__':
    lst = List()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    print(lst)
    lst2 = copy(lst)
    print(30 in lst)
    print(lst2)
    print(len(lst))
    print(lst[5])
