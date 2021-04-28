def insert_sort(lst: list) -> list:
    if len(lst) < 2:
        return lst
    lst2 = insert_sort(lst[1:])
    element = lst[0]
    not_inserted = True
    i = 0
    while not_inserted is True:
        if lst2[i] > element:
            lst2.insert(i, element)
            not_inserted = False
    return lst2
