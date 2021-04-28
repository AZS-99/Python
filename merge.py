def merge_sort(lst: list) -> list:
    """
    Return the passed list in
    """
    if len(lst) < 2:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(lst1: list, lst2: list) -> list:
    i = j = 0
    sorted = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            sorted.append(lst1[i])
            i += 1
        else:
            sorted.append(lst2[j])
            j += 1

    return sorted + lst1[i:] + lst2[j:]