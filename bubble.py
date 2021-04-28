def bubble_sort(lst: list) -> list:
    length = len(lst)
    for i in range(0, length):
        element = lst[i]
        index = i
        for j in range (i + 1, length):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst
